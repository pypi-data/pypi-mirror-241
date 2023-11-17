from pathlib import Path
import logging

import numpy as np
import pandas as pd

# from pandas.io.json import json_normalize
import requests
import geopandas as gpd
import rasterio

import sa_gwdata

# Import database connection if needed.
from .sageodata_database import connect
from ._hydstra import *
from . import _aquarius_ts
from .utils import *


logger = get_logger()


def fetch_wl_data(
    wells,
    include_replacements=False,
    ts_agg_ndays=5,
    ts_agg_methods=None,
    conn=None,
    aq=None,
    **kwargs,
):
    """Fetch and merge water level data from SA Geodata and Aquarius.

    Args:
        wells: either a list of :class:`sa_gwdata.Well` objects
            or a :class:`pandas.DataFrame` with a column
            "unit_long"
        include_replacements (bool): splice data from replacement wells for
            SA Geodata. ***NOTE***: this does NOT include AQTS data for
            replaced wells.
        conn (sageodata_db.Connection): server
        aq (dew_gwdata.DEWAquarius): server
        ts_agg_ndays (int): aggregate continuous TS data from AQTS to
            a given number of days
        ts_agg_methods (dict): how to aggregate AQ TS data.
            None means to use :func:`dew_gwdata.reduce_to_interval`'s
            default argument.

    Other keyword arguments are passed to
    :func:`dew_gwdata.DEWAquarius.fetch_timeseries_data`

    Aquarius data is retrieved from Aquarius TimeSeries production.

    Note that by default the logger data from Hydstra is requested as the
    mean of every 5 day window of data. You can increase the frequency (and
    time taken for the request) by using the *interval* and *multiplier* keyword
    arguments to this function. They are documented in
    :func:`dew_gwdata.fetch_hydstra_dtw_data`.

    Returns:
        :class:`pandas.DataFrame`

    """
    if conn is None:
        conn = connect()
    if aq is None:
        aq = _aquarius_ts.DEWAquarius()

    logger.debug(f"Requesting {len(wells)} wells: {wells}")

    try:
        assert isinstance(wells[0], sa_gwdata.Well)
        # It is a list of Well objects.
        potential_aq_sites = [w.unit_no.hyphen for w in wells]
    except (AssertionError, KeyError) as e:
        # It is a table e.g. from conn.drillhole_details()
        potential_aq_sites = wells.unit_hyphen.values

    # Filter to only those locations which exist in AQTS:
    aqdf = aq.fetch_locations_timeseries_metadata(potential_aq_sites)
    aq_sites = [u for u in aqdf.loc_id.unique()]
    logger.debug(
        f"Found {len(aq_sites)} of {len(wells)} wells as locations in AQTS: {aq_sites}"
    )

    logger.debug(
        f"Fetching SA Geodata water levels for all {len(potential_aq_sites)} wells"
    )
    wells = conn.find_wells(",".join([str(x) for x in potential_aq_sites]))

    logger.debug(f"Located {len(wells)} wells.\n{str(wells.dh_no)}")
    sag_wls = conn.water_levels(wells.dh_no, include_replacements=include_replacements)
    sag_wls["database"] = "SA Geodata"

    aq_dfs = {}
    if len(aq_sites) > 0:
        aq_md = aq.fetch_locations_timeseries_metadata(aq_sites)
        for aq_locid in aq_sites:
            aq_md2 = aq_md[
                (aq_md.loc_id == aq_locid)
                & (aq_md.param == "Depth to Water")
                & (aq_md.label.str.startswith("Best Available"))
                & (aq_md.label != "Best Available--Hydstra 110")
            ]
            logger.debug(
                f"Timeseries found for {aq_locid}:\n{aq_md2[['param', 'label']]}"
            )
            if len(aq_md2) == 0:
                ts_uid = None
                logger.debug(f"none found - skipping.")
            elif len(aq_md2) == 1:
                ts_uid = aq_md2.ts_uid.iloc[0]
                logger.debug(f"one found - using {ts_uid}")
            else:
                ts_uid = aq_md2.ts_uid.iloc[0]
                logger.warning(f"multiple timeseries: using {ts_uid}")
            if not ts_uid is None:
                logger.debug(f"Fetching AQTS data for {aq_locid} ts_uid={ts_uid}")
                df = aq.fetch_timeseries_data(ts_uid=ts_uid)
                #     locid=aq_locid, param="Depth to Water", label=label, label_startswith=False
                # )
                logger.debug(f"fetched {len(df)} data points")
                logger.debug(
                    f"before reduction to {ts_agg_ndays} days ts_agg_methods={ts_agg_methods}: {len(df)} data points, {df.columns}"
                )
                if len(df):
                    df = reduce_to_interval(
                        df, ts_agg_ndays, dt_col="timestamp", aggs=ts_agg_methods
                    )
                else:
                    logger.debug("skipped reduction - df has no records")
                logger.debug(f"after reduction: {len(df)} data points, {df.columns}")
                df = df.rename(
                    columns={"Depth to Water": "dtw", "timestamp": "obs_date"}
                )
                df["unit_hyphen"] = aq_locid
                if len(df):
                    df["obs_date"] = df.obs_date.dt.tz_localize(None)
                aq_dfs[aq_locid] = df

    if len(aq_dfs):
        aqdf = pd.concat(aq_dfs)

        elevs = conn.elevation_surveys(wells)
        logger.debug(f'Fetched AQTS DTW for\n{aqdf.groupby("unit_hyphen").dtw.count()}')

        series = transform_dtw_to_rswl(aqdf, elevs, well_id_col="unit_hyphen")
        aqdf["rswl"] = series.values
        aqdf["database"] = "Aquarius"
        aqdf["anomalous_ind"] = "N"
        aqdf.loc[aqdf.grade <= 0, "anomalous_ind"] = "Y"
        logger.debug(
            f'Calculated RSWL for data from AQTS for\n{aqdf.groupby("unit_hyphen").rswl.count()}'
        )
        if len(aqdf):
            dh_details = conn.drillhole_details(
                conn.find_wells(",".join([str(u) for u in aqdf.unit_hyphen.unique()]))
            )
            aqdf = pd.merge(
                dh_details,
                aqdf[[x for x in aqdf.columns if not x == "well_id"]],
                how="outer",
                on="unit_hyphen",
            )
            ret_df = pd.concat([sag_wls, aqdf], sort=False).sort_values(
                by=["unit_long", "obs_date"]
            )
        else:
            ret_df = sag_wls
    else:
        ret_df = sag_wls.sort_values(by=["unit_long", "obs_date"])

    # make sure all columns are present.
    extra_cols = {
        "database": "",
        "quality_code": pd.NA,
        "grade": pd.NA,
    }
    for col, value in extra_cols.items():
        if not col in ret_df:
            ret_df[col] = value
    return ret_df


def reduce_to_interval(
    df,
    ndays=5,
    dt_col="obs_date",
    aggs=None,
):
    """Reduce to a less frequent daily interval e.g. daily, weekly, monthly.

    Args:
        df (pandas.DataFrame): dataset
        ndays (int): number of days (interval length)
        dt_col (str): name of column in *df* containing the timestamps

    Returns:
        A pandas.DataFrame. The index is a set of datetime objects spaced at an
        interval of *ndays*; the values are those from *data_col*, aggregated by
        the method *agg_method*.

    """
    if aggs is None:
        aggs = {
            "Depth to Water": "mean",
            "grade": "min",
            "approval": "first",
            "qualifier": "first",
        }
    logger.debug(f"Reducing data by ndays={ndays} dt_col={dt_col} aggs={aggs}")
    offset = pd.Timedelta(ndays, "d") / 2
    grouper = pd.Grouper(key=dt_col, freq=f"{ndays:.0f}d", label="left")
    logger.debug(f"offset={offset} grouper={grouper}")
    df2 = df.groupby(grouper)[list(aggs.keys())].agg(aggs)
    df2 = df2.shift(1, freq=(offset)).reset_index()
    return df2


def transform_dtw_to_rswl(
    edf,
    elevs,
    well_id_col="unit_long",
    dt_col="obs_date",
    dtw_col="dtw",
    rswl_col="rswl",
):
    """Convert depth to water (m) to reduced standing water level (m AHD).

    Args:
        edf (:class:`pandas.DataFrame`): water level observations
        elevs (:class:`pandas.DataFrame`): elevation surveys from SA Geodata
            (see :meth:`dew_gwdata.SAGeodataConnection.elevation_surveys`)
        well_id_col (str): if *edf* and *elevs* have data from more than one
            well in them, you will need to provide the field name which can
            be used to correlate data between the two dataframes. By default,
            when using Hydstra and SA Geodata, this value should be "unit_long"
        dt_col (str): column with WL measurement date in *edf*
        dtw_col (str): column with DTW measurement in *edf*
        rswl_col (str): column to be created with RSWL measurement

    Returns: :class:`pandas.Series`

    Example:

        >>> import dew_gwdata as gd
        >>> db = gd.connect()
        >>> wells = db.find_wells('PLL019')
        >>> df = db.water_levels(wells)
        >>> elevs = db.elevation_surveys(wells)
        >>> df["rswl_custom"] = gd.transform_dtw_to_rswl(df, elevs)

    """
    if len(edf) == 0:
        return pd.Series(name=rswl_col)

    def per_well_apply(well_df):
        well_elevs = elevs[elevs[well_id_col] == well_df[well_id_col].iloc[0]]
        x = transform_dtw_to_rswl(
            well_df,
            well_elevs,
            well_id_col=None,
            dt_col=dt_col,
            dtw_col=dtw_col,
            rswl_col=rswl_col,
        )
        if not isinstance(x, pd.DataFrame):
            x = x.to_frame()
        return x

    if well_id_col in edf and well_id_col in elevs:
        results = edf.groupby(well_id_col, as_index=False).apply(per_well_apply)
        return results.droplevel(0)[rswl_col]

    if "well_id" in edf:
        logger.debug(f'Calculating DTW -> RSWL transform for {edf["well_id"].unique()}')
    edf2 = edf.copy()
    edf2[rswl_col] = np.nan
    elevs["ref_elev"] = pd.to_numeric(elevs["ref_elev"])
    elev_records = elevs.to_dict(orient="records")
    if len(elevs) == 0:
        logger.debug("No elevation records present")
        return edf2
    if len(elevs) == 1:
        logger.debug("One elevation record present.")
        elev = elev_records[0]
        if isinstance(elev["applied_date"], pd.Timestamp):
            logger.debug(f'Applied date of {elev["applied_date"]} exists')
            if not np.isnan(elev["ref_elev"]):
                edf2.loc[edf2[dt_col] >= elev["applied_date"], rswl_col] = (
                    elev["ref_elev"] - edf2[dtw_col]
                )
            elif not np.isnan(elev["ground_elev"]):
                edf2.loc[edf2[dt_col] >= elev["applied_date"], rswl_col] = (
                    elev["ground_elev"] - edf2[dtw_col]
                )
        else:
            logger.debug("No applied date exists")
            if not np.isnan(elev["ref_elev"]):
                edf2.loc[:, rswl_col] = elev["ref_elev"] - edf2[dtw_col]
            elif not np.isnan(elev["ground_elev"]):
                edf2.loc[:, rswl_col] = elev["ground_elev"] - edf2[dtw_col]
    else:
        logger.debug(f"{len(elevs)} elevation records found")
        if np.any([isinstance(x["applied_date"], pd.Timestamp) for x in elev_records]):
            logger.debug("At least one applied date exists")
            # There is at least one applied date.
            applied_recs = sorted(
                [e for e in elev_records if e["applied_date"]],
                key=lambda x: x["applied_date"],
            )

            if np.all([~pd.isnull(x["ref_elev"]) for x in applied_recs]):
                logger.debug("All records have finite ref_elev")
                for elev in elev_records:
                    idx = edf2[dt_col] >= elev["applied_date"]
                    edf2.loc[idx, rswl_col] = (elev["ref_elev"] - edf2[dtw_col])[idx]
            elif np.all([~pd.isnull(x["ground_elev"]) for x in applied_recs]):
                logger.debug("All records have finite ground_elev")
                for elev in elev_records:
                    idx = edf2[dt_col] >= elev["applied_date"]
                    edf2.loc[idx, rswl_col] = (elev["ground_elev"] - edf2[dtw_col])[idx]
        else:
            elev = sorted(elev_records, key=lambda x: x["elev_date"])[-1]
            logger.debug(
                f'No records have an applied_date. Therefore using most recent data of {elev["elev_date"]}'
            )
            if not np.isnan(elev["ref_elev"]):
                edf2.loc[:, rswl_col] = elev["ref_elev"] - edf2[dtw_col]
            else:
                edf2.loc[:, rswl_col] = elev["ground_elev"] - edf2[dtw_col]

    return edf2[rswl_col]


def make_drillhole_events_table(
    wls,
    sals,
    const,
    elevs,
    wde_maint,
    wde_alerts,
    wde_logger_installs,
    wde_logger_reads,
):
    """Construct a table of events for a well.

    Args:
        wls (pandas.DataFrame): from predefined query "water_levels"
        sals (pandas.DataFrame): from predefined query "water_levels"
        const (pandas.DataFrame): from predefined query "water_levels"
        elevs (pandas.DataFrame): from predefined query "water_levels"
        wde_maint (pandas.DataFrame): from predefined WDE query "maintenance_issues" with
            additional columns "well_id" and "unit_hyphen"
        wde_alerts (pandas.DataFrame): from predefined WDE query "alerts" with
            additional columns "well_id" and "unit_hyphen"
        wde_logger_installs (pandas.DataFrame): from predefined WDE query "logger_installations" with
            additional columns "well_id" and "unit_hyphen"
        wde_logger_reads (pandas.DataFrame): from predefined WDE query "logger_readings" with
            additional columns "well_id" and "unit_hyphen"

    Returns: pandas DataFrame with columns:

    - well_id
    - event_date
    - event_type
    - param_type
    - param_value
    - details
    - comments
    - created_by
    - creation_date
    - modified_by
    - modified_date

    """

    # Water levels
    wls = wls.rename(columns={"obs_date": "event_date"}).assign(
        event_type="Water level",
        details="",
        param_type="",
        param_value="",
        comments="",
    )
    if len(wls.rswl.dropna()) > 0:
        wls["param_type"] = "DTW | SWL | RSWL"
        wls["param_value"] = wls.apply(
            (lambda row: f"{row.dtw:.2f} | {row.swl:.2f} | {row.rswl:.2f}"),
            axis="columns",
        )
    else:
        wls["param_type"] = "DTW | SWL"
        wls["param_value"] = wls.apply(
            (lambda row: f"{row.dtw:.2f} | {row.swl:.2f}"), axis="columns"
        )

    # Salinity
    sals = sals.rename(columns={"collected_date": "event_date"}).assign(
        event_type="Salinity",
        param_type="EC | TDS",
        param_value="",
        details="",
    )
    sals["details"] = sals.apply(
        (lambda row: f"{row.extract_method} by {row.collected_by}"),
        axis="columns",
    )
    sals["param_value"] = sals.apply(
        (lambda row: f"{row.ec:.0f} | {row.tds:.0f}"), axis="columns"
    )

    # Construction events
    const = const.rename(
        columns={
            "completion_date": "event_date",
            "current_depth": "param_value",
            #             "construction_aquifer": "details",
        }
    ).assign(
        param_type="Current depth",
        details="",
    )
    const["event_type"] = const.event_type.map({"C": "Construction", "S": "Survey"})
    const["comments"] = const.apply(
        (
            lambda row: (
                f"{'Aquifer: ' + row.construction_aquifer + ' ' if row.construction_aquifer else ''}"
                f"{row.comments}"
            )
        ),
        axis="columns",
    )

    # Elevation surveys
    elevs = elevs.rename(columns={"elev_date": "event_date"}).assign(
        event_type="Elevation survey",
        param_type="Ground | Ref. pt",
        param_value="",
        details="",
    )
    elevs["param_value"] = elevs.apply(
        (lambda row: f"{row.ground_elev} | {row.ref_elev}"), axis="columns"
    )
    elevs["details"] = elevs.apply(
        (
            lambda row: (
                f"{row.ref_point_type} ({row.ref_height}) "
                f"using {row.survey_meth} applied"
                f"{' from ' + row.applied_date.strftime('%Y-%m-%d') if not pd.isnull(row.applied_date) else ''}"
            )
        ),
        axis="columns",
    )

    # WDE maintenance
    wde_reports = wde_maint.rename(
        columns={"reported_date": "event_date", "reported_by": "created_by"}
    ).assign(
        event_type="WDE maintenance issue report",
        param_type="",
        param_value="",
        details="",
        creation_date=None,
        modified_by="",
        modified_date=None,
    )
    if len(wde_reports):
        wde_reports["details"] = wde_reports.priority.apply(lambda v: f"Priority {v}")

    wde_res = (
        wde_maint[~wde_maint.completed_date.isnull()]
        .rename(columns={"completed_date": "event_date", "created_by": "actioned_by"})
        .assign(
            event_type="WDE maintenance issue resolution",
            param_type="",
            param_value="",
            details="",
            creation_date=None,
            modified_by="",
            modified_date=None,
        )
    )
    if len(wde_res):
        wde_res["details"] = wde_res.priority.apply(lambda v: f"Priority {v}")
        wde_res["comments"] = wde_res.apply(
            (
                lambda row: (
                    f"{row.comments} resolved: "
                    f"{row.action_comments} {row.action_other}"
                )
            ),
            axis="columns",
        )

    # WDE alerts
    wde_alerts = wde_alerts.rename(
        columns={"creation_date": "event_date", "description": "comments"}
    ).assign(
        event_type="WDE alert",
        param_type="",
        param_value="",
        details="",
        creation_date=None,
        modified_by="",
        modified_date=None,
    )
    if len(wde_alerts):
        wde_alerts.loc[wde_alerts.active == True, "details"] = "Active"
        wde_alerts.loc[wde_alerts.active == False, "details"] = "Inactive"

    # Logger installations
    lg_inst = wde_logger_installs.rename(
        columns={"install_date": "event_date", "serial_no": "param_value"}
    ).assign(
        event_type="WDE Logger installation",
        param_type="S/N",
        creation_date=None,
        details="",
        created_by="",
        modified_by="",
        modified_date=None,
    )
    if len(lg_inst):
        lg_inst.loc[lg_inst.telemetry == True, "temp_telem"] = "Telemetered"
        lg_inst.loc[lg_inst.telemetry != True, "temp_telem"] = ""
        lg_inst["details"] = lg_inst.apply(
            (lambda row: f"{row.type} {row.model} {row.temp_telem}"),
            axis="columns",
        )

    # Logger readings
    lg_reads = wde_logger_reads.rename(
        columns={"reading_date": "event_date", "read_by": "created_by"}
    ).assign(
        event_type="WDE Logger read",
        param_type="Batt. | Mem. %",
        param_value="",
        details="",
        creation_date=None,
        modified_by="",
        modified_date=None,
    )
    if len(lg_reads):
        lg_reads["param_value"] = lg_reads.apply(
            (lambda row: f"{row.battery_pct} | {row.memory_pct}"), axis="columns"
        )

    # Chain together
    dfs = []
    cols = [
        "dh_no",
        "unit_hyphen",
        "well_id",
        "event_date",
        "event_type",
        "param_type",
        "param_value",
        "details",
        "comments",
        "created_by",
        "creation_date",
        "modified_by",
        "modified_date",
    ]
    for df in (wls, sals, const, elevs, wde_reports, wde_alerts, lg_inst, lg_reads):
        if "event_date" in df:
            if len(df):
                df["event_date"] = df.event_date.dt.date
        df["comments"] = df.comments.fillna("")
        dfs.append(df[cols])
    df = pd.concat(dfs).sort_values("event_date")
    df = df[~pd.isnull(df.event_date)]
    return df


class StratigraphyHierarchy:
    """Tables of stratigraphic units and tools for working with them.

    Args:
        db (SAGeodataConnection): default None i.e. created as needed

    Other keywords args are passed to SAGeodataConnection i.e. for
    getting into QA or Dev; production  by default

    Attributes:
        strat (pd.DataFrame): a table of all stratigraphic units
        tlstrat (pd.DataFrame): a table of the top-level stratigraphic
            units as used in SA Geodata codes i.e. eons for the Precambrian, then
            periods for the Phanerozoic (but using Tertiary instead of Palaeogene
            and Neogene).

    The columns in strat are:

        >>> st = StratigraphyHierarchy()
        >>> st.strat.info()
        <class 'pandas.core.frame.DataFrame'>
        RangeIndex: 2536 entries, 0 to 2535
        Data columns (total 4 columns):
         #   Column                Non-Null Count  Dtype
        ---  ------                --------------  -----
         0   strat_unit_no         2536 non-null   int64
         1   parent_strat_unit_no  2422 non-null   float64
         2   map_symbol            2536 non-null   object
         3   strat_name            2536 non-null   object
        dtypes: float64(1), int64(1), object(2)
        memory usage: 79.4+ KB
        >>> print(st.strat.head())
           strat_unit_no  parent_strat_unit_no map_symbol                strat_name
        0           2960                   NaN          A            Archaean rocks
        1           4608                2960.0        A-c         Cooyerdoo Granite
        2           6684                4608.0       A-c1  Cooyerdoo Granite unit 1
        3           3462                2960.0        A-o           Coolanie Gneiss
        4           6685                2960.0         A1           Archaean unit 1

    tlstrat is:

        >>> st.tlstrat.info()
        <class 'pandas.core.frame.DataFrame'>
        Int64Index: 51 entries, 28 to 0
        Data columns (total 8 columns):
         #   Column                Non-Null Count  Dtype
        ---  ------                --------------  -----
         0   strat_unit_no         51 non-null     int64
         1   parent_strat_unit_no  0 non-null      object
         2   map_symbol            51 non-null     object
         3   strat_name            51 non-null     object
         4   start                 51 non-null     float64
         5   end                   51 non-null     float64
         6   oldest_unit           51 non-null     object
         7   youngest_unit         51 non-null     object
        dtypes: float64(2), int64(1), object(5)
        memory usage: 3.6+ KB
        >>> print(st.tlstrat[['strat_unit_no', 'map_symbol', 'strat_name']])
                    strat_unit_no map_symbol                               strat_name
        28           3106          Q                         Quaternary rocks
        35           3210         TQ               Tertiary-Pleistocene rocks
        34           3187          T                           Tertiary rocks
        49           6902         KT              Cretaceous toTertiary rocks
        50           2992        KTa               Cretaceous-Paleocene rocks
        48           2990          K                         Cretaceous rocks
        47           2989         JT                  Jurassic-Tertiary rocks
        46           4574         JK                Jurassic-Cretaceous rocks
        45           2986          J                           Jurassic rocks
        31           4760         RK                           Mesozoic rocks
        30           3185         RJ                  Triassic-Jurassic rocks
        29           3184          R                           Triassic rocks
        6            2968         CK           Carboniferous-Cretaceous rocks
        8            5815         CR             Carboniferous-Triassic rocks
        5            2967          C                      Carboniferous rocks
        25           6877         PQ                 Permian-Quaternary rocks
        27           6772         PT                   Permian-Tertiary rocks
        24           5650         PJ                   Permian-Jurassic rocks
        26           3103         PR                   Permian-Triassic rocks
        7            2970         CP              Carboniferous-Permian rocks
        23           2997          P                            Permian rocks
        9            2971          D                           Devonian rocks
        33           6020         SD                  Silurian-Devonian rocks
        32           3186          S                           Silurian rocks
        21           2995         OD                Ordovician-Devonian rocks
        22           5893         OS                Ordovician-Silurian rocks
        20           4421          O                         Ordovician rocks
        12           5281         EK                Cambrian-Cretaceous rocks
        14           2985         EP                         Palaeozoic rocks
        11           5593         ED                  Cambrian-Devonian rocks
        15           6790         ES                  Cambrian-Silurian rocks
        13           2978         EO                Cambrian-Ordovician rocks
        10           4698          E                           Cambrian rocks
        18           5013         NK          Neoproterozoic-Cretaceous rocks
        19           6445         NO          Neoproterozoic-Ordovician rocks
        17           2999         NE            Neoproterozoic-Cambrian rocks
        16           3037          N                     Neoproterozoic rocks
        37           6691         ME           Mesoproterozoic-Cambrian rocks
        38           4976         MN     Mesoproterozoic-Neoproterozoic rocks
        36           3000          M                    Mesoproterozoic rocks
        41           6798         YK       Palaeoproterozoic-Cretaceous rocks
        44           6797         YP          Palaeoproterozoic-Permian rocks
        40           5589         YE         Palaeoproterozoic-Cambrian rocks
        43           4736         YN                        Proterozoic rocks
        42           5012         YM  Palaeoproterozoic-Mesoproterozoic rocks
        39           4724          Y                  Palaeoproterozoic rocks
        1            6663         AD                  Archaean-Devonian rocks
        3            6451         AO                Archaean-Ordovician rocks
        2            6234         AM           Archaean-Mesoproterozoic rocks
        4            2961         AY         Archaean-Palaeoproterozoic rocks
        0            2960          A                           Archaean rocks

    """

    all_ages = [
        ("Qh", 11.7e3 / 1e6, 0),
        ("Qp", 2.58, 11.7e3 / 1e6),
        ("Q", 2.58, 0),
        ("Tp", 5.333, 2.58),
        ("Tm", 23.03, 5.333),
        ("To", 33.9, 23.03),
        ("Te", 56, 33.9),
        ("Ta", 66, 56),
        ("T", 66, 2.58),
        ("K", 145, 66),
        ("J", 201.4, 145),
        ("R", 251.9, 201.4),
        ("C", 298.9, 251.9),
        ("P", 358.9, 298.9),
        ("D", 419.2, 358.9),
        ("S", 443.8, 419.2),
        ("O", 485.4, 443.8),
        ("E", 538.8, 485.4),
        ("N", 1000, 538.8),
        ("M", 1600, 1000),
        ("Y", 2500, 1600),
        ("A", 4000, 2500),
    ]

    def __init__(self, db=None, **kwargs):
        if db is None:
            import sageodata_db

            db = sageodata_db.connect(**kwargs)
        self.db = db

        df = self.db.query(
            """
            select
                st.strat_unit_no,
                st.subdiv_strat_unit_no as parent_strat_unit_no,
                st.map_symbol,
                st.strat_name
            from
                dhdb.st_strat_unit_vw st
            where
                st.map_symbol is not null
        """
        )
        self.strat = self.add_missing_parents(df)
        self.tlstrat = self._build_top_level_units()

    @staticmethod
    def add_missing_parents(df):
        copy = df.copy()
        copy.loc[
            copy.map_symbol.str.startswith("T")
            & (~copy.map_symbol.isin(["T", "TQ"]))
            & pd.isnull(copy.parent_strat_unit_no),
            "parent_strat_unit_no",
        ] = 3187
        copy.loc[copy.map_symbol == "JK-h", "parent_strat_unit_no"] = 4574
        copy.loc[
            copy.map_symbol.isin(["ME1", "Mt", "Mr", "Mthhdj"]), "parent_strat_unit_no"
        ] = 3000
        copy.loc[copy.map_symbol == "N-m", "parent_strat_unit_no"] = 3037
        copy.loc[copy.map_symbol == "Omy", "parent_strat_unit_no"] = 4421
        return copy

    def _build_top_level_units(self):
        units = self.db.query(
            """
            select
                st.strat_unit_no,
                st.subdiv_strat_unit_no as parent_strat_unit_no,
                st.map_symbol,
                st.strat_name
            from
                dhdb.st_strat_unit_vw st
            where
                st.subdiv_strat_unit_no is null
                and st.map_symbol is not null
        """
        )
        units = self.add_missing_parents(units)
        units = units[pd.isnull(units.parent_strat_unit_no)]

        records = []
        for idx, row in units.iterrows():
            ages = [
                (i, (sym, start, end))
                for i, (sym, start, end) in enumerate(self.all_ages)
                if sym in row.map_symbol
            ]
            min_age = 9999
            max_age = -1
            max_age_sym = ""
            min_age_sym = ""
            for i, (sym, start, end) in ages:
                if start > max_age:
                    max_age = start
                    max_age_sym = sym
                if end < min_age:
                    min_age = end
                    min_age_sym = sym
            record = row.to_dict()
            record["start"] = max_age
            record["end"] = min_age
            record["oldest_unit"] = max_age_sym
            record["youngest_unit"] = min_age_sym
            if record["start"] != -1:
                records.append(record)
        return pd.DataFrame(records).sort_values(["start", "end"])

    def _find_strat_unit_parentage(self, unit_chain):
        df = self.strat
        broadest_unit = unit_chain[0]
        finest_unit = unit_chain[-1]
        parent_units = df[df["strat_unit_no"] == broadest_unit]
        if len(parent_units) == 0:
            return unit_chain
        elif len(parent_units) == 1:
            row = parent_units.iloc[0]
            broader_unit = row.parent_strat_unit_no
            if pd.isnull(broader_unit):
                return unit_chain
            else:
                unit_chain = [broader_unit] + list(unit_chain)
                return self._find_strat_unit_parentage(unit_chain)

    def _find_strat_unit_siblings(self, st_unit_no):
        df = self.strat
        parent_units = df[df["strat_unit_no"] == st_unit_no]
        if len(parent_units) == 0:
            return []
        else:
            row = parent_units.iloc[0]
            sibling_units = df[df.parent_strat_unit_no == row.parent_strat_unit_no]
            return [u for u in sibling_units.strat_unit_no if not u == st_unit_no]

    def _find_strat_unit_next_level_children(self, st_unit_no):
        df = self.strat
        child_units = df[df["parent_strat_unit_no"] == st_unit_no]
        if len(child_units) == 0:
            return []
        else:
            return list(child_units.strat_unit_no)

    def find_strat_parentage(self, map_symbol):
        strat = self.strat
        st_unit_no = strat[strat.map_symbol == map_symbol].iloc[0].strat_unit_no
        unit_chain = self._find_strat_unit_parentage([st_unit_no])
        records = [strat[strat.strat_unit_no == s].iloc[0] for s in unit_chain]
        return pd.DataFrame(records)

    def find_strat_siblings(self, map_symbol):
        strat = self.strat
        st_unit_no = strat[strat.map_symbol == map_symbol].iloc[0].strat_unit_no
        sibling_u_nos = self._find_strat_unit_siblings(st_unit_no)
        return strat[strat.strat_unit_no.isin(sibling_u_nos)]

    def find_strat_children(self, map_symbol, levels=1):
        strat = self.strat
        assert levels == 1
        st_unit_no = strat[strat.map_symbol == map_symbol].iloc[0].strat_unit_no
        child_u_nos = self._find_strat_unit_next_level_children(st_unit_no)
        return strat[strat.strat_unit_no.isin(child_u_nos)]


class Hydrostratigraphy(StratigraphyHierarchy):
    """Tables of hydrostratigraphic units and tools for working with them.

    Args:
        db (SAGeodataConnection): default None i.e. created as needed

    Other keywords args are passed to SAGeodataConnection i.e. for
    getting into QA or Dev; production by default

    This fundamentally relies on SA Geodata being correct:

    * all aquifer monitored codes referring to hydrostrat subunits
      with [SUxx] in their description
    * all hydrostrat sub-intervals referring to subunits with
      'HS LOG ONLY' in their description

    Attributes:
        hstrat (pd.DataFrame): a table of all potential hydrostrat subunits
        aqmon (pd.DataFrame): a table of all potential aquifer monitored subunits

    The columns in strat are:

        >>> st = Hydrostratigraphy()
        >>> st.strat.info()

        >>> print(st.strat.head())

    tlstrat is:

    """

    def __init__(self, *args, **kwargs):
        super(Hydrostratigraphy, self).__init__(*args, **kwargs)

        def create_unit_name(row):
            if row.hydro_subunit_code == "" or pd.isnull(row.hydro_subunit_code):
                return row.strat_name
            else:
                return f"{row.strat_name} - {row.hydro_subunit_name}"

        def create_unit_code(row):
            if row.hydro_subunit_code == "" or pd.isnull(row.hydro_subunit_code):
                return row.map_symbol
            else:
                return f"{row.map_symbol}({row.hydro_subunit_code})"

        df = self.db.query(
            """
            select
                su.strat_unit_no,
                su.map_symbol as strat_unit,
                hsu.hydro_subunit_code,
                su.map_symbol || hsu.hydro_subunit_code as aquifer_code,
                su.strat_name,
                hsu.hydro_subunit_desc as hydro_subunit_name
            from 
                dhdb.wa_hydrostrat_subunit_vw hsu
            left join 
                dhdb.st_strat_unit_vw su on hsu.strat_unit_no = su.strat_unit_no
        """
        )
        self.hsubunit_strat = df[
            df.hydro_subunit_name.str.contains("HS LOG ONLY", regex=False)
        ]

        aqmon = df[df.hydro_subunit_name.str.contains("[SU", regex=False)]
        aqmon["linked_strat_unit_no"] = aqmon.hydro_subunit_name.str.extract(
            r"\[SU(\d{1,4})\]"
        ).astype(int)

        self.pot_aqmon = pd.merge(
            aqmon,
            self.strat.rename(
                columns={
                    "strat_unit_no": "linked_strat_unit_no",
                    "map_symbol": "linked_map_symbol",
                    "strat_name": "linked_strat_name",
                }
            )[["linked_strat_unit_no", "linked_map_symbol", "linked_strat_name"]],
            on="linked_strat_unit_no",
            how="left",
        )

        # Get hydrostrat log sub-intervals, and aquifer monitored entries.
        df2a = self.db.query(
            """
            select
                su.strat_unit_no,
                su.map_symbol,
                hsu.hydro_subunit_code,
                su.map_symbol || hsu.hydro_subunit_code as aquifer_code,
                su.strat_name,
                hsu.hydro_subunit_desc as hydro_subunit_name,
                aqmon.drillhole_no as aqmon_dh_no,
                -- aqmon.constrn_date as aqmon_date,
                hsl_int.drillhole_no as hslog_dh_no
            from 
                dhdb.wa_hydrostrat_subunit_vw hsu
            left join dhdb.st_strat_unit_vw su 
                on hsu.strat_unit_no = su.strat_unit_no
            left join dhdb.dd_dh_aquifer_mon_vw aqmon 
                on aqmon.strat_unit_no = hsu.strat_unit_no and aqmon.hydro_subunit_code = hsu.hydro_subunit_code
            left join dhdb.wa_hydrostrat_subint_vw hsl_subint
                on hsl_subint.strat_unit_no = hsu.strat_unit_no and hsl_subint.hydro_subunit_code = hsu.hydro_subunit_code
            left join dhdb.wa_hydrostrat_int_vw hsl_int
                on hsl_int.hydro_int_no = hsl_subint.hydro_int_no
            """
        )
        # Get hydrostrat log intervals made up on purely strat unit entries.
        df2b = self.db.query(
            """
            select
                su.strat_unit_no,
                su.map_symbol,
                '' as hydro_subunit_code,
                su.map_symbol as aquifer_code,
                su.strat_name,
                '' as hydro_subunit_name,
                null as aqmon_dh_no,
                hsl_int.drillhole_no as hslog_dh_no
            from
                dhdb.wa_hydrostrat_int_vw hsl_int
            left join dhdb.st_strat_unit_vw su
                on hsl_int.strat_unit_no = su.strat_unit_no
        """
        )
        df2b["hydro_subunit_code"] = ""
        df2b["hydro_subunit_name"] = "HS LOG ONLY"
        df2 = pd.concat([df2a, df2b])
        df2 = df2.sort_values(
            ["map_symbol", "hydro_subunit_code", "hydro_subunit_name"]
        )
        df2_summ = (
            df2.groupby(
                [
                    "map_symbol",
                    "hydro_subunit_code",
                    "aquifer_code",
                    "strat_name",
                    "hydro_subunit_name",
                ]
            )
            .agg(
                count_aqmon=("aqmon_dh_no", lambda dh_nos: dh_nos.dropna().nunique()),
                count_hslog=("hslog_dh_no", lambda dh_nos: dh_nos.dropna().nunique()),
            )
            .reset_index()
        )

        self.hslog_use = (
            df2[~df2.hslog_dh_no.isnull()]
            .drop(["aquifer_code", "aqmon_dh_no"], axis=1)
            .drop_duplicates()
        )
        self.aqmon_use = (
            df2[~df2.aqmon_dh_no.isnull()]
            .drop(["hslog_dh_no"], axis=1)
            .drop_duplicates()
        )

        self.hslog_summ_use = df2_summ[df2_summ.count_hslog > 0].drop(
            ["aquifer_code", "count_aqmon"], axis=1
        )
        self.aqmon_summ_use = df2_summ[df2_summ.count_aqmon > 0].drop(
            ["count_hslog"], axis=1
        )

        self.hslog_use["unit_code"] = self.hslog_use.apply(create_unit_code, axis=1)
        self.hslog_summ_use["unit_code"] = self.hslog_summ_use.apply(
            create_unit_code, axis=1
        )

        hslog_valid = self.hslog_use.hydro_subunit_name.str.contains(
            "HS LOG ONLY", regex=False
        )
        self.hslog_errors = self.hslog_use[~hslog_valid]
        self.hslog_use = self.hslog_use[hslog_valid]

        self.hslog_summ_use = self.hslog_summ_use[
            self.hslog_summ_use.hydro_subunit_name.str.contains(
                "HS LOG ONLY", regex=False
            )
        ]

        aqmon_valid = self.aqmon_use.hydro_subunit_name.str.contains("SU", regex=False)
        self.aqmon_errors = self.aqmon_use[~aqmon_valid]
        self.aqmon_use = self.aqmon_use[aqmon_valid]

        self.aqmon_summ_use = self.aqmon_summ_use[
            self.aqmon_summ_use.hydro_subunit_name.str.contains("[SU", regex=False)
        ]

        self.aqmon_use[
            "linked_strat_unit_no"
        ] = self.aqmon_use.hydro_subunit_name.str.extract(r"\[SU(\d{1,4})\]").astype(
            int
        )
        self.aqmon_use = pd.merge(
            self.aqmon_use,
            self.strat.rename(
                columns={
                    "strat_unit_no": "linked_strat_unit_no",
                    "map_symbol": "linked_map_symbol",
                    "strat_name": "linked_strat_name",
                }
            )[["linked_strat_unit_no", "linked_map_symbol", "linked_strat_name"]],
            on="linked_strat_unit_no",
            how="left",
        )

        self.aqmon_summ_use[
            "linked_strat_unit_no"
        ] = self.aqmon_summ_use.hydro_subunit_name.str.extract(
            r"\[SU(\d{1,4})\]"
        ).astype(
            int
        )
        self.aqmon_summ_use = pd.merge(
            self.aqmon_summ_use,
            self.strat.rename(
                columns={
                    "strat_unit_no": "linked_strat_unit_no",
                    "map_symbol": "linked_map_symbol",
                    "strat_name": "linked_strat_name",
                }
            )[["linked_strat_unit_no", "linked_map_symbol", "linked_strat_name"]],
            on="linked_strat_unit_no",
            how="left",
        )

        self.aqmon_use = self.aqmon_use.rename(
            columns={"hydro_subunit_name": "aquifer_name"}
        )
        self.aqmon_summ_use = self.aqmon_summ_use.rename(
            columns={"hydro_subunit_name": "aquifer_name"}
        )

        hslog_units = self.strat[["strat_unit_no", "map_symbol", "strat_name"]]
        hslog_subunits = pd.merge(
            self.strat[["strat_unit_no", "map_symbol", "strat_name"]],
            self.hsubunit_strat[
                ["strat_unit_no", "hydro_subunit_code", "hydro_subunit_name"]
            ],
            on="strat_unit_no",
            how="right",
        )
        pot_hlog_units = pd.concat([hslog_units, hslog_subunits])
        pot_hlog_units["hydro_subunit_code"] = pot_hlog_units[
            "hydro_subunit_code"
        ].fillna("")
        pot_hlog_units["hydro_subunit_name"] = pot_hlog_units[
            "hydro_subunit_name"
        ].fillna("")
        pot_hlog_units["unit_name"] = pot_hlog_units.apply(create_unit_name, axis=1)
        pot_hlog_units["unit_code"] = pot_hlog_units.apply(create_unit_code, axis=1)
        pot_hlog_units = pot_hlog_units.sort_values("unit_code")
        pot_hlog_units = pot_hlog_units[
            [
                "strat_unit_no",
                "map_symbol",
                "strat_name",
                "hydro_subunit_code",
                "hydro_subunit_name",
                "unit_code",
                # "unit_name",
            ]
        ]

        h_int_df = self.db.query(
            """
            select
                int.drillhole_no as dh_no,
                int.strat_unit_no
            from dhdb.wa_hydrostrat_int_vw int
        """
        )
        actual_hlog_units = pot_hlog_units[
            pot_hlog_units.strat_unit_no.isin(h_int_df.strat_unit_no)
        ]

        self.pot_hlog_units = pot_hlog_units
        self.actual_hlog_units = actual_hlog_units

        self.aq_codes = pd.merge(
            self.pot_aqmon,
            self.aqmon_summ_use[["aquifer_code", "count_aqmon"]],
            on="aquifer_code",
            how="left",
        )
        self.aq_codes = self.aq_codes[
            [
                "strat_unit_no",
                "strat_unit",
                "strat_name",
                "hydro_subunit_code",
                "aquifer_code",
                "count_aqmon",
                "hydro_subunit_name",
                "linked_strat_unit_no",
                "linked_map_symbol",
                "linked_strat_name",
            ]
        ]
        self.hlog_codes = pd.merge(
            self.pot_hlog_units,
            self.hslog_summ_use[["unit_code", "count_hslog"]],
            on="unit_code",
            how="left",
        )
        self.hlog_codes = self.hlog_codes[
            (self.hlog_codes.hydro_subunit_code != "")
            | (self.hlog_codes.count_hslog > 0)
        ]
        self.hlog_codes = self.hlog_codes[
            [
                "strat_unit_no",
                "map_symbol",
                "strat_name",
                "unit_code",
                "count_hslog",
                "hydro_subunit_code",
                "hydro_subunit_name",
            ]
        ]


class ProductionZoneData:
    """Class to make it easier to use production zone (PZ) data from SA Geodata.
    PZ data is basically the riser, screen, slotted section, blank section, sump,
    and/or open-hole data records.

    It is complicated because of the presence of S-type records (survey events) which
    largely measure the depth of a borehole, and multiple records, when usually we
    want the most recent current construction.

    This class provides a way to automatically generate a single record which has
    the max and min depth of the open interval, ignoring the rare situation where
    there may be blanks within that open interval.

    Args:
        wells: list of drillhole numbers or a dataframe with 'dh_no'
        db (SAGeodataConnection): will create a new connection if not supplied
        index_id (str): well ID column to use as the index for pzone attribute.

    Attributes:
        pzones (pd.DataFrame): the original data obtained via db.production_zones(dh_nos)
        events (pd.DataFrame): only construction event PZ data with a completion date
        most_recent_event (pd.DataFrame): the most recent construction event PZ data
        open_pzone_intervals (pd.DataFrame): the open intervals (screen, slots, open hole) from the
            most recent construction event PZ data
        pzone (pd.DataFrame): the maximum extent of open intervals - note this dataframe
            has the index_id argument set as the index, and it is guaranteed to have only
            one record/row for each well.

    Note the attributes are all dataframes because the object can be used for one or
    more wells.

    Example usage

    .. code-block::

        >>> import dew_gwdata as gd
        >>> db = gd.sageodata()
        >>> wells = db.find_wells('YAT060 YAT115')
        >>> pz = db.ProductionZoneData(wells, index_id='obs_no')
        >>> pz.pzone.loc['YAT060']
        well_id                             YAT060
        dh_no                                58443
        unit_hyphen                     6628-11474
        unit_long                        662811474
        completion_date        1979-03-14 00:00:00
        open_depth_from_min                   15.0
        open_depth_to_max                     21.0
        open_types                              SC
        open_extent                   (15.0, 21.0)
        Name: YAT060, dtype: object

    """

    def __init__(self, wells, db=None, index_id="obs_no"):
        if db is None:
            import dew_gwdata as gd

            db = gd.sageodata()

        pzones = db.production_zones(wells)
        events = pzones[
            (pzones.event_type == "C") & (~pd.isnull(pzones.completion_date))
        ]
        most_recent_event = events.groupby("dh_no", group_keys=False).apply(
            lambda grp: grp[grp.completion_date == grp.completion_date.max()]
        )
        open_pzone_intervals = most_recent_event[
            most_recent_event.pzone_type.isin(["S", "SC", "OH"])
        ]
        pzone = (
            open_pzone_intervals.groupby(
                [
                    "well_id",
                    "obs_no",
                    "dh_no",
                    "unit_hyphen",
                    "unit_long",
                    "completion_date",
                ],
            )
            .agg(
                open_depth_from_min=("depth_from", "min"),
                open_depth_to_max=("depth_to", "max"),
                open_types=("pzone_type", lambda ptypes: " ".join(ptypes)),
            )
            .reset_index()
        )
        pzone["open_extent"] = pzone.apply(
            lambda row: (row.open_depth_from_min, row.open_depth_to_max), axis=1
        )
        self.pzones = pzones
        self.events = events
        self.most_recent_event = most_recent_event
        self.open_pzone_intervals = open_pzone_intervals
        self.pzone = pzone

        self.set_index(index_id)

    def set_index(self, id_col):
        """Change the well ID column used as the index for the attribute pzone.

        Args:
            id_col (str): either 'unit_long', 'unit_hyphen', 'obs_no', or 'well_id'

        """
        assert id_col in ("unit_long", "unit_hyphen", "obs_no", "well_id")
        self.pzone = self.pzone.set_index(id_col)


def get_dem_elev(xy_coords, crs="epsg:7844"):
    """Obtain a rapid elevation value from DEW EGIS DEMs.

    Args:
        xy_coords: an array of x, y tuples for each location
        crs: coordinate system of tuples. Longitude and latitude by default.
            SA Lambert GDA2020 is "epsg:8059". GDA2020 zones are
            "epsg:7853" and "epsg:7854" respectively.

    Returns:
        gpd.GeoDataFrame: a dataframe with columns "geometry",
        "x", "y", "elev", and "elev_source"

    See source code for the DEMS in use. Currently they are sourced
    from EGIS and are:

    - DEM_NASA_30M (i.e. the SRTM)
    - DEM_ADHILLS_10M
    - DEM_SE_10M

    The most accurate available is used

    """

    layer_bounds = {
        "r:\dfw_cbd\projects\projects_gw\state\giscache\dem_nasa_30m.tif": {
            "left": 29664.586230052802,
            "bottom": 1140353.10508565,
            "right": 1970394.58623005,
            "top": 2829983.10508565,
        },
        "r:\dfw_cbd\projects\projects_gw\state\giscache\dem_adhills_10m.tif": {
            "left": 1279784.32845606,
            "bottom": 1584673.99189635,
            "right": 1387694.32845606,
            "top": 1737933.99189635,
        },
        "r:\dfw_cbd\projects\projects_gw\state\giscache\dem_se_10m.tif": {
            "left": 1371606.553399,
            "bottom": 1311986.42128288,
            "right": 1541946.553399,
            "top": 1608656.42128288,
        },
    }

    x = [val[0] for val in xy_coords]
    y = [val[1] for val in xy_coords]
    pts_original = gpd.points_from_xy(x, y, crs=crs)
    pts = gpd.GeoSeries(pts_original.to_crs("epsg:8059")).to_frame(name="geometry")
    pts["x"] = pts.geometry.x
    pts["y"] = pts.geometry.y
    for file, bounds in layer_bounds.items():
        file = Path(file)
        pts_subset = pts[
            (pts.x >= bounds["left"])
            & (pts.x <= bounds["right"])
            & (pts.y >= bounds["bottom"])
            & (pts.y <= bounds["top"])
        ]
        with rasterio.open(file) as raster:
            elevs = raster.sample(pts_subset[["x", "y"]].values)
            pts_subset["elev"] = [
                elev[0] if elev[0] != -9999 else pd.NA for elev in elevs
            ]
            pts_subset["elev_source"] = file.stem
        pts_subset = pts_subset.dropna(subset=["elev"], how="any")
        pts.loc[pts_subset.index, ["elev", "elev_source"]] = pts_subset[
            ["elev", "elev_source"]
        ]
    return pts


def depth_to_elev(df, db=None):
    """Converts any depth columns to elevations in a new column.

    Args:
        df (pd.DataFrame): any table - it should have "latitude" and "longitude"
            columns or "dh_no" (so that the location can be looked up).
        db (optional SAGeodataConnection): only used if we need to look up
            the location via "dh_no" field.

    Returns:
        pd.DataFrame: the same dataframe as input with additional columns:

        - "elev" - from :func:`dew_gwdata.get_dem_elev`
        - "elev_source" - from :func:`dew_gwdata.get_dem_elev`
        - anything in the original dataframe with "depth" will have "_mahd"
          appended and the value in the depth column converted to "elev"
        - some special cases like "casing_at_test" is identified as a depth
        - "rswl" - any rows where "swl" is populated by "rswl" is not will be
          filled in appropriately.

    .. warning::

        This function does not look at the elevation data that is
        already in SA Geodata! It purely uses the elevation rasters used
        by :func:`dew_gwdata.get_dem_elev`. Although this is fine for most
        purposes, it may lead to some confusion.

    """
    if "latitude" in df.columns and "longitude" in df.columns:
        xy_coords = df[["longitude", "latitude"]].values
        crs = "epsg:7844"
    # elif "zone" in df.columns and "easting" in df.columns and "northing" in df.columns:
    #     # that's annoying and hard, need to break it down by different zones.
    #     xy_coords = df[["easting", "northing"]].values
    #     crs = f"epsg:75{df.zone}"
    elif "dh_no" in df.columns:
        if db is None:
            db = connect()
        details = db.drillhole_details(df.dh_no)
        df_for_coords = pd.merge(df, details, on="dh_no", how="left")
        xy_coords = df_for_coords[["longitude", "latitude"]].values
        crs = "epsg:7844"

    elev_df = get_dem_elev(xy_coords, crs)
    elev_df.index = df.index
    df_result = pd.merge(
        df,
        elev_df[["elev", "elev_source"]],
        left_index=True,
        right_index=True,
        how="left",
    )
    for col in df_result.columns:
        new_col = None
        if "depth" in col or col in ("casing_at_test",):
            new_col = col + "_mahd"
        if new_col and "greater" in col:
            new_col = None
        if new_col:
            df_result[new_col] = df_result.elev - df_result[col]
    if "rswl" in df_result.columns and "swl" in df_result.columns:
        df_result.loc[pd.isnull(df_result.rswl), "rswl"] = (
            df_result.elev - df_result.swl
        )
    return df_result

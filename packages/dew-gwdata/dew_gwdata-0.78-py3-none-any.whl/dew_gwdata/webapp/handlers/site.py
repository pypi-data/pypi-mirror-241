from pathlib import Path
from typing import Annotated

import pandas as pd
from geojson import Feature, Point
from fastapi import APIRouter, Request, Query, status, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, HTMLResponse
from starlette.datastructures import URL

from sageodata_db import connect as connect_to_sageodata
from sageodata_db import load_predefined_query
from sageodata_db.utils import parse_query_metadata

import dew_gwdata as gd
from dew_gwdata.sageodata_datamart import get_sageodata_datamart_connection

from dew_gwdata.webapp import utils as webapp_utils
from dew_gwdata.webapp.models import queries


router = APIRouter(prefix="/app", include_in_schema=False)

templates_path = Path(__file__).parent.parent / "templates"

templates = Jinja2Templates(directory=templates_path)


@router.get("/well_find")
def well_find(
    request: Request,
    query: str,
    env: str = "PROD",
    unit_no: bool = False,
    obs_no: bool = False,
    dh_no: bool = False,
    singular_search_only: bool = False,
    redirect_to: str = "well_summary",
):
    db = connect_to_sageodata(service_name=env)
    types = []
    if unit_no:
        types.append("unit_no")
    if obs_no:
        types.append("obs_no")
    if dh_no:
        types.append("dh_no")
    if singular_search_only:
        # Try and search dh_no only if there is no result
        wells = db.find_wells(query, types=[t for t in types if not t == "dh_no"]).df()
        if len(wells) == 0:
            wells = db.find_wells(query, types=types).df()
        if len(wells) > 0 and len(wells) > 1:
            wells = wells.iloc[:1]
    else:
        wells = db.find_wells(query, types=types).df()
    if len(wells) == 0:
        raise Exception("No wells found")
    elif len(wells) == 1:
        return RedirectResponse(
            f"/app/{redirect_to}?dh_no={wells.iloc[0].dh_no:.0f}&redirect_to={redirect_to}&env={env}"
        )
    else:
        return RedirectResponse(
            f"/app/wells_find?query={query}&unit_no={unit_no}&obs_no={obs_no}&dh_no={dh_no}&redirect_to={redirect_to}&env={env}"
        )


@router.get("/wells_find")
def wells_find(
    request: Request,
    query: str,
    env: str = "PROD",
    unit_no: bool = False,
    obs_no: bool = False,
    dh_no: bool = False,
    redirect_to: str = "wells_summary",
):
    db = connect_to_sageodata(service_name=env)
    types = []
    if unit_no:
        types.append("unit_no")
    if obs_no:
        types.append("obs_no")
    if dh_no:
        types.append("dh_no")
    wells = db.find_wells(query, types=types).df()
    if len(wells) == 0:
        raise Exception("No wells found")
    elif len(wells) == 1:
        return RedirectResponse(
            f"/app/{redirect_to}?dh_no={wells.iloc[0].dh_no:.0f}&env={env}"
        )
    else:
        url_str = webapp_utils.dhnos_to_urlstr(wells.dh_no)
        return RedirectResponse(f"/app/{redirect_to}?url_str={url_str}&env={env}")


@router.get("/wells_search_name")
def wells_search_name(
    request: Request,
    query: str,
    env: str = "PROD",
):
    db = connect_to_sageodata(service_name=env)
    wells = db.drillhole_details_by_name_search(query)
    if len(wells) == 0:
        raise Exception("No wells found")
    elif len(wells) == 1:
        return RedirectResponse(
            f"/app/well_summary?dh_no={wells.iloc[0].dh_no:.0f}&env={env}"
        )
    else:
        url_str = webapp_utils.dhnos_to_urlstr(wells.dh_no)
        return RedirectResponse(f"/app/wells_summary?url_str={url_str}&env={env}")


@router.get("/wells_search_around")
def wells_search_around(
    request: Request,
    query: str,
    env: str = "PROD",
    unit_no: bool = False,
    obs_no: bool = False,
    dh_no: bool = False,
    singular_search_only: bool = True,
    distance: float = 1,
    redirect_to: str = "wells_summary",
):
    db = connect_to_sageodata(service_name=env)
    types = []
    if unit_no:
        types.append("unit_no")
    if obs_no:
        types.append("obs_no")
    if dh_no:
        types.append("dh_no")

    query_well = None
    if singular_search_only:
        # Try and search dh_no only if there is no result
        wells = db.find_wells(query, types=[t for t in types if not t == "dh_no"]).df()
        if len(wells) == 0:
            wells = db.find_wells(query, types=types).df()
        if len(wells) > 0:
            query_well = wells.iloc[0]
    else:
        wells = db.find_wells(query, types=types).df()
        if len(wells) > 0:
            query_well = wells.iloc[0]

    if query_well is None:
        raise Exception("No well found with query.")

    wells = db.drillhole_within_distance(query_well.dh_no, distance)
    url_str = webapp_utils.dhnos_to_urlstr(wells.dh_no)
    return RedirectResponse(f"/app/{redirect_to}?url_str={url_str}&env={env}")


@router.get("/wells_summary")
def wells_summary(
    request: Request,
    query: Annotated[queries.Wells, Depends()],
):
    db = connect_to_sageodata(service_name=query.env)
    wells, name, name_safe, query_params = query.find_wells()
    dh_nos = wells.dh_no
    title = name
    if len(dh_nos):
        df = db.wells_summary(dh_nos)
    else:
        cols, _, _ = parse_query_metadata(load_predefined_query("wells_summary"))
        df = pd.DataFrame(columns=cols)

    df = df.sort_values(
        [query.sort], ascending=True if query.order.startswith("asc") else False
    )

    df_for_table = df[
        [
            "dh_no",
            "unit_hyphen",
            "obs_no",
            "dh_name",
            "aquifer",
            "latest_status",
            "latest_swl",
            "latest_tds",
            "purpose",
            "owner",
            "orig_drilled_depth",
            "orig_drilled_date",
            "latest_cased_to",
            "comments",
            "pwa",
            "pwra",
        ]
    ]
    title_series = df_for_table.apply(
        lambda well: (
            f'<nobr><a href="/app/well_summary?dh_no={well.dh_no}&env={query.env}">'
            f'{webapp_utils.make_dh_title(well, elements=("unit_no", "obs_no"))}</a></nobr>'
        ),
        axis=1,
    )
    df_for_table.insert(0, "title", title_series)
    df_for_table = df_for_table.drop(["unit_hyphen", "obs_no"], axis=1)
    table = webapp_utils.frame_to_html(df_for_table)

    egis_layer_definition_query = (
        "DHNO IN (" + ",".join([str(dh_no) for dh_no in df.dh_no]) + ")"
    )

    return templates.TemplateResponse(
        "wells_summary.html",
        {
            "request": request,
            "env": query.env,
            "title": title,
            "query": query,
            "redirect_to": "wells_summary",
            "wells_title": title,
            "wells_query_params": query_params,
            "wells": df,
            "wells_table": table,
            "egis_layer_definition_query": egis_layer_definition_query,
        },
    )


@router.get("/wells_data_available")
def wells_data_available(
    request: Request,
    query: Annotated[queries.Wells, Depends()],
):
    db = connect_to_sageodata(service_name=query.env)
    wells, name, name_safe, query_params = query.find_wells()
    dh_nos = wells.dh_no
    title = name
    if len(dh_nos):
        summ = db.wells_summary(dh_nos)
    else:
        cols, _, _ = parse_query_metadata(load_predefined_query("wells_summary"))
        summ = pd.DataFrame(columns=cols)

    if len(dh_nos):
        data = db.data_available(dh_nos)
    else:
        cols, _, _ = parse_query_metadata(load_predefined_query("data_available"))
        data = pd.DataFrame(columns=cols)

    summ = summ.sort_values(
        [query.sort], ascending=True if query.order.startswith("asc") else False
    )

    col_to_endpoint_map = {
        "drill_or_lith_logs": "well_drillhole_logs",
        "strat_or_hydro_logs": "well_drillhole_logs",
        "water_levels": "well_manual_water_level",
        "elev_surveys": "well_summary",
        # "aquarius_flag": "well_summary"
        "salinities": "well_salinity",
        "water_cuts": "well_construction",
        # "geophys_logs": "",
        "dh_docimg_flag": "well_drillhole_document_images",
        # "photo_flag": "",
    }
    for col, endpoint in col_to_endpoint_map.items():
        data[col] = data.apply(
            lambda row: (
                f'<a href="/app/{endpoint}?dh_no={row.dh_no}&env={query.env}">{row[col]}</a>'
                if row[col] > 0
                else 0
            ),
            axis=1,
        )

    summ_keep = [
        "dh_no",
        "unit_hyphen",
        "obs_no",
        "dh_name",
        "aquifer",
        "orig_drilled_depth",
        "orig_drilled_date",
    ]
    summ["orig_drilled_depth"] = summ.orig_drilled_depth.apply(
        lambda v: f"{v:.02f}" if not pd.isnull(v) else ""
    )
    df_for_table = pd.merge(summ[summ_keep], data, on="dh_no")

    title_series = df_for_table.apply(
        lambda well: (
            f'<nobr><a href="/app/well_summary?dh_no={well.dh_no}&env={query.env}">'
            f'{webapp_utils.make_dh_title(well, elements=("unit_no", "obs_no"))}</a></nobr>'
        ),
        axis=1,
    )
    df_for_table.insert(0, "title", title_series)
    df_for_table = df_for_table.drop(["unit_hyphen", "obs_no"], axis=1)

    def series_styler(series):
        def value_function(value):
            if value == 0:
                return "border: 1px solid grey;"
            else:
                return "background-color: lightgreen; border: 1px solid grey;"

        return series.apply(value_function)

    apply_colours_to = [
        c for c in df_for_table.columns if not c in summ.columns and not c == "title"
    ]

    table = webapp_utils.frame_to_html(
        df_for_table,
        apply=series_styler,
        apply_kws=dict(
            axis=1,
            subset=apply_colours_to,
        ),
    )

    egis_layer_definition_query = (
        "DHNO IN (" + ",".join([str(dh_no) for dh_no in summ.dh_no]) + ")"
    )

    return templates.TemplateResponse(
        "wells_data_available.html",
        {
            "request": request,
            "env": query.env,
            "title": title,
            "query": query,
            "redirect_to": "wells_data_available",
            "wells_title": title,
            "wells_query_params": query_params,
            "wells": summ,
            "wells_table": table,
            "egis_layer_definition_query": egis_layer_definition_query,
        },
    )


@router.get("/wells_geojson_summary")
def wells_map(
    request: Request,
    query: Annotated[queries.Wells, Depends()],
):
    db = connect_to_sageodata(service_name=query.env)
    wells, name, name_safe, query_params = query.find_wells()
    dh_nos = wells.dh_no
    title = name
    if len(dh_nos):
        df = db.wells_summary(dh_nos)
    else:
        cols, _, _ = parse_query_metadata(load_predefined_query("wells_summary"))
        df = pd.DataFrame(columns=cols)

    df = df.sort_values([query.sort])

    features = []
    for idx, row in df.iterrows():
        feature = Feature(geometry=Point(()))

    return templates.TemplateResponse(
        "wells_map.html",
        {
            "request": request,
            "env": query.env,
            "redirect_to": "wells_map",
            "title": title,
            "wells_title": title,
            "wells_query_params": query_params,
            "wells": df,
        },
    )


def get_well_metadata(df, dh_no, env="PROD"):
    cols = ["dh_no", "unit_hyphen", "obs_no", "dh_name"]

    def check_columns():
        for col in cols:
            if not col in df.columns:
                return False
        return True

    if len(df) and check_columns():
        result = df[cols].iloc[0]
    else:
        db = connect_to_sageodata(service_name=env)
        result = db.wells_summary([dh_no])[cols].iloc[0]
    result["title"] = webapp_utils.make_dh_title(result)
    return result


@router.get("/well_summary")
def well_summary(request: Request, dh_no: int, env: str = "PROD") -> str:
    db = connect_to_sageodata(service_name=env)
    well = db.wells_summary([dh_no]).iloc[0]
    groups = db.drillhole_groups([dh_no]).pipe(gd.cleanup_columns)
    elev = db.elevation_surveys([dh_no]).pipe(gd.cleanup_columns)
    groups["sort_key"] = groups.group_type.map(
        {"OMN": 0, "PR": 1, "OMH": 2, "GDU": 3, "MDU": 4}
    )
    groups = groups.sort_values(["sort_key", "group_modified_date"])
    groups = groups.drop(
        [
            "well_id",
            "sort_key",
            "dh_created_by",
            "dh_creation_date",
            "dh_modified_by",
            "dh_modified_date",
            "group_created_by",
            "group_creation_date",
            "group_modified_by",
            "group_modified_date",
        ],
        axis=1,
    )
    elev_cols = [
        "elev_date",
        "applied_date",
        "ground_elev",
        "ref_elev",
        "survey_meth",
        "ref_point_type",
        "comments",
    ]
    elev = elev[elev_cols]

    well["title"] = webapp_utils.make_dh_title(well)
    well_table = webapp_utils.series_to_html(well)
    groups_table = webapp_utils.frame_to_html(groups)
    elev_table = webapp_utils.frame_to_html(elev)

    return templates.TemplateResponse(
        "well_summary.html",
        {
            "request": request,
            "env": env,
            "title": well.title,
            "redirect_to": "well_summary",
            "wells_title": "1 well",
            "wells_query_params": "url_str=" + webapp_utils.dhnos_to_urlstr([dh_no]),
            "well": well,
            "well_table": well_table,
            "groups_table": groups_table,
            "elev_table": elev_table,
        },
    )


@router.get("/well_manual_water_level")
def well_manual_water_level(request: Request, dh_no: int, env: str = "PROD") -> str:
    db = connect_to_sageodata(service_name=env)
    df = db.water_levels([dh_no]).sort_values("obs_date", ascending=False)
    well = get_well_metadata(df, dh_no)

    table = webapp_utils.frame_to_html(gd.cleanup_columns(df, keep_cols=[]))
    return templates.TemplateResponse(
        "well_manual_water_level.html",
        {
            "request": request,
            "env": env,
            "title": well.title,
            "redirect_to": "well_manual_water_level",
            "wells_title": "1 well",
            "wells_query_params": "url_str=" + webapp_utils.dhnos_to_urlstr([dh_no]),
            "well": well,
            "df": df,
            "table": table,
        },
    )


@router.get("/well_salinity")
def well_salinity(request: Request, dh_no: int, env: str = "PROD") -> str:
    db = connect_to_sageodata(service_name=env)
    df = db.salinities([dh_no]).sort_values("collected_date", ascending=False)
    well = get_well_metadata(df, dh_no)
    table = webapp_utils.frame_to_html(
        gd.cleanup_columns(df, keep_cols=[]).drop(
            ["amg_easting", "amg_northing"], axis=1
        )
    )
    return templates.TemplateResponse(
        "well_salinity.html",
        {
            "request": request,
            "env": env,
            "title": well.title,
            "redirect_to": "well_salinity",
            "wells_title": "1 well",
            "wells_query_params": "url_str=" + webapp_utils.dhnos_to_urlstr([dh_no]),
            "well": well,
            "df": df,
            "table": table,
        },
    )


@router.get("/well_drillhole_logs")
def well_drillhole_logs(request: Request, dh_no: int, env: str = "PROD") -> str:
    db = connect_to_sageodata(service_name=env)

    logs = db.drillhole_logs([dh_no]).sort_values("log_date", ascending=True)
    log_types = logs.log_type.unique()

    drill = db.drillers_logs([dh_no]).sort_values(["depth_from", "depth_to"])
    lith = db.lith_logs([dh_no]).sort_values(["depth_from", "depth_to"])
    strat = db.strat_logs([dh_no]).sort_values(["depth_from", "depth_to"])
    hstrat = db.hydrostrat_logs([dh_no])  # .sort_values(["depth_from", "depth_to"])

    well = get_well_metadata(logs, dh_no)

    logs_table = webapp_utils.frame_to_html(gd.cleanup_columns(logs, keep_cols=[]))
    drill_table = webapp_utils.frame_to_html(gd.cleanup_columns(drill, keep_cols=[]))
    lith_table = webapp_utils.frame_to_html(gd.cleanup_columns(lith, keep_cols=[]))
    strat_table = webapp_utils.frame_to_html(gd.cleanup_columns(strat, keep_cols=[]))
    hstrat_table = webapp_utils.frame_to_html(gd.cleanup_columns(hstrat, keep_cols=[]))

    return templates.TemplateResponse(
        "well_drillhole_logs.html",
        {
            "request": request,
            "env": env,
            "title": well.title,
            "redirect_to": "well_drillhole_logs",
            "wells_title": "1 well",
            "wells_query_params": "url_str=" + webapp_utils.dhnos_to_urlstr([dh_no]),
            "well": well,
            "logs": logs,
            "log_types": log_types,
            "drill": drill,
            "lith": lith,
            "strat": strat,
            "hstrat": hstrat,
            "logs_table": logs_table,
            "drill_table": drill_table,
            "lith_table": lith_table,
            "strat_table": strat_table,
            "hstrat_table": hstrat_table,
        },
    )


@router.get("/well_construction")
def well_construction(request: Request, dh_no: int, env: str = "PROD") -> str:
    db = connect_to_sageodata(service_name=env)

    cevents_df = db.construction_events([dh_no]).sort_values(
        "completion_date", ascending=False
    )

    well = get_well_metadata(cevents_df, dh_no)

    bool_flags = [
        "screened",
        "pcemented",
        "developed",
        "abandoned",
        "backfilled",
        "dry",
        "enlarged",
        "flowing",
        "replacement",
        "rehabilitated",
        "core_flag",
    ]
    cevents_df["activity"] = cevents_df.apply(
        lambda row: " + ".join([col for col in bool_flags if row[col] == "Y"]), axis=1
    )
    summary_cols = [
        "completion_date",
        "event_type",
        "activity",
        "wcr_id",
        "permit_no",
        "comments",
        "total_depth",
        "final_depth",
        "current_depth",
        "final_swl",
        "final_yield",
        "drill_method",
        "drill_to",
        "casing_material",
        "casing_min_diam",
        "casing_to",
        "pzone_type",
        "pzone_material",
        "pzone_diam",
        "pzone_from",
        "pzone_to",
    ]
    summary_table = webapp_utils.frame_to_html(
        gd.cleanup_columns(cevents_df[summary_cols], keep_cols=[])
    )

    # drilling, casing, wcuts, pzones, other_items
    drilling = db.drilled_intervals([dh_no]).sort_values(["depth_from", "depth_to"])
    casing = db.casing_strings([dh_no]).sort_values(["depth_from", "depth_to"])
    seals = db.casing_seals([dh_no]).sort_values("seal_depth")
    wcuts = db.water_cuts([dh_no]).sort_values(["depth_from", "depth_to"])
    pzones = db.production_zones([dh_no]).sort_values(["pzone_from", "pzone_to"])
    other_items = db.other_construction_items([dh_no]).sort_values(
        ["depth_from", "depth_to"]
    )

    cevents = []
    sevents = []

    kws = dict(
        keep_cols=[],
        drop=("construction_aquifer", "completion_no", "completion_date", "event_type"),
    )

    for completion_no, cevent_summ in cevents_df.groupby("completion_no"):
        summary = gd.cleanup_columns(cevent_summ, keep_cols=[]).iloc[0]
        if summary.event_type == "C":
            title = f"Construction event "
        elif summary.event_type == "S":
            title = f"Survey event "
        title += webapp_utils.format_datetime(summary.completion_date)

        summary = summary.drop([
            "latest", "max_case", "orig_case", "lod_case", "from_flag",
        ])

        summary_1 = summary[[
            "completion_no", "event_type", "activity",
            "commenced_date", "completion_date", "wcr_id", "permit_no_full",
            "plant_operator", "construction_aquifer", "start_depth", "total_depth",
            "final_depth", "created_by",
            "creation_date", "modified_by", "modified_date",
        ]]
        
        summary_2 = summary[[
            'drill_method', "drill_from", "drill_to", "drill_diam",
            "casing_material", "casing_from", "casing_to", "casing_diam",
            "casing_min_diam", "pzone_type", "pzone_material", "pzone_from",
            "pzone_to", "pzone_diam", "pcement_from", "pcement_to",
        ]]

        cevent = {
            "data_types": [],
            "title": title,
            "summary": summary,
            "summary_1": summary_1,
            "summary_2": summary_2,
            "comments": summary.comments,
            "summary_table": webapp_utils.series_to_html(
                summary.drop(index=["comments"])
            ),
            "summary_1_table": webapp_utils.series_to_html(summary_1),
            "summary_2_table": webapp_utils.series_to_html(summary_2),
        }

        cevent_drilling = drilling[drilling.completion_no == completion_no]
        if len(cevent_drilling) > 0:
            cevent["drilling"] = webapp_utils.frame_to_html(
                gd.cleanup_columns(cevent_drilling, **kws).T
            )
            cevent["data_types"].append("drilling")

        cevent_casing = casing[casing.completion_no == completion_no]
        if len(cevent_casing) > 0:
            cevent["casing"] = webapp_utils.frame_to_html(
                gd.cleanup_columns(cevent_casing, **kws).T
            )
            cevent["data_types"].append("casing")

        cevent_seals = seals[seals.completion_no == completion_no]
        if len(cevent_seals) > 0:
            cevent["seals"] = webapp_utils.frame_to_html(
                gd.cleanup_columns(cevent_seals, **kws).T
            )
            cevent["data_types"].append("seals")

        cevent_wcuts = wcuts[wcuts.completion_no == completion_no]
        if len(cevent_wcuts) > 0:
            cevent["wcuts"] = webapp_utils.frame_to_html(
                gd.cleanup_columns(cevent_wcuts, **kws)
            )
            cevent["data_types"].append("wcuts")

        cevent_pzones = pzones[pzones.completion_no == completion_no]
        if len(cevent_pzones) > 0:
            cevent["pzones"] = webapp_utils.frame_to_html(
                gd.cleanup_columns(cevent_pzones, **kws).T
            )
            cevent["data_types"].append("pzones")

        cevent_other_items = other_items[other_items.completion_no == completion_no]
        if len(cevent_other_items) > 0:
            cevent["other_items"] = webapp_utils.frame_to_html(
                gd.cleanup_columns(cevent_other_items, **kws).T
            )
            cevent["data_types"].append("other_items")

        if summary.event_type == "C":
            cevents.append(cevent)
        elif summary.event_type == "S":
            sevents.append(cevent)

    cevents = sorted(cevents, key=lambda x: x["summary"].completion_date)
    sevents = sorted(sevents, key=lambda x: x["summary"].completion_date)

    return templates.TemplateResponse(
        "well_construction.html",
        {
            "request": request,
            "env": env,
            "title": well.title,
            "redirect_to": "well_construction",
            "wells_title": "1 well",
            "wells_query_params": "url_str=" + webapp_utils.dhnos_to_urlstr([dh_no]),
            "well": well,
            "summary_table": summary_table,
            "events": [cevents, sevents],
        },
    )


@router.get("/well_drillhole_document_images")
def well_drillhole_document_images(
    request: Request,
    dh_no: int,
    env: str = "PROD",
    width: int = 950,
    height: int = -1,
    inline: bool = False,
    new_tab: bool = False,
) -> str:
    db = connect_to_sageodata(service_name=env)
    df = db.drillhole_document_image_list([dh_no])
    well = get_well_metadata(df, dh_no)

    images = [im for idx, im in df.iterrows()]

    return templates.TemplateResponse(
        "well_drillhole_document_images.html",
        {
            "request": request,
            "env": env,
            "title": well.title,
            "redirect_to": "well_drillhole_document_images",
            "wells_title": "1 well",
            "wells_query_params": "url_str=" + webapp_utils.dhnos_to_urlstr([dh_no]),
            "well": well,
            "df": df,
            "images": images,
            "width": width,
            "height": height,
            "inline": inline,
            "new_tab": new_tab,
            "target": "_blank" if new_tab else "",
        },
    )


@router.get("/")
def home_handler(request: Request) -> str:
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "title": "Home",
            "redirect_to": "well_summary",
            "env": "prod",
        },
    )


@router.get("/schema")
def schema(
    request: Request,
    env: str = "PROD",
    filter_by: str = "",
) -> str:
    if "test" in env.lower() or "qa" in env.lower():
        user = "dhdb"
        password = "android22"
    else:
        user = "gwquery"
        password = "gwquery"

    filter_by = filter_by.upper()

    db = connect_to_sageodata(service_name=env, user=user, password=password)

    tables_where = ""
    views_where = ""
    if filter_by:
        tables_where = f"and table_name like '%{filter_by}%'"
        views_where = f"and view_name like '%{filter_by}%'"

    tables = db.query(
        f"select owner, table_name from all_tables where owner in ('DHDB', 'DHDBVIEW') and not table_name like '%$%' {tables_where}"
    )
    views = db.query(
        f"select owner, view_name, text_length as view_definition_length from all_views where owner in ('DHDB', 'DHDBVIEW') and not view_name like '%$%' {views_where}"
    )

    title = "Tables and views"
    if filter_by:
        title += f" containing '{filter_by}'"

    tables["table_name"] = tables.apply(
        lambda r: f'<a href="/app/schema_data?owner={r.owner}&table_name={r.table_name}&env={env}">{r.table_name}</a>',
        axis=1,
    )
    views["view_definition_length"] = views.apply(
        lambda r: f'<a href="/app/schema_view?owner={r.owner}&view_name={r.view_name}&env={env}">{r.view_definition_length}</a>',
        axis=1,
    )
    views["view_name"] = views.apply(
        lambda r: f'<a href="/app/schema_data?owner={r.owner}&table_name={r.view_name}&env={env}">{r.view_name}</a>',
        axis=1,
    )

    tables_html = webapp_utils.frame_to_html(tables)
    views_html = webapp_utils.frame_to_html(views)

    return templates.TemplateResponse(
        "app_schema.html",
        {
            "request": request,
            "redirect_to": "well_summary",
            "env": env,
            "title": title,
            "filter_by": filter_by,
            "tables_html": tables_html,
            "views_html": views_html,
        },
    )


@router.get("/schema_data")
def schema_data(
    request: Request,
    owner: str,
    table_name: str,
    limit: int = 200,
    transpose: bool = False,
    suffix: str = "",
    env: str = "PROD",
    select: str = "*",
    where: str = "",
) -> str:
    if "test" in env.lower() or "qa" in env.lower():
        user = "dhdb"
        password = "android22"
    else:
        user = "gwquery"
        password = "gwquery"

    db = connect_to_sageodata(service_name=env, user=user, password=password)

    if where:
        where = "and " + where
    else:
        where = ""

    data = db.query(
        f"select {select} from (select * from {owner}.{table_name} {suffix}) where rownum <= {limit} " + where
    )

    for col in [c for c in data.columns if c.upper().endswith("_CONTENTS")]:
        data[col] = "🗎"

    view = db.query(
        f"select * from all_views where owner = '{owner}' and view_name = '{table_name}'"
    )

    if len(view):
        is_view = True
    else:
        is_view = False

    title = f"{owner}.{table_name}"

    if transpose:
        transpose_last = True
        remove_col_underscores = False
    else:
        transpose_last = False
        remove_col_underscores = True

    data_html = webapp_utils.frame_to_html(
        data,
        transpose_last=transpose_last,
        remove_col_underscores=remove_col_underscores,
    )

    return templates.TemplateResponse(
        "app_schema_data.html",
        {
            "request": request,
            "redirect_to": "well_summary",
            "env": env,
            "title": title,
            "owner": owner,
            "table_name": table_name,
            "limit": limit,
            "data_html": data_html,
            "transpose": transpose,
            "is_view": is_view,
        },
    )


@router.get("/schema_view")
def schema_view(
    request: Request,
    owner: str,
    view_name: str,
    env: str = "PROD",
) -> str:
    if "test" in env.lower() or "qa" in env.lower():
        user = "dhdb"
        password = "android22"
    else:
        user = "gwquery"
        password = "gwquery"

    db = connect_to_sageodata(service_name=env, user=user, password=password)

    data = db.query(
        f"select text from all_views where owner = '{owner}' and view_name = '{view_name}'"
    ).iloc[0]

    title = f"{owner}.{view_name}"

    return templates.TemplateResponse(
        "app_schema_view.html",
        {
            "request": request,
            "redirect_to": "well_summary",
            "env": env,
            "title": title,
            "owner": owner,
            "view_name": view_name,
            "text": data.text,
        },
    )

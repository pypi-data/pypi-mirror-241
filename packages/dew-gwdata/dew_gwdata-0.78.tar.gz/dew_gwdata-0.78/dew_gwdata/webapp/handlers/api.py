import base64
import io
from typing import Annotated

import pandas as pd
from fastapi import APIRouter, Request, Query, Depends
from fastapi.responses import StreamingResponse, Response
import cx_Oracle
from PIL import Image

import dew_gwdata as gd
from dew_gwdata.sageodata_database import connect as connect_to_sageodata
from dew_gwdata.sageodata_datamart import get_sageodata_datamart_connection

from dew_gwdata.webapp import utils as webapp_utils
from dew_gwdata.webapp.models import queries


router = APIRouter(prefix="/api")


def apply_format(data, format="json", response_name="export"):
    data = data.fillna("")
    if format == "json":
        if isinstance(data, pd.Series):
            return data.to_dict()
        if isinstance(data, pd.DataFrame):
            return data.to_dict(orient="records")
    elif format == "csv":
        stream = io.StringIO()
        if isinstance(data, pd.Series):
            data.to_frame().to_csv(stream)
        if isinstance(data, pd.DataFrame):
            data.to_csv(stream)
    response = StreamingResponse(iter([stream.getvalue()]), media_type="text/csv")
    response.headers[
        "Content-Disposition"
    ] = f"attachment; filename={response_name}.csv"
    return response


@router.get("/utils_find_wells", tags=["utils"])
def find_wells(
    request: Request,
    query: str,
    env: str = "PROD",
    unit_no: bool = False,
    obs_no: bool = False,
    dh_no: bool = False,
    singular_search_only: bool = False,
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
        df = db.find_wells(query, types=[t for t in types if not t == "dh_no"]).df()
        if len(df) == 0:
            df = db.find_wells(query, types=types).df()
    else:
        df = db.find_wells(query, types=types).df()
    dh_nos = [int(dh_no) for dh_no in df.dh_no]
    url_str = webapp_utils.dhnos_to_urlstr(dh_nos)
    return {"dh_nos": dh_nos, "url_str": url_str}


@router.get("/utils_dhnos_to_urlstr", tags=["utils"])
def dhnos_to_urlstr(
    request: Request,
    dh_no: Annotated[list[int], Query()],
):
    return {"dh_nos": dh_no, "url_str": webapp_utils.dhnos_to_urlstr(dh_no)}


@router.get("/wells_summary", tags=["data"])
def wells_summary(query: queries.Wells = Depends(), format: str = "json"):
    db = connect_to_sageodata(service_name=query.env)
    dh_nos, name, name_safe, query_params = query.find_wells()
    well = db.wells_summary(dh_nos)
    return apply_format(
        well, format=format, response_name=f"wells_summary__{name_safe}"
    )


@router.get("/wells_manual_water_level", tags=["data"])
def manual_water_level(query: queries.Wells = Depends(), format: str = "json"):
    db = connect_to_sageodata(service_name=query.env)
    dh_nos, name, name_safe, query_params = query.find_wells()
    df = db.water_levels(dh_nos).sort_values("obs_date", ascending=False)
    return apply_format(
        df, format=format, response_name=f"manual_water_level__{name_safe}"
    )


@router.get("/wells_salinity", tags=["data"])
def salinity(query: queries.Wells = Depends(), format: str = "json"):
    db = connect_to_sageodata(service_name=query.env)
    dh_nos, name, name_safe, query_params = query.find_wells()
    df = db.salinities(dh_nos).sort_values("collected_date", ascending=False)
    return apply_format(df, format=format, response_name=f"wells_salinity__{name_safe}")


@router.get("/wells_drillhole_logs", tags=["data"])
def drillhole_logs(query: queries.Wells = Depends(), format: str = "json"):
    db = connect_to_sageodata(service_name=query.env)
    dh_nos, name, name_safe, query_params = query.find_wells()
    logs = db.drillhole_logs(dh_nos).sort_values("log_date", ascending=True)
    return apply_format(
        logs, format=format, response_name=f"wells_drillhole_logs__{name_safe}"
    )


@router.get("/wells_drillers_logs", tags=["data"])
def drillers_logs(query: queries.Wells = Depends(), format: str = "json"):
    db = connect_to_sageodata(service_name=query.env)
    dh_nos, name, name_safe, query_params = query.find_wells()
    drill = db.drillers_logs(dh_nos)
    return apply_format(
        drill, format=format, response_name=f"wells_drillers_logs__{name_safe}"
    )


@router.get("/wells_lith_logs", tags=["data"])
def lith_logs(query: queries.Wells = Depends(), format: str = "json"):
    db = connect_to_sageodata(service_name=query.env)
    dh_nos, name, name_safe, query_params = query.find_wells()
    lith = db.lith_logs(dh_nos)
    return apply_format(
        lith, format=format, response_name=f"wells_lith_logs__{name_safe}"
    )


@router.get("/wells_strat_logs", tags=["data"])
def strat_logs(query: queries.Wells = Depends(), format: str = "json"):
    db = connect_to_sageodata(service_name=query.env)
    dh_nos, name, name_safe, query_params = query.find_wells()
    strat = db.strat_logs(dh_nos)
    return apply_format(
        strat, format=format, response_name=f"wells_strat_logs__{name_safe}"
    )


@router.get("/wells_hydrostrat_logs", tags=["data"])
def hydrostrat_logs(query: queries.Wells = Depends(), format: str = "json"):
    db = connect_to_sageodata(service_name=query.env)
    dh_nos, name, name_safe, query_params = query.find_wells()
    df = db.hydrostrat_logs(dh_nos)
    return apply_format(
        df, format=format, response_name=f"wells_hydrostrat_logs__{name_safe}"
    )


@router.get("/wells_construction_events", tags=["data"])
def construction_events(query: queries.Wells = Depends(), format: str = "json"):
    db = connect_to_sageodata(service_name=query.env)
    dh_nos, name, name_safe, query_params = query.find_wells()
    df = db.construction_events(dh_nos)
    return apply_format(
        df, format=format, response_name=f"wells_construction_events__{name_safe}"
    )


@router.get("/wells_drilled_intervals", tags=["data"])
def drilled_intervals(query: queries.Wells = Depends(), format: str = "json"):
    db = connect_to_sageodata(service_name=query.env)
    dh_nos, name, name_safe, query_params = query.find_wells()
    df = db.drilled_intervals(dh_nos)
    return apply_format(
        df, format=format, response_name=f"wells_drilled_intervals__{name_safe}"
    )


@router.get("/wells_casing_strings", tags=["data"])
def casing_strings(query: queries.Wells = Depends(), format: str = "json"):
    db = connect_to_sageodata(service_name=query.env)
    dh_nos, name, name_safe, query_params = query.find_wells()
    df = db.casing_strings(dh_nos)
    return apply_format(
        df, format=format, response_name=f"wells_casing_strings__{name_safe}"
    )


@router.get("/wells_casing_seals", tags=["data"])
def casing_seals(query: queries.Wells = Depends(), format: str = "json"):
    db = connect_to_sageodata(service_name=query.env)
    dh_nos, name, name_safe, query_params = query.find_wells()
    df = db.casing_seals(dh_nos)
    return apply_format(
        df, format=format, response_name=f"wells_casing_seals{name_safe}"
    )


@router.get("/wells_production_zones", tags=["data"])
def production_zones(query: queries.Wells = Depends(), format: str = "json"):
    db = connect_to_sageodata(service_name=query.env)
    dh_nos, name, name_safe, query_params = query.find_wells()
    df = db.production_zones(dh_nos)
    return apply_format(
        df, format=format, response_name=f"wells_production_zones__{name_safe}"
    )


@router.get("/wells_other_construction_items", tags=["data"])
def other_construction_items(query: queries.Wells = Depends(), format: str = "json"):
    db = connect_to_sageodata(service_name=query.env)
    dh_nos, name, name_safe, query_params = query.find_wells()
    df = db.other_construction_items(dh_nos)
    return apply_format(
        df,
        format=format,
        response_name=f"wells_other_construction_items__{name_safe}",
    )


@router.get("/wells_water_cuts", tags=["data"])
def water_cuts(query: queries.Wells = Depends(), format: str = "json"):
    db = connect_to_sageodata(service_name=query.env)
    dh_nos, name, name_safe, query_params = query.find_wells()
    df = db.water_cuts(dh_nos)
    return apply_format(
        df, format=format, response_name=f"wells_water_cuts__{name_safe}"
    )


@router.get("/wells_permits_by_completed_drillholes_only", tags=["data"])
def permits_by_completed_drillholes_only(
    query: queries.Wells = Depends(), format: str = "json"
):
    db = connect_to_sageodata(service_name=query.env)
    dh_nos, name, name_safe, query_params = query.find_wells()
    df = db.permits_by_completed_drillholes_only(dh_nos)
    return apply_format(
        df,
        format=format,
        response_name=f"wells_permits_by_completed_drillholes_only__{name_safe}",
    )


@router.get("/wells_permit_conditions_and_notes", tags=["data"])
def permit_conditions_and_notes(query: queries.Wells = Depends(), format: str = "json"):
    db = connect_to_sageodata(service_name=query.env)
    dh_nos, name, name_safe, query_params = query.find_wells()
    df = db.permit_conditions_and_notes(dh_nos)
    return apply_format(
        df,
        format=format,
        response_name=f"wells_permit_conditions_and_notes__{name_safe}",
    )


@router.get("/wells_logger_data_summary", tags=["data"])
def logger_data_summary(query: queries.Wells = Depends(), format: str = "json"):
    db = connect_to_sageodata(service_name=query.env)
    dh_nos, name, name_safe, query_params = query.find_wells()
    df = db.logger_data_summary(dh_nos)
    return apply_format(
        df, format=format, response_name=f"wells_logger_data_summary__{name_safe}"
    )


@router.get("/wells_logger_data_by_dh", tags=["data"])
def logger_data_by_dh(query: queries.Wells = Depends(), format: str = "json"):
    db = connect_to_sageodata(service_name=query.env)
    dh_nos, name, name_safe, query_params = query.find_wells()
    df = db.logger_data_by_dh(dh_nos)
    return apply_format(
        df, format=format, response_name=f"wells_logger_data_by_dh__{name_safe}"
    )


@router.get("/wells_logger_wl_data_by_dh", tags=["data"])
def logger_wl_data_by_dh(query: queries.Wells = Depends(), format: str = "json"):
    db = connect_to_sageodata(service_name=query.env)
    dh_nos, name, name_safe, query_params = query.find_wells()
    df = db.logger_wl_data_by_dh(dh_nos)
    return apply_format(
        df, format=format, response_name=f"wells_logger_wl_data_by_dh__{name_safe}"
    )


@router.get("/wells_geophys_log_metadata", tags=["data"])
def geophys_log_metadata(query: queries.Wells = Depends(), format: str = "json"):
    db = connect_to_sageodata(service_name=query.env)
    dh_nos, name, name_safe, query_params = query.find_wells()
    df = db.geophys_log_metadata(dh_nos)
    return apply_format(
        df, format=format, response_name=f"wells_geophys_log_metadata__{name_safe}"
    )


@router.get("/wells_geophys_log_files", tags=["data"])
def geophys_log_files(query: queries.Wells = Depends(), format: str = "json"):
    db = connect_to_sageodata(service_name=query.env)
    dh_nos, name, name_safe, query_params = query.find_wells()
    df = db.geophys_log_files(dh_nos)
    return apply_format(
        df, format=format, response_name=f"wells_geophys_log_files__{name_safe}"
    )


@router.get("/wells_drillhole_document_image_list", tags=["data"])
def drillhole_document_image_list(
    query: queries.Wells = Depends(), format: str = "json"
):
    db = connect_to_sageodata(service_name=query.env)
    dh_nos, name, name_safe, query_params = query.find_wells()
    df = db.drillhole_document_image_list(dh_nos)
    return apply_format(
        df,
        format=format,
        response_name=f"wells_drillhole_document_image_list__{name_safe}",
    )


@router.get("/wells_data_available", tags=["data"])
def data_available(query: queries.Wells = Depends(), format: str = "json"):
    db = connect_to_sageodata(service_name=query.env)
    dh_nos, name, name_safe, query_params = query.find_wells()
    df = db.data_available(dh_nos)
    return apply_format(
        df,
        format=format,
        response_name=f"wells_data_available__{name_safe}",
    )


@router.get("/drillhole_document_image", tags=["data"], response_class=Response)
def drillhole_document_image(
    image_no: int,
    width: int = -1,
    height: int = -1,
    inline: bool = False,
    env: str = "prod",
):
    db = connect_to_sageodata(service_name=env)

    cursor = db.cursor()
    var = cursor.var(cx_Oracle.BLOB)
    cursor.execute(
        """
            declare
                t_Image ordsys.ordimage;
            begin
                select Image
                into t_Image
                from dhdb.dd_dh_image where image_no = {:.0f};

                :1 := t_Image.source.localdata;

            end;""".format(
            image_no
        ),
        (var,),
    )
    blob = var.getvalue()
    image = Image.open(blob)
    image = gd.resize_image(image, width=width, height=height)
    memfile = io.BytesIO()
    image.save(memfile, "PNG", quality=100)
    memfile.seek(0)
    data = memfile.read()
    if inline:
        data_base64 = base64.b64encode(data)  # encode to base64 (bytes)
        data_base64 = data_base64.decode()
        img_data = '<img src="data:image/jpeg;base64,' + data_base64 + '">'
        response = Response(content=f"<html>{img_data}</html>", media_type="text/html")
    else:
        response = Response(content=data, media_type="image/png")
        response.headers[
            "Content-Disposition"
        ] = f"attachment; filename=drillhole_document_image_{image_no}.png"
    return response

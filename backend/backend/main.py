#!/usr/bin/env python3
import logging

from fastapi import FastAPI

from backend import models, schemas

# set logging to display all messages INFO and above
logger = logging.getLogger()
logger.setLevel(logging.INFO)

db_session = models.init_db("sqlite:///:memory:")


logger.info("Starting FastAPI server")
app = FastAPI(title="Rails Takehome", version="0.1.0")


@app.get("/reports")
async def get_all_report_configs() -> list[schemas.ReportBase]:
    # TODO:
    raise NotImplementedError


@app.get("/reports/{id}")
async def get_report_config(id: int) -> schemas.ReportBase:
    # TODO:
    raise NotImplementedError


@app.put("/reports/{id}")
async def put_report_config(id: int, body: schemas.ReportBase) -> None:
    # TODO:
    raise NotImplementedError


@app.delete("/reports/{id}")
async def delete_report_config(id: int) -> None:
    # TODO:
    raise NotImplementedError


@app.get("/reports/{id}/data")
async def get_report_data(id: int) -> schemas.ReportData:
    # TODO: https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-stooq
    raise NotImplementedError

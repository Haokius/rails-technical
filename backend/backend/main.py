#!/usr/bin/env python3
import logging

from fastapi import FastAPI

from backend import models, schemas

import pandas_datareader.data as web

from datetime import date

# set logging to display all messages INFO and above
logger = logging.getLogger()
logger.setLevel(logging.INFO)

db_session = models.init_db("sqlite:///:memory:")


logger.info("Starting FastAPI server")
app = FastAPI(title="Rails Takehome", version="0.1.0")


@app.get("/dummy")
async def dummy() -> schemas.ReportBase:
    # dummy reportbase
    return schemas.ReportBase(
        name="dummy", 
        date_start=date(2022, 1, 1), 
        date_end=date(2022, 1, 10), 
        tickers=[
            {"ticker": "AAPL", "metric": "open"},
            {"ticker": "MSFT", "metric": "close"}
        ])

@app.get("/reports")
async def get_all_report_configs() -> list[schemas.ReportBase]:
    return db_session.query(models.ReportConfig).all()


@app.get("/reports/{id}")
async def get_report_config(id: int) -> schemas.ReportBase:
    return db_session.query(models.ReportConfig).filter(models.ReportConfig.id == id).first()


@app.put("/reports/{id}")
async def put_report_config(id: int, body: schemas.ReportBase) -> None:
    report = models.ReportConfig(id=id, name=body.name, date_start=body.date_start, date_end=body.date_end, tickers=body.tickers)
    db_session.add(report)
    db_session.commit()
    db_session.refresh(report)


@app.delete("/reports/{id}")
async def delete_report_config(id: int) -> None:
    report = db_session.query(models.ReportConfig).filter(models.ReportConfig.id == id).first()
    db_session.delete(report)
    db_session.commit()


@app.get("/reports/{id}/data")
async def get_report_data(id: int) -> schemas.ReportData:
    # TODO: https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-stooq
    
     # first query the report configs database
    report = db_session.query(models.ReportConfig).filter(models.ReportConfig.id == id).first()
    tickers = [ticker_info["ticker"] for ticker_info in report.tickers]
    metrics = [ticker_info["metric"] for ticker_info in report.tickers]
    date_start = report.date_start
    date_end = report.date_end

    # get the dataframe
    df = web.DataReader(tickers, 'stooq', date_start, date_end)

    output = []
    # convert to list of ReportDataUnit
    # iterate through the dataframe by date
    for date in df.index:
        for ticker, metric in zip(tickers, metrics):
            report_data_unit = schemas.ReportDataUnit(ticker=ticker, date=date, value=df.loc[date, (metric.capitalize(), ticker)], metric=metric)
            output.append(report_data_unit)

    output = output[::-1]

    return schemas.ReportData(data=output)

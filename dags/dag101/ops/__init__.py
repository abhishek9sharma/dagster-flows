"""Definitions that provide Dagster code locations."""
from dag101.assets.data.dask_check import some_computation
from dag101.assets.data.ingest import download_data
from dagster import Definitions

defs = Definitions(
    assets=[download_data, some_computation],
)

from dagster import job, op
from dagster_aws.s3.io_manager import s3_pickle_io_manager
from dagster_aws.s3.resources import s3_resource
from dagster_dask import dask_executor


@op
def hello_world():
    return "Hello, World!"


from dagster_dask import dask_executor


@job(executor_def=dask_executor)
def local_dask_job():
    hello_world()


@job(
    executor_def=dask_executor,
    resource_defs={"io_manager": s3_pickle_io_manager, "s3": s3_resource},
)
def distributed_dask_job():
    hello_world()

import dask.array as da
from dagster import asset


@asset
def some_computation():
    x = da.random.random(size=(10000, 10000), chunks=(1000, 1000))
    # x = x.persist()
    # progress(x)
    x.sum().compute()
    # x.mean(axis=0).compute()
    # x[x < 0] = 0
    # x[x > x.mean(axis=0)] = 1
    # y = x + x.T
    # da.diag(y).compute()

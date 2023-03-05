import os
import tarfile
import urllib.request

from dagster import asset


@asset
def download_data():
    # url="https://tickettagger.blob.core.windows.net/datasets/nlbse23-issue-classification-train.csv.tar.gz"
    # tgt_file_path = os.path.join("data", "data.tar.gz")
    # urllib.request.urlretrieve(url, tgt_file_path)
    # # # Extract the tar file
    # # with tarfile.open(filename, "r:gz") as tar:
    # #     tar.extractall(foldername)
    print("some data is downloaed here")

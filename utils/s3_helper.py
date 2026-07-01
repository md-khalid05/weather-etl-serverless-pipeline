import boto3

s3 = boto3.client("s3")


def download_file(bucket, key, destination):
    """
    Download a file from Amazon S3.
    """
    s3.download_file(bucket, key, destination)


def upload_file(source, bucket, key):
    """
    Upload a file to Amazon S3.
    """
    s3.upload_file(source, bucket, key)
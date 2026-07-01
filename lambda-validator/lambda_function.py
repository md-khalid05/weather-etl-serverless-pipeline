import json
import os
import tempfile

import pandas as pd

from utils.constants import PROCESSED_PREFIX
from utils.csv_helper import validate_dataframe
from utils.logger import get_logger
from utils.s3_helper import download_file, upload_file


logger = get_logger()


def lambda_handler(event, context):
    """
    Validator Lambda

    Trigger:
        S3 Object Created (raw/)

    Workflow:
        S3(raw) -> Validate -> S3(processed)
    """

    try:

        # -----------------------------------------
        # Read S3 Event
        # -----------------------------------------

        record = event["Records"][0]

        bucket = record["s3"]["bucket"]["name"]
        key = record["s3"]["object"]["key"]

        logger.info("=" * 60)
        logger.info("Weather Validator Started")
        logger.info("=" * 60)

        logger.info(f"Bucket : {bucket}")
        logger.info(f"Object : {key}")

        filename = os.path.basename(key)

        local_input = os.path.join(
            tempfile.gettempdir(),
            filename
        )

        local_output = os.path.join(
            tempfile.gettempdir(),
            f"validated_{filename}"
        )

        # -----------------------------------------
        # Download File
        # -----------------------------------------

        logger.info("Downloading CSV from S3...")

        download_file(
            bucket=bucket,
            key=key,
            destination=local_input
        )

        logger.info("Download Successful")

        # -----------------------------------------
        # Read CSV
        # -----------------------------------------

        df = pd.read_csv(local_input)

        logger.info(f"Records Found : {len(df)}")

        # -----------------------------------------
        # Validate Dataset
        # -----------------------------------------

        clean_df, stats = validate_dataframe(df)

        logger.info("Validation Completed")

        logger.info(
            json.dumps(
                stats,
                indent=4
            )
        )

        # -----------------------------------------
        # Save Clean Dataset
        # -----------------------------------------

        clean_df.to_csv(
            local_output,
            index=False
        )

        processed_key = (
            PROCESSED_PREFIX + filename
        )

        # -----------------------------------------
        # Upload Clean File
        # -----------------------------------------

        upload_file(
            source=local_output,
            bucket=bucket,
            key=processed_key
        )

        logger.info(
            f"Uploaded : {processed_key}"
        )

        logger.info("=" * 60)
        logger.info("Validator Finished Successfully")
        logger.info("=" * 60)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Validation Successful",
                "statistics": stats,
                "processed_file": processed_key
            })
        }

    except Exception as error:

        logger.exception(error)

        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(error)
            })
        }
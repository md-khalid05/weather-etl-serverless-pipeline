import json
import csv
import boto3
from io import StringIO
from datetime import datetime
from decimal import Decimal

# AWS Clients
s3 = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")

# Configuration
BUCKET_NAME = "weather-etl-khalid-2026"
OBJECT_KEY = "raw/weather.csv"
TABLE_NAME = "clean_weather_records"

table = dynamodb.Table(TABLE_NAME)


def lambda_handler(event, context):

    try:
        # Read CSV file from S3
        response = s3.get_object(
            Bucket=BUCKET_NAME,
            Key=OBJECT_KEY
        )

        csv_content = response["Body"].read().decode("utf-8")
        reader = csv.DictReader(StringIO(csv_content))

        total_records = 0
        inserted_records = 0
        rejected_records = 0

        processed_time = datetime.utcnow().isoformat()

        for row in reader:

            total_records += 1

            try:

                # Validate required fields
                required_fields = [
                    "record_id",
                    "city",
                    "temperature_c",
                    "humidity",
                    "wind_speed",
                    "condition",
                    "latitude",
                    "longitude",
                    "timestamp",
                ]

                if any(not row[field] for field in required_fields):
                    rejected_records += 1
                    print(f"Rejected record {row.get('record_id')} : Missing required field")
                    continue

                # Clean & Transform
                item = {
                    "record_id": row["record_id"],
                    "city": row["city"].strip().upper(),
                    "temperature_c": Decimal(row["temperature_c"]),
                    "humidity": int(row["humidity"]),
                    "wind_speed": Decimal(row["wind_speed"]),
                    "condition": row["condition"].strip(),
                    "latitude": Decimal(row["latitude"]),
                    "longitude": Decimal(row["longitude"]),
                    "timestamp": row["timestamp"],
                    "processed_time": processed_time
                }

                # Load into DynamoDB
                table.put_item(Item=item)

                inserted_records += 1

            except Exception as e:
                rejected_records += 1
                print(f"Error processing record {row.get('record_id')}: {str(e)}")

        audit = {
            "Total Records": total_records,
            "Inserted": inserted_records,
            "Rejected": rejected_records,
            "Processed Time": processed_time
        }

        print(json.dumps(audit, indent=4))

        return {
            "statusCode": 200,
            "body": json.dumps({
                "records_written": inserted_records,
                "records_rejected": rejected_records,
                "total_records": total_records
            })
        }

    except Exception as e:
        print(f"Fatal Error: {str(e)}")

        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }

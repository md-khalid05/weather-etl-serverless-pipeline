"""
Project-wide constants.
"""

RAW_PREFIX = "raw/"
PROCESSED_PREFIX = "processed/"

REQUIRED_COLUMNS = [
    "record_id",
    "city",
    "temperature_c",
    "humidity",
    "wind_speed",
    "condition",
    "latitude",
    "longitude",
    "timestamp"
]

TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"
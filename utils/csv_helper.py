import pandas as pd

from utils.constants import REQUIRED_COLUMNS


def validate_dataframe(df):
    """
    Validate and clean the weather dataset.

    Returns:
        cleaned_df (DataFrame)
        stats (dict)
    """

    original_count = len(df)

    # -------------------------------------------------
    # Check Required Columns
    # -------------------------------------------------
    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    # -------------------------------------------------
    # Remove Rows with Missing Values
    # -------------------------------------------------
    df = df.dropna()

    # -------------------------------------------------
    # Convert Numeric Columns
    # -------------------------------------------------
    numeric_columns = [
        "temperature_c",
        "humidity",
        "wind_speed",
        "latitude",
        "longitude"
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    # Remove rows that became NaN after conversion
    df = df.dropna()

    # -------------------------------------------------
    # Business Rule Validation
    # -------------------------------------------------

    # Temperature should be between -50°C and 60°C
    df = df[
        (df["temperature_c"] >= -50) &
        (df["temperature_c"] <= 60)
    ]

    # Humidity should be between 0% and 100%
    df = df[
        (df["humidity"] >= 0) &
        (df["humidity"] <= 100)
    ]

    # Wind speed should be non-negative
    df = df[
        df["wind_speed"] >= 0
    ]

    # Latitude should be between -90 and 90
    df = df[
        (df["latitude"] >= -90) &
        (df["latitude"] <= 90)
    ]

    # Longitude should be between -180 and 180
    df = df[
        (df["longitude"] >= -180) &
        (df["longitude"] <= 180)
    ]

    # -------------------------------------------------
    # Remove Duplicate Weather Records
    # -------------------------------------------------
    df = df.drop_duplicates(
        subset="record_id"
    )

    # -------------------------------------------------
    # Processing Statistics
    # -------------------------------------------------
    cleaned_count = len(df)
    rejected_count = original_count - cleaned_count

    stats = {
        "total_records": original_count,
        "valid_records": cleaned_count,
        "rejected_records": rejected_count
    }

    return df, stats
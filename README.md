# Weather ETL Serverless Pipeline on AWS

A production-style serverless ETL pipeline built using AWS services. This project demonstrates how raw weather data stored in Amazon S3 is automatically processed by AWS Lambda, validated, transformed, and loaded into Amazon DynamoDB.

---

## Project Overview

This project implements a fully serverless ETL (Extract, Transform, Load) pipeline.

The pipeline automatically:

- Reads weather CSV files from Amazon S3
- Validates incoming records
- Cleans and transforms the data
- Loads processed records into Amazon DynamoDB
- Records processing logs in Amazon CloudWatch

The project is designed following production-style folder organization and CI/CD best practices.

---

## Architecture

```
                +----------------+
                |   Weather CSV  |
                +-------+--------+
                        |
                        v
                +----------------+
                |   Amazon S3    |
                +-------+--------+
                        |
                  Object Created
                        |
                        v
                +----------------+
                | AWS Lambda ETL |
                +-------+--------+
                        |
        +---------------+----------------+
        |                                |
        v                                v
+---------------+              +------------------+
| DynamoDB      |              | CloudWatch Logs  |
| Clean Records |              | Audit & Errors   |
+---------------+              +------------------+
```

---

## AWS Services Used

- Amazon S3
- AWS Lambda
- Amazon DynamoDB
- Amazon CloudWatch
- IAM
- GitHub
- GitHub Actions (CI)
- AWS CodeBuild (planned)

---

## Features

- Serverless ETL architecture
- Automatic S3 event trigger
- CSV validation
- Data cleaning
- Data transformation
- DynamoDB storage
- CloudWatch logging
- Git version control
- CI/CD ready repository

---

## Folder Structure

```
weather-etl-serverless-pipeline/
│
├── src/
│   └── lambda_function.py
│
├── infrastructure/
│   └── buildspec.yml
│
├── sample_data/
│   └── weather.csv
│
├── screenshots/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ETL Workflow

1. Upload CSV file to Amazon S3
2. Amazon S3 triggers AWS Lambda
3. Lambda validates the records
4. Invalid records are rejected
5. Valid records are transformed
6. Processed data is inserted into DynamoDB
7. Processing logs are stored in CloudWatch

---

## Sample Dataset

Each weather record contains:

- Record ID
- City
- Temperature
- Humidity
- Wind Speed
- Weather Condition
- Latitude
- Longitude
- Timestamp

---

## Project Screenshots

The `screenshots/` directory contains:

- S3 Bucket
- Lambda Function
- CloudWatch Logs
- DynamoDB Records
- GitHub Repository

---

## Future Improvements

- CI/CD using GitHub Actions
- AWS CodeBuild Integration
- Terraform Infrastructure as Code
- CloudFormation deployment
- Data quality monitoring
- SNS email notifications
- Unit testing
- Dockerized local testing

---

## Author

**Md Khalid Ansari**

B.Tech Computer Science Engineering

Aspiring Data Engineer

GitHub:
https://github.com/md-khalid05
# Trigger Test Tue Jun 30 17:31:34 IST 2026

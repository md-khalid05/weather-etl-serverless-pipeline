# Weather ETL Serverless Pipeline on AWS

A production-style **Serverless ETL (Extract, Transform, Load)** pipeline built using AWS cloud services and modern DevOps practices.

The project demonstrates how weather CSV data stored in Amazon S3 is automatically processed by AWS Lambda, validated and transformed, loaded into Amazon DynamoDB, monitored using Amazon CloudWatch, and continuously integrated using GitHub Actions, AWS CodeBuild, and AWS CodePipeline.

---

# Project Overview

This project automates the complete ETL workflow:

- Upload raw weather CSV files to Amazon S3
- Automatically trigger AWS Lambda
- Validate incoming records
- Clean and transform data
- Store processed records in Amazon DynamoDB
- Record execution logs in Amazon CloudWatch
- Automatically build the project using GitHub Actions
- Deploy build validation using AWS CodePipeline

The project follows production-style folder organization and CI/CD best practices.

---

# Architecture

```
                    Weather CSV
                         │
                         ▼
                  Amazon S3 Bucket
                         │
                  ObjectCreated Event
                         │
                         ▼
                 AWS Lambda Function
                         │
        ┌────────────────┴────────────────┐
        ▼                                 ▼
 Amazon DynamoDB                  CloudWatch Logs

             GitHub Repository
                     │
              GitHub Actions
                     │
             AWS CodePipeline
                     │
              AWS CodeBuild
```

---

# Technology Stack

| Category       | Service           |
| -------------- | ----------------- |
| Storage        | Amazon S3         |
| Compute        | AWS Lambda        |
| Database       | Amazon DynamoDB   |
| Monitoring     | Amazon CloudWatch |
| Source Control | GitHub            |
| CI             | GitHub Actions    |
| CD             | AWS CodePipeline  |
| Build          | AWS CodeBuild     |
| Language       | Python 3          |
| SDK            | boto3             |

---

# AWS Resources

| Resource        | Name                    |
| --------------- | ----------------------- |
| S3 Bucket       | weather-etl-khalid-2026 |
| Lambda Function | weather-etl-processor   |
| DynamoDB Table  | clean_weather_records   |
| Build Project   | weather-etl-build       |
| Pipeline        | weather-etl-pipeline    |

---

# Features

- Fully serverless architecture
- Automatic S3 event trigger
- CSV validation
- Data cleaning
- Data transformation
- DynamoDB storage
- CloudWatch logging
- Git version control
- GitHub Actions CI
- AWS CodePipeline
- AWS CodeBuild integration
- Production-style project structure

---

# Project Structure

```
weather-etl-serverless-pipeline/

│
├── src/
│     └── lambda_function.py
│
├── infrastructure/
│     └── buildspec.yml
│
├── sample_data/
│     └── weather.csv
│
├── screenshots/
│
├── .github/
│     └── workflows/
│             ci.yml
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ETL Workflow

### Extract

- Weather CSV is uploaded into Amazon S3.

### Transform

The Lambda function:

- validates required fields
- removes invalid records
- converts records into structured format
- prepares data for DynamoDB

### Load

- Clean records are inserted into Amazon DynamoDB.

### Monitor

- Processing statistics and errors are logged into Amazon CloudWatch.

---

# Sample Dataset

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

# CI/CD Workflow

```
Developer
     │
 git push
     │
     ▼
 GitHub Repository
     │
     ▼
 GitHub Actions
     │
     ▼
 AWS CodePipeline
     │
     ▼
 AWS CodeBuild
     │
     ▼
 Build Successful
```

---

# Project Results

Successfully demonstrated:

- Automatic Lambda trigger from Amazon S3
- Validation of weather CSV records
- Transformation of raw records
- Storage of clean records in DynamoDB
- CloudWatch execution logging
- GitHub Actions CI workflow
- AWS CodeBuild execution
- AWS CodePipeline execution

Final Output

- Total records processed: **100**
- Records inserted: **100**
- Invalid records: **0**

---

# Screenshots

The screenshots directory contains:

- GitHub Repository
- Amazon S3 Bucket
- AWS Lambda
- CloudWatch Logs
- DynamoDB Records
- GitHub Actions
- AWS CodePipeline

---

# Reflection Questions

## 1. Why did you choose Amazon S3 for this project?

Amazon S3 is highly scalable, durable, and integrates directly with AWS Lambda through event notifications. It is widely used as the storage layer for serverless ETL pipelines.

---

## 2. What is your partition key and why?

The DynamoDB table uses **record_id** as the partition key.

Since every weather record has a unique identifier, this ensures efficient lookups while preventing duplicate entries.

---

## 3. What transformation does the Lambda function perform?

The Lambda function:

- validates CSV records
- removes invalid data
- converts records into structured JSON
- prepares data for DynamoDB
- logs processing statistics to CloudWatch

---

## 4. What did GitHub Actions automate?

GitHub Actions automatically:

- checks out the repository
- installs dependencies
- runs validation/build steps
- verifies the project after every push

---

## 5. What did AWS CodePipeline do?

AWS CodePipeline automatically:

- detects GitHub commits
- retrieves the latest source code
- triggers AWS CodeBuild
- validates the project build
- reports build success or failure

---

## 6. What files should never be committed to GitHub?

Sensitive files should never be committed, including:

- AWS Access Keys
- Secret Keys
- `.env`
- API Tokens
- Passwords
- Private Certificates
- Generated cache files
- Virtual environments

---

# Future Improvements

- Infrastructure as Code using Terraform
- AWS SAM deployment
- AWS CloudFormation templates
- Amazon SNS email notifications
- Data quality reporting
- CloudWatch dashboards
- Unit testing with pytest
- Docker-based local testing

---

# Author

**Md Khalid Ansari**

B.Tech Computer Science Engineering

Aspiring Data Engineer

GitHub: [https://github.com/md-khalid05](https://github.com/md-khalid05)

---

## Final Assessment

This revised README would move your project from a typical student submission to something suitable for a hiring manager or recruiter to review. It documents the architecture, implementation, AWS resources, CI/CD workflow, results, and reflection questions in one place, making it useful both for grading and as a portfolio project.

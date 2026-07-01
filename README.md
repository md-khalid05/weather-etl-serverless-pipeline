# 🌦️ Weather ETL Serverless Pipeline on AWS

A production-inspired **serverless ETL pipeline** that extracts weather data from a CSV dataset stored in Amazon S3, transforms and validates the records using AWS Lambda, loads the cleaned data into Amazon DynamoDB, and automates validation and deployment through GitHub Actions and AWS CodePipeline.

---

![Python](https://img.shields.io/badge/Python-3.11-blue)
![AWS Lambda](https://img.shields.io/badge/AWS-Lambda-orange)
![Amazon S3](https://img.shields.io/badge/Amazon-S3-red)
![DynamoDB](https://img.shields.io/badge/AWS-DynamoDB-blue)
![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-success)
![AWS CodePipeline](https://img.shields.io/badge/AWS-CodePipeline-yellow)

## 📖 Project Overview

This project demonstrates the implementation of a serverless ETL (Extract, Transform, Load) pipeline on AWS using modern cloud-native services.

The pipeline automatically processes weather datasets uploaded to Amazon S3. Whenever a CSV file is uploaded, an AWS Lambda function is triggered to validate, clean, and transform the dataset before loading the processed records into Amazon DynamoDB. Throughout execution, Amazon CloudWatch captures logs for monitoring and troubleshooting.

To improve software quality and deployment reliability, the entire project is integrated with GitHub Actions for continuous integration (CI) and AWS CodePipeline with AWS CodeBuild for continuous deployment (CD).

The objective is to simulate a real-world data engineering workflow using fully managed AWS services while following serverless architecture principles.

## 🎯 Business Scenario

Imagine a weather monitoring organization that receives daily weather observations collected from multiple cities.

Instead of manually cleaning and storing the data, the organization requires an automated cloud-based ETL pipeline capable of:

- Receiving raw weather datasets
- Validating incoming records
- Cleaning inconsistent or invalid data
- Standardizing weather attributes
- Loading processed records into a NoSQL database
- Maintaining execution logs for auditing
- Automatically validating and deploying application updates

This project implements that workflow using AWS serverless services.

## 🏗️ Architecture Overview

```text
                Weather Dataset (CSV)
                        │
                        ▼
            Amazon S3 (raw folder)
                        │
             S3 Object Created Event
                        │
                        ▼
              AWS Lambda ETL Function
        ┌───────────────────────────────┐
        │ Read CSV                      │
        │ Validate Records              │
        │ Remove Invalid Entries        │
        │ Standardize Data              │
        │ Generate record_id            │
        │ Add processed_timestamp       │
        └───────────────────────────────┘
                        │
                        ▼
       Amazon DynamoDB (clean_weather_records)
                        │
                        ▼
         Amazon CloudWatch Logs & Monitoring


──────────────────────────────────────────────

GitHub Repository
        │
GitHub Actions (CI)
        │
AWS CodeBuild
        │
AWS CodePipeline (CD)
        │
Automatic Deployment
```

## 🔄 ETL Workflow

| Stage         | Description                                                                                    |
| ------------- | ---------------------------------------------------------------------------------------------- |
| **Extract**   | Read raw weather CSV from Amazon S3                                                            |
| **Transform** | Validate records, remove invalid rows, standardize fields, generate unique IDs, add timestamps |
| **Load**      | Store cleaned records into Amazon DynamoDB                                                     |
| **Audit**     | Log processing statistics in Amazon CloudWatch                                                 |

## 💻 Technology Stack

| Category             | Technology                |
| -------------------- | ------------------------- |
| Programming Language | Python 3.11               |
| Cloud Platform       | Amazon Web Services (AWS) |
| Storage              | Amazon S3                 |
| Compute              | AWS Lambda                |
| Database             | Amazon DynamoDB           |
| Monitoring           | Amazon CloudWatch         |
| Version Control      | Git & GitHub              |
| CI                   | GitHub Actions            |
| CD                   | AWS CodePipeline          |
| Build Service        | AWS CodeBuild             |

## ☁️ AWS Services Used

| Service           | Purpose                        |
| ----------------- | ------------------------------ |
| Amazon S3         | Stores raw weather datasets    |
| AWS Lambda        | Executes ETL logic             |
| Amazon DynamoDB   | Stores cleaned weather records |
| Amazon CloudWatch | Execution logs and monitoring  |
| AWS IAM           | Secure permission management   |
| GitHub            | Source code management         |
| GitHub Actions    | Continuous Integration         |
| AWS CodeBuild     | Build validation               |
| AWS CodePipeline  | Continuous Deployment          |

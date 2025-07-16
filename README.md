# pipay-enhancement-suite

A collection of AWS-based enhancements for PiPay internal systems:  
- Access Control  
- Geo-Fencing for Field Staff  
- Real-Time Payment Alerts  

## Technologies Used
- AWS Lambda
- Amazon DynamoDB
- Amazon API Gateway
- Amazon SNS
- Amazon Cognito
- Ionic / Angular (Frontend)

## Project Structure
pipay-enhancement-suite/
├── access-control/
├── geo-fencing/
├── real-time-alerts/
│   └── lambda_function.py
└── README.md

## How to Run
1. Clone this repo
2. Deploy AWS services via console or IaC (CloudFormation / Terraform)
3. Connect Ionic frontend via API Gateway endpoints
4. Test user access via Cognito authentication

## Purpose
Enhance PiPay systems with reliable, serverless AWS architecture for secure and efficient internal tools.

## Author
[Prajwal Kori](https://github.com/kori-prajwal)

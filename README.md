# Email-Validation-API

# Demonstration video
https://www.loom.com/share/d37509d6440a433d880d9fc824e65a41?sid=8ba03a72-d709-4456-8819-3fedbd7b24bc

# Overview
<br>
This project implements an Email Validation API using AWS API Gateway and AWS Lambda. The API validates the format of provided email addresses but does not check if the domain exists. It ensures that email addresses follow a standard structure like example@domain.com.

# Technologies Used
<br>
1. AWS Lambda: Executes the email validation logic.
<br>
2. AWS API Gateway: Manages the API endpoint and routes HTTP requests to the Lambda function.
<br>
3. Python: Used as the runtime environment for the Lambda function.
<br>
4. Postman: Used for testing the API.

# Features
* Validates email addresses based on their format using a regular expression.
* Returns a 200 OK response for valid email formats and a 400 Bad Request for invalid formats.
* Easily deployable with AWS API Gateway and Lambda.

# Prerequisites
* An AWS account with access to Lambda and API Gateway.
* Basic understanding of Python and AWS Services.
* Postman for testing the API






















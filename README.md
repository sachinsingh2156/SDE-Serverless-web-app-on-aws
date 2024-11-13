Here is a README file for your "Serverless Web Application on AWS" project:

---

# Serverless Web Application on AWS

## Project Description
This project demonstrates a serverless web application built using Amazon Web Services (AWS) technologies. The application allows users to create, read, update, and delete (CRUD) items from a DynamoDB table through a contact form on a web page. The form collects data such as the user's name, email, subject, and message, which is then processed by an AWS Lambda function and stored in a DynamoDB table.

## Project Architecture
![Project Architecture](Serverless.jpg)

The project architecture consists of:
- **DynamoDB**: A NoSQL database used to store user-submitted data from the contact form.
- **AWS Lambda**: A serverless compute service that processes the data submitted by the contact form and performs CRUD operations on DynamoDB.
- **Amazon S3**: Used for hosting the static files of the web application (HTML, CSS, JavaScript).
- **Amazon CloudFront**: A content delivery network (CDN) used to distribute the S3-hosted web application for low latency and better performance.

## Project Setup

### Steps to Build the Project

1. **Create a DynamoDB Table**
   - Create a DynamoDB table (e.g., `studentMessage`) to store items with attributes like `id`, `name`, `email`, `subject`, and `message`.
  
2. **Build the Lambda Function**
   - Write and deploy a Lambda function to handle incoming requests and store data in DynamoDB.
   - The Lambda function processes data sent from the contact form, checks for required fields, and stores it in the DynamoDB table.
  
3. **Set Up S3 for Static Hosting**
   - Create an S3 bucket to host the HTML, CSS, and JavaScript files of the web application.
   - Enable static website hosting on the S3 bucket and upload the static files.

4. **Create a CloudFront Distribution**
   - Set up a CloudFront distribution to serve the static files stored in S3 for better performance and low latency.
   - Configure the distribution to point to your S3 bucket as the origin.

### Frontend Code
All the code you can find in the following GitHub Repository
```bash
   git clone https://github.com/sachinsingh2156/SDE-serverless-project-on-AWS.git
   ```

## Expected Outcome
By completing this project, you will have:
- A fully functional serverless web application hosted on AWS.
- Experience using AWS services such as Lambda, DynamoDB, S3, and CloudFront.
- Hands-on skills in building and deploying serverless applications on AWS.

## Conclusion
This project provides practical experience in cloud computing, serverless architecture, and AWS integration. It demonstrates how to set up a simple yet powerful serverless web application to handle CRUD operations without traditional server management.

---

import json
import boto3
from datetime import datetime

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table_name = 'studentMessage'  
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    # Remove the explicit CORS headers in code and rely on API Gateway or Lambda URL configuration
    headers = {
        "Access-Control-Allow-Methods": "POST, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type"
    }

    try:
        # Parse the incoming request body
        body = json.loads(event['body'])
        name = body.get('name')
        email = body.get('email')
        subject = body.get('subject')
        message = body.get('message')

        # Check for required fields
        if not name or not email or not subject or not message:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({'error': 'Missing required fields'})
            }

        # Prepare the item to store in DynamoDB
        item = {
            'id': datetime.utcnow().isoformat(),
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }

        # Store the item in DynamoDB
        table.put_item(Item=item)

        # Return success response
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({'message': 'Data stored successfully'})
        }

    except Exception as e:
        # Log the exception and return an error response
        print(f"Error storing data: {str(e)}")
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': 'Could not store data'})
        }

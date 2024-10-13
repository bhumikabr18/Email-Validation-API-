import json
import re

def lambda_handler(event, context):
    # Parse the request body
    body = json.loads(event.get('body', '{}'))
    email = body.get('email', '')
    
    # Define the regex for a valid email
    email_regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    
    # Validate the email against the regex
    if re.match(email_regex, email):
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Valid email'})
        }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Invalid email format'})
        }

import json
import re

def lambda_handler(event, context):
    try:
        # Parse the input JSON body
        body = json.loads(event['body'])
        email = body.get('email', '')
        
        # Email validation regex pattern
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(email_pattern, email):
            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Valid email'})
            }
        else:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'Invalid email format'})
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Error processing request', 'error': str(e)})
        }

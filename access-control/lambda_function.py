import json

def handler(event, context):
    user_role = event.get('role', 'guest')

    if user_role == 'admin':
        access = "Access granted to admin resources."
    else:
        access = "Access denied. Insufficient permissions."

    return {
        'statusCode': 200,
        'body': json.dumps({'message': access})
    }

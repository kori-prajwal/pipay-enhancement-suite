import json
from geopy.distance import geodesic

def handler(event, context):
    user_location = event.get('user_location')  # (lat, lon)
    store_location = event.get('store_location')  # (lat, lon)

    distance = geodesic(user_location, store_location).meters

    if distance <= 100:
        message = "Within allowed geo-fence."
    else:
        message = "Outside allowed geo-fence."

    return {
        'statusCode': 200,
        'body': json.dumps({'distance': distance, 'message': message})
    }

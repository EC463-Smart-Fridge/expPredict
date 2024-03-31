import json
from datetime import datetime, timedelta


def predict_expiration(input_string):
    # Load the predicted expiration times dataset
    with open('expirationPredictions.json', 'r') as file:
        expiration_data = json.load(file)

    # Variables to keep track of the best match
    best_match = None
    best_score = 0

    # Search for a product that best matches the user input
    for product_id, product_info in expiration_data.items():
        keywords = product_info.get('Keywords', [])

        # Calculate match score for current product
        score = sum(1 for keyword in keywords if keyword in input_string)

        # Update best match if current product has higher score
        if score > best_score:
            best_match = product_info
            best_score = score

    # Output results
    if best_match:
        # Calculate predicted expiration date
        expiration_time_days = best_match['Expiration_time_DAYS']
        current_date = datetime.now().date()
        expiration_date = current_date + timedelta(days=expiration_time_days)

        # Convert to Unix timestamp format
        expiration_datetime = datetime.combine(expiration_date, datetime.min.time())
        expiration_timestamp = expiration_datetime.timestamp()
        return int(expiration_timestamp)
    else:
        return None


# Lambda handler function
def lambda_handler(event, context):
    input_string = event['input_string']
    expiration_timestamp = predict_expiration(input_string)
    if expiration_timestamp:
        return {"expiration_timestamp": expiration_timestamp}
    else:
        return {"error": "No matching products found."}


'''
event = {
    "input_string": "chocolate milk"
}
print(lambda_handler(event, None))
'''

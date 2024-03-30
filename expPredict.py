import json
from datetime import datetime, timedelta

# load the predicted expiration times dataset
with open('expirationPredictions.json', 'r') as file:
    expiration_data = json.load(file)

user_input = input("Enter food item name: ")

# variables to keep track of the best match
best_match = None
best_score = 0

# search for a product that best matches the user input
for product_id, product_info in expiration_data.items():
    keywords = product_info.get('Keywords', [])

    # calculate match score for current product
    score = sum(1 for keyword in keywords if keyword in user_input)

    # update best match if current product has higher score
    if score > best_score:
        best_match = product_info
        best_score = score

# output results
if best_match:
    print("Match found!")
    print("Name:", best_match['Name'])
    print("Subtitle:", best_match['Name_subtitle'])
    print("Keywords:", best_match['Keywords'])
    print("Expiration time:", best_match['Expiration_time'], best_match['Expiration_metric'])
    print("")

    # calculate predicted expiration date
    expiration_time_days = best_match['Expiration_time_DAYS']

    current_date = datetime.now().date()
    print("Current date:", current_date.strftime("%Y-%m-%d"))

    expiration_date = current_date + timedelta(days=expiration_time_days)
    print("Predicted expiration date:", expiration_date.strftime("%Y-%m-%d"))

else:
    print("No matching products found.")

import json

# using food storage data scrubbed and extracted from FoodKeeper
with open('foodkeeperFormatted.json', 'r') as file:
    formatted_data = json.load(file)

# dictionary to store expiration time predictions for each food product type
expiration_predictions = {}

for product_id, product_info in formatted_data.items():

    # check which fields are not null
    fields = [
        'Pantry_Max', 'DOP_Pantry_Max', 'Pantry_After_Opening_Max',
        'Refrigerate_Max', 'DOP_Refrigerate_Max', 'Refrigerate_After_Opening_Max',
        'Freeze_Max', 'DOP_Freeze_Max'
    ]
    non_null_fields = [field for field in fields if product_info.get(field) is not None]
    if len(non_null_fields) == 1:
        expiration_basis = non_null_fields[0]
        expiration_time = product_info[expiration_basis]
    else:
        expiration_basis = ''
        expiration_time = 0

    metrics = [
        'Pantry_Metric', 'DOP_Pantry_Metric', 'Pantry_After_Opening_Metric',
        'Refrigerate_Metric', 'DOP_Refrigerate_Metric', 'Refrigerate_After_Opening_Metric',
        'Freeze_Metric', 'DOP_Freeze_Metric'
    ]

    if expiration_basis == 'Pantry_Max':
        expiration_metric = product_info['Pantry_Metric']
    elif expiration_basis == 'DOP_Pantry_Max':
        expiration_metric = product_info['DOP_Pantry_Metric']
    elif expiration_basis == 'Pantry_After_Opening_Max':
        expiration_metric = product_info['Pantry_After_Opening_Metric']
    elif expiration_basis == 'Refrigerate_Max':
        expiration_metric = product_info['Refrigerate_Metric']
    elif expiration_basis == 'DOP_Refrigerate_Max':
        expiration_metric = product_info['DOP_Refrigerate_Metric']
    elif expiration_basis == 'Refrigerate_After_Opening_Max':
        expiration_metric = product_info['Refrigerate_After_Opening_Metric']
    elif expiration_basis == 'Freeze_Max':
        expiration_metric = product_info['Freeze_Metric']
    elif expiration_basis == 'DOP_Freeze_Max':
        expiration_metric = product_info['DOP_Freeze_Metric']
    else:
        expiration_metric = ''

    expiration_predictions[product_id] = {
        'Name': product_info['Name'],
        'Name_subtitle': product_info['Name_subtitle'],
        'Keywords': product_info['Keywords'],
        'Expiration_time': expiration_time,
        'Expiration_metric': expiration_metric
    }

# save to new JSON file
with open('expirationPredictions.json', 'w') as file:
    json.dump(expiration_predictions, file, indent=4)

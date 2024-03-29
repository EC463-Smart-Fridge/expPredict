import json

# using food storage data scrubbed and extracted from FoodKeeper
with open('foodkeeperFormatted.json', 'r') as file:
    formatted_data = json.load(file)

# dictionary to store expiration time predictions for each food product type
expiration_predictions = {}

for product_id, product_info in formatted_data.items():
    expiration_basis = ''
    # check which fields are not null
    fields = [
        'Pantry_Max', 'DOP_Pantry_Max', 'Pantry_After_Opening_Max',
        'Refrigerate_Max', 'DOP_Refrigerate_Max', 'Refrigerate_After_Opening_Max',
        'Freeze_Max', 'DOP_Freeze_Max'
    ]
    non_null_fields = [field for field in fields if product_info.get(field) is not None]

    # choose basis for expiration time based on available storage data
    if len(non_null_fields) == 1:
        expiration_basis = non_null_fields[0]

    elif 'Pantry_Max' not in non_null_fields and 'DOP_Pantry_Max' not in non_null_fields and 'Pantry_After_Opening_Max' not in non_null_fields:

        if 'Refrigerate_After_Opening_Max' in non_null_fields:
            expiration_basis = 'Refrigerate_After_Opening_Max'
        elif 'DOP_Refrigerate_Max' in non_null_fields:
            expiration_basis = 'DOP_Refrigerate_Max'
        elif 'Refrigerate_Max' in non_null_fields:
            expiration_basis = 'Refrigerate_Max'
        elif 'DOP_Freeze_Max' in non_null_fields:
            expiration_basis = 'DOP_Freeze_Max'
        elif 'Freeze_Max' in non_null_fields:
            expiration_basis = 'Freeze_Max'
    else:
        compare_times = {}
        if 'Pantry_Max' in non_null_fields:
            pantry_max = product_info['Pantry_Max']
            pantry_metric = product_info['Pantry_Metric']
            if pantry_metric == 'Days':
                pantry_max_time = pantry_max
            elif pantry_metric == 'Weeks':
                pantry_max_time = pantry_max * 7
            elif pantry_metric == 'Months':
                pantry_max_time = pantry_max * 30
            elif pantry_metric == 'Years':
                pantry_max_time = pantry_max * 365
            else:
                pantry_max_time = 0
            compare_times['Pantry_Max'] = pantry_max_time
        if 'DOP_Pantry_Max' in non_null_fields:
            dop_pantry_max = product_info['DOP_Pantry_Max']
            dop_pantry_metric = product_info['DOP_Pantry_Metric']
            if dop_pantry_metric == 'Days':
                dop_pantry_time = dop_pantry_max
            elif dop_pantry_metric == 'Weeks':
                dop_pantry_time = dop_pantry_max * 7
            elif dop_pantry_metric == 'Months':
                dop_pantry_time = dop_pantry_max * 30
            elif dop_pantry_metric == 'Years':
                dop_pantry_time = dop_pantry_max * 365
            else:
                dop_pantry_time = 0
            compare_times['DOP_Pantry_Max'] = dop_pantry_time
        if 'Pantry_After_Opening_Max' in non_null_fields:
            pantry_after_open = product_info['Pantry_After_Opening_Max']
            pantry_after_open_metric = product_info['Pantry_After_Opening_Metric']
            if pantry_after_open_metric == 'Days':
                pantry_after_open_time = pantry_after_open
            elif pantry_after_open_metric == 'Weeks':
                pantry_after_open_time = pantry_after_open * 7
            elif pantry_after_open_metric == 'Months':
                pantry_after_open_time = pantry_after_open * 30
            elif pantry_after_open_metric == 'Years':
                pantry_after_open_time = pantry_after_open * 365
            else:
                pantry_after_open_time = 0
            compare_times['Pantry_After_Opening_Max'] = pantry_after_open_time
        if 'Refrigerate_Max' in non_null_fields:
            fridge_max = product_info['Refrigerate_Max']
            fridge_metric = product_info['Refrigerate_Metric']
            if fridge_metric == 'Days':
                fridge_max_time = fridge_max
            elif fridge_metric == 'Weeks':
                fridge_max_time = fridge_max * 7
            elif fridge_metric == 'Months':
                fridge_max_time = fridge_max * 30
            elif fridge_metric == 'Years':
                fridge_max_time = fridge_max * 365
            else:
                fridge_max_time = 0
            compare_times['Refrigerate_Max'] = fridge_max_time
        if 'DOP_Refrigerate_Max' in non_null_fields:
            dop_fridge_max = product_info['DOP_Refrigerate_Max']
            dop_fridge_metric = product_info['DOP_Refrigerate_Metric']
            if dop_fridge_metric == 'Days':
                dop_fridge_max_time = dop_fridge_max
            elif dop_fridge_metric == 'Weeks':
                dop_fridge_max_time = dop_fridge_max * 7
            elif dop_fridge_metric == 'Months':
                dop_fridge_max_time = dop_fridge_max * 30
            elif dop_fridge_metric == 'Years':
                dop_fridge_max_time = dop_fridge_max * 365
            else:
                dop_fridge_max_time = 0
            compare_times['DOP_Refrigerate_Max'] = dop_fridge_max_time
        if 'Refrigerate_After_Opening_Max' in non_null_fields:
            fridge_after_open_max = product_info['Refrigerate_After_Opening_Max']
            fridge_after_open_metric = product_info['Refrigerate_After_Opening_Metric']
            if fridge_after_open_metric == 'Days':
                fridge_after_open_time = fridge_after_open_max
            elif fridge_after_open_metric == 'Weeks':
                fridge_after_open_time = fridge_after_open_max * 7
            elif fridge_after_open_metric == 'Months':
                fridge_after_open_time = fridge_after_open_max * 30
            elif fridge_after_open_metric == 'Years':
                fridge_after_open_time = fridge_after_open_max * 365
            else:
                fridge_after_open_time = 0
            compare_times['Refrigerate_After_Opening_Max'] = fridge_after_open_time

        if compare_times:
            expiration_basis = max(compare_times, key=lambda k: compare_times[k])
        elif 'DOP_Freeze_Max' in non_null_fields:
            expiration_basis = 'DOP_Freeze_Max'
        elif 'Freeze_Max' in non_null_fields:
            expiration_basis = 'Freeze_Max'

    metrics = [
        'Pantry_Metric', 'DOP_Pantry_Metric', 'Pantry_After_Opening_Metric',
        'Refrigerate_Metric', 'DOP_Refrigerate_Metric', 'Refrigerate_After_Opening_Metric',
        'Freeze_Metric', 'DOP_Freeze_Metric'
    ]

    # get the correct time metric based on basis for expiration time
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

    if expiration_basis != '' and expiration_metric != '':
        expiration_time = product_info[expiration_basis]
        if expiration_metric == 'Days':
            expiration_time_days = expiration_time
        elif expiration_metric == 'Weeks':
            expiration_time_days = expiration_time * 7
        elif expiration_metric == 'Months':
            expiration_time_days = expiration_time * 30
        elif expiration_metric == 'Years':
            expiration_time_days = expiration_time * 365
        else:
            expiration_time_days = 0
    else:
        expiration_time = None
        expiration_time_days = None

    expiration_predictions[product_id] = {
        'Name': product_info['Name'],
        'Name_subtitle': product_info['Name_subtitle'],
        'Keywords': product_info['Keywords'],
        'Expiration_basis': expiration_basis,
        'Expiration_time': expiration_time,
        'Expiration_metric': expiration_metric,
        'Expiration_time_DAYS': expiration_time_days
    }

# save to new JSON file
with open('expirationPredictions.json', 'w') as file:
    json.dump(expiration_predictions, file, indent=4)

import json

with open('foodkeeper.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# extract "Product" sheet data
product_data = data['sheets'][2]['data']

# create dictionary to store formatted data
formatted_data = {}

# extract identifier data for each product
for entry in product_data:
    product_id = entry[0]['ID']
    product_name = entry[2]['Name']
    product_subtitle = entry[3]['Name_subtitle']
    product_keywords = entry[4]['Keywords']

    # split keywords string into array of strings
    keywords_array = [keyword.strip().lower() for keyword in product_keywords.split(",")]

    # extract relevant data
    pantry_max = None
    pantry_metric = None
    dop_pantry_max = None
    dop_pantry_metric = None
    pantry_after_opening_max = None
    pantry_after_opening_metric = None
    refrigerate_max = None
    refrigerate_metric = None
    dop_refrigerate_max = None
    dop_refrigerate_metric = None
    refrigerate_after_opening_max = None
    refrigerate_after_opening_metric = None
    freeze_max = None
    freeze_metric = None
    dop_freeze_max = None
    dop_freeze_metric = None

    for item in entry:
        if 'Pantry_Max' in item:
            pantry_max = item['Pantry_Max']
        elif 'Pantry_Metric' in item:
            pantry_metric = item['Pantry_Metric']
        elif 'DOP_Pantry_Max' in item:
            dop_pantry_max = item['DOP_Pantry_Max']
        elif 'DOP_Pantry_Metric' in item:
            dop_pantry_metric = item['DOP_Pantry_Metric']
        elif 'Pantry_After_Opening_Max' in item:
            pantry_after_opening_max = item['Pantry_After_Opening_Max']
        elif 'Pantry_After_Opening_Metric' in item:
            pantry_after_opening_metric = item['Pantry_After_Opening_Metric']
        elif 'Refrigerate_Max' in item:
            refrigerate_max = item['Refrigerate_Max']
        elif 'Refrigerate_Metric' in item:
            refrigerate_metric = item['Refrigerate_Metric']
        elif 'DOP_Refrigerate_Max' in item:
            dop_refrigerate_max = item['DOP_Refrigerate_Max']
        elif 'DOP_Refrigerate_Metric' in item:
            dop_refrigerate_metric = item['DOP_Refrigerate_Metric']
        elif 'Refrigerate_After_Opening_Max' in item:
            refrigerate_after_opening_max = item['Refrigerate_After_Opening_Max']
        elif 'Refrigerate_After_Opening_Metric' in item:
            refrigerate_after_opening_metric = item['Refrigerate_After_Opening_Metric']
        elif 'Freeze_Max' in item:
            freeze_max = item['Freeze_Max']
        elif 'Freeze_Metric' in item:
            freeze_metric = item['Freeze_Metric']
        elif 'DOP_Freeze_Max' in item:
            dop_freeze_max = item['DOP_Freeze_Max']
        elif 'DOP_Freeze_Metric' in item:
            dop_freeze_metric = item['DOP_Freeze_Metric']

    # store product data to formatted data dictionary
    formatted_data[product_id] = {
        'Name': product_name,
        'Name_subtitle': product_subtitle,
        'Keywords': keywords_array,
        'Pantry_Max': pantry_max,
        'Pantry_Metric': pantry_metric,
        'DOP_Pantry_Max': dop_pantry_max,
        'DOP_Pantry_Metric': dop_pantry_metric,
        'Pantry_After_Opening_Max': pantry_after_opening_max,
        'Pantry_After_Opening_Metric': pantry_after_opening_metric,
        'Refrigerate_Max': refrigerate_max,
        'Refrigerate_Metric': refrigerate_metric,
        'DOP_Refrigerate_Max': dop_refrigerate_max,
        'DOP_Refrigerate_Metric': dop_refrigerate_metric,
        'Refrigerate_After_Opening_Max': refrigerate_after_opening_max,
        'Refrigerate_After_Opening_Metric': refrigerate_after_opening_metric,
        'Freeze_Max': freeze_max,
        'Freeze_Metric': freeze_metric,
        'DOP_Freeze_Max': dop_freeze_max,
        'DOP_Freeze_Metric': dop_freeze_metric
    }

# save to new JSON file
with open('foodkeeperFormatted.json', 'w') as file:
    json.dump(formatted_data, file, indent=4)


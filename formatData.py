import json

with open('foodkeeper.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# extract "Product" sheet data
product_data = data['sheets'][2]['data']

# create dictionary to store formatted data
formatted_data = {}

# extract relevant entries from each entry
for entry in product_data:
    product_id = entry[0]['ID']
    product_name = entry[2]['Name']
    product_subtitle = entry[3]['Name_subtitle']
    product_keywords = entry[4]['Keywords']

    # store entry data to formatted data dictionary
    formatted_data[product_id] = {
        'Name': product_name,
        'Name_subtitle': product_subtitle,
        'Keywords': product_keywords
    }

# save to new JSON file
with open('foodkeeperFormatted.json', 'w') as file:
    json.dump(formatted_data, file)


import json
import re
import csv

def correcting_business_json(raw_file):
    with open(raw_file,'r') as rfile:
        raw_data = rfile.read()
    fixed_json = re.sub('}\n*{"business_id":', '},\n{"business_id":', raw_data.strip())
    fixed_json = '{\n"businesses": [' + fixed_json + ']\n}'
    json_data = json.loads(fixed_json)

    for business in json_data["businesses"]:
        business.pop("attributes", None)
        business.pop("hours", None)
        if business["categories"]:
            business["categories"] = list(business["categories"].split(", "))
        else: []

    with open("initial_business.json", "w") as file:
        json.dump(json_data, file, indent=4)

correcting_business_json('yelp_academic_dataset_business.json')

def json_to_csv(json_file):
    with open(json_file, 'r') as jfile:
        content = json.load(jfile)
    list_of_businesses = list(content.values())

    for item in list_of_businesses[0]:
        fieldnames = item.keys()

    with open('intermediate_business.csv', 'w', newline='') as fp:
        writer = csv.DictWriter(fp, fieldnames)
        writer.writeheader()

        for item in list_of_businesses[0]:
            writer.writerow(item)
json_to_csv('initial_business.json')

def csv_to_json(csv_file, json_file):
    data = []
    with open(csv_file, mode='r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            row["categories"] = re.findall(r"'([^']*)'", row["categories"])
            data.append(row)

    with open(json_file, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

csv_to_json('intermediate_business.csv', 'final_business.json')

#correcting_business_json('yelp_academic_dataset_business.json')
#json_to_csv('initial_business.json')
#csv_to_json('intermediate_business.csv', 'final_business.json')

import json
import re
import csv


def extracting_reviews_json(raw_file):
    with open(raw_file,'r') as rfile:
        raw_data = rfile.read()
    fixed_json = re.sub('}\n*{"review_id":"', '},\n{"review_id":"', raw_data.strip())
    fixed_json = '{\n"reviews": [' + fixed_json + ']\n}'

    json_data = json.loads(fixed_json)
    for review in json_data["reviews"]:
        review.pop("text", None)

    with open('initial_reviews.json', 'w') as jfile:
        json.dump(json_data, jfile, indent=4)

    print("Initial json file created")
extracting_reviews_json('yelp_academic_dataset_review.json')

def json_to_csv(json_file):
    with open(json_file, 'r') as jfile:
        content = json.load(jfile)
    list_of_reviews = list(content.values())

    for item in list_of_reviews[0]:
        fieldnames = item.keys()

    with open('intermediate_reviews.csv', 'w', newline='') as fp:
        writer = csv.DictWriter(fp, fieldnames)
        writer.writeheader()

        for item in list_of_reviews[0]:
            writer.writerow(item)
json_to_csv('initial_reviews.json')

def csv_to_json(csv_file, json_file):
    data = []
    with open(csv_file, mode='r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            data.append(row)

    with open(json_file, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)
csv_to_json('intermediate_reviews.csv', 'final_reviews.json')


#extracting_reviews_json('yelp_academic_dataset_review.json')
#json_to_csv('initial_reviews.json')
csv_to_json('intermediate_reviews.csv', 'final_reviews.json')




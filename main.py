import ijson
import csv
import datetime
print(datetime.datetime.now())

json_file_path = '2024-05-01_anthem_index.json'
# json_file_path = 'test.json'
csv_file_path = 'output_file.csv'
with open(json_file_path, 'r') as json_file, open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    objects = ijson.items(json_file, 'reporting_structure.item.in_network_files.item')
    for item in objects:
        des_details = item['description'].lower()
        if "ny" in des_details or " new york" in des_details:
            # if "ppo" in des_details:
            writer.writerow([item['location']])
    csv_file.flush()
    csv_file.close()

print(datetime.datetime.now())
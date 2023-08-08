import csv
import json

f = open('input.json')

data = json.load(f)

f.close()

with open('output.csv', 'w', newline='') as csv_file:

    writer = csv.writer(csv_file)
    
    count = 0

    for i in data:
        if count == 0:
            writer.writerow(i.keys())
            count += 1
        writer.writerow(i.values())

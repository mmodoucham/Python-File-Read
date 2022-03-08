#read a txt file
f = open('files/data.txt', 'r')
print(f.read())
f.close()

print("--------------------------------------------------")

#read a csv file
import csv
with open('files/data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)

print("--------------------------------------------------")

#read an xml file
from logging import root
import xml.etree.ElementTree as ET
content = ET.parse('files/data.xml')
root = content.getroot()
for child in root:
    print(child.tag, child.text)

print("--------------------------------------------------")

#read json file
import json
with open('files/data.json') as json_file:
    data = json.load(json_file)
    print(data)
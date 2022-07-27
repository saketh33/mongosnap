import xmltodict
import json
import os
directory = os.path.dirname(os.path.realpath(__file__))
for filename in os.listdir(directory):
    if filename.endswith('.xml'):
        file_location=os.path.abspath(filename)
        with open(file_location) as xml_file:
            data_dict = xmltodict.parse(xml_file.read())
        xml_file.close()
        file_name = os.path.basename(file_location)
        name,ext=file_name.split('.');
        json_data = json.dumps(data_dict)
        with open(name+".json", "w") as json_file:
            json_file.write(json_data)
        json_file.close()
l=[]

directory = os.path.dirname(os.path.realpath(__file__))
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        file_location=os.path.abspath(filename)
        l.append(file_location)

print(l)
from pymongo import MongoClient
client = MongoClient("localhost", 27017)
mydatabase = client.local
for file_name in l:
    with open(file_name) as f:
        file_data = json.load(f)
        mydatabase.bigfile.insert_one(file_data)

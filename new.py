import time
import xmltodict
import json
import os
start= time.time()
l=[]
directory = os.path.dirname(os.path.realpath(__file__))
print(directory)
for filename in os.listdir(directory):
    if filename.endswith('.xml'):
        file_location=os.path.abspath(filename)
        with open(file_location) as xml_file:
            data_dict = xmltodict.parse(xml_file.read())
        xml_file.close()
        file_name = os.path.basename(file_location)
        name,ext=file_name.split('.')
        json_data = json.dumps(data_dict)
        with open(name+".json", "w") as json_file:
            json_file.write(json_data)
        json_file.close()
        l.append(directory+"\\"+name+".json")

def merge_JsonFiles(filename):
    result = list()
    for f1 in filename:
        with open(f1, 'r') as infile:
            result.append(json.load(infile))
    with open('counseling3.json', 'w') as output_file:
        json.dump(result, output_file)
merge_JsonFiles(l)

from pymongo import MongoClient
client = MongoClient("localhost", 27017)
mydatabase = client.local
with open(directory+"\\"+"counseling3.json") as f:
    file_data = json.load(f)
    mydatabase.bigfile.insert_many(file_data)
end = time.time()
print("The time of execution of above program is :", end-start)

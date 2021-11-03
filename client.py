
import requests
import json
from requests.structures import CaseInsensitiveDict

url = "http://localhost:5000/predict"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Content-Type"] = "application/json"

with open("student_test.json") as json_file:
    data = json.load(json_file)

resp = requests.post(url, headers=headers, json = data)

print(str(resp.content,'utf-8' ))
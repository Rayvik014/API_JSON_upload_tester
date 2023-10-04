from requests import post
import io

url = 'http://127.0.0.1:8000/api/upload'
file = 'json_medved2_for_test.json'
with io.open(file, 'r', encoding='utf-8') as json_file:
    json_for_upload = json_file.read()
req = post(url, json=json_for_upload)
req.text
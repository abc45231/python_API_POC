import requests
import jsonpath
import json

def test_add_student_data():
    API_URL="http://thetestingworldapi.com/api/studentsDetails"
    file = open('F:\\Python_API_Testing\\Request_json.json', 'r')
    json_request=json.loads(file.read())
    response = requests.post(API_URL,json_request)
    print(response.text)
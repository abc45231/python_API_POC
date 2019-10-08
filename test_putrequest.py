import json
import requests
import jsonpath

def test_put_student_data():

    API_URL="http://thetestingworldapi.com/api/studentsDetails/147070"
    file = open("F:\\Python_API_Testing\\Request_json1.json","r")
    json_request = json.loads(file.read())
    response = requests.put(API_URL,json_request)
    print(response.text)
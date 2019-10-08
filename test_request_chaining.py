import requests
import jsonpath
import json

def test_add_new_student():
    global id
    API_URL="http://thetestingworldapi.com/api/studentsDetails"
    file = open('F:\\Python_API_Testing\\Request_json.json', 'r')
    request_json = json.loads(file.read())
    response = requests.post(API_URL, request_json)
    print(response.text)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

def test_get_details():
    final_details = "http://thetestingworldapi.com/api/FinalStudentDetails/" + str(id[0])
    response = requests.get(final_details)
    print(response.text)



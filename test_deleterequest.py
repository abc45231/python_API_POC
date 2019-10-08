import requests
import jsonpath
import json

def test_delete_student():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/147070"
    response = requests.delete(API_URL)
    print(response.text)

def test_get_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/147070"
    response=requests.get(API_URL)
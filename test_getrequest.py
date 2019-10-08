import requests
import jsonpath
import json

def test_get_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/147070"
    response=requests.get(API_URL)
   # json_response = json.loads(response.text)

    json_response = response.json()
    id=jsonpath.jsonpath(json_response,'data.id')

    assert id[0] == 147070
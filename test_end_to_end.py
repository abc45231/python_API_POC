import requests
import jsonpath
import json

def test_Add_new_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    file = open('F:\\Python_API_Testing\\Request_json.json', 'r')
    request_json=json.loads(file.read())
    response = requests.post(API_URL,request_json)
    id=jsonpath.jsonpath(response.json(),'id')
    print(id[0])
    #print(response.text)

#like this we need to add the below technical details
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    file = open('F:\\Python_API_Testing\\Request_json.json', 'r')
    request_json = json.loads(file.read())
    request_json['id']=int(id[0])
    request_json['st_id']=id[0]
    response = requests.post(API_URL, request_json)
    print(response.text)

    #like this we need to add address

    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    file = open('F:\\Python_API_Testing\\Request_json.json', 'r')
    request_json = json.loads(file.read())
    request_json['stid'] = id[0]
    response = requests.post(API_URL, request_json)
    print(response.text)

#get the final details of the student
    final_details="http://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
    response = requests.get(final_details)
    print(response.text)








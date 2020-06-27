import requests

SERVER_URL="http://localhost:8000"


def create_session(**payload):
    resp = requests.post(SERVER_URL + '/api/v1/sessions/', json=payload)
    resp.raise_for_status() # ensure it succeeded
    return resp

resp = create_session(session_config_name='trust', room_name='econ101', num_participants=4, modified_session_config_fields=dict(num_apples=10, abc=[1, 2, 3]))
print(resp.text) # returns the session code

def get_session(name):
    resp = requests.get(f"{SERVER_URL}/SessionMonitor/{name}",  headers={'Content-type': 'application/json'})
    print(resp.text)

get_session(resp.text)

"""

POST http://localhost:8000/api/v1/sessions/ HTTP/1.1
content-type: application/json
{
    "session_config_name": "trust",
    "room_name": "econ101",
    "num_participants": 4
}

http://localhost:8000/SessionMonitor/abuu1dm4/

GET http://localhost:8000/SessionMonitor/abuu1dm4/ HTTP/1.1 
content-type: application/json

GET http://localhost:8000/SessionData/abuu1dm4/ HTTP/1.1 
content-type: application/json


"""
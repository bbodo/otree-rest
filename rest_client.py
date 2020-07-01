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

def set_participant_vars(**payload):
    resp = requests.post(SERVER_URL + '/api/v1/participant_vars/', json=payload)
    resp.raise_for_status() # ensure it succeeded
    return resp

resp = set_participant_vars(room_name='econ101', participant_label='Charlie', vars=dict(age=25, is_male=True, x=[3,6,9]))
print(resp.text)

"""

POST http://localhost:8001/api/v1/sessions/ HTTP/1.1
content-type: application/json
otree-rest-key: testkey

{
    "session_config_name": "trust",
    "room_name": "econ101",
    "num_participants": 4
}


POST http://localhost:8000/api/cool/sessions/ HTTP/1.1
content-type: application/json
otree-rest-key: testkey

{
    "session_config_name": "trust",
    "room_name": "econ101",
    "num_participants": 4
}

http://localhost:8000/SessionMonitor/abuu1dm4/

GET http://localhost:8001/SessionMonitor/abuu1dm4/ HTTP/1.1 
content-type: application/json

GET http://localhost:8001/SessionData/abuu1dm4/ HTTP/1.1 
content-type: application/json

POST http://localhost:8001/api/v1/participant_vars/ HTTP/1.1
content-type: application/json
otree-rest-key: testkey

{
    "room_name": "econ101",
    "participant_label": "Alice",
    "vars": {
        "age": 225, 
        "is_male": false, 
        "x": [3,6,9]
    }
}


"""
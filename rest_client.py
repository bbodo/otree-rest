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

http://localhost:8000/SessionMonitor/abuu1dm4/

GET http://localhost:8001/SessionMonitor/l5ws5ht5/ HTTP/1.1 
content-type: application/json

GET http://localhost:8001/SessionData/l5ws5ht5/ HTTP/1.1 
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


DELETE http://localhost:8001/API/participants/12/?format=json HTTP/1.1
content-type: application/json
otree-rest-key: testkey

{"url":"http://localhost:8001/API/participants/12/?format=json","vars":{},"label":null,"id_in_session":1,"payoff":"0","time_started":"2020-07-09T15:05:13.932638+02:00","mturk_assignment_id":null,"mturk_worker_id":null,"_index_in_subsessions":0,"_index_in_pages":2,"_waiting_for_ids":null,"code":"ymaz61a2","visited":true,"_last_page_timestamp":1594299919,"_last_request_timestamp":1594299919,"is_on_wait_page":false,"_current_page_name":"Guess","_current_app_name":"guess_two_thirds","_round_number":1,"_current_form_page_url":"http://localhost:8000/p/ymaz61a2/guess_two_thirds/Guess/2/","_max_page_index":13,"_browser_bot_finished":false,"_is_bot":false,"is_browser_bot":false,"session":"http://localhost:8000/API/sessions/5/?format=json"}
"""
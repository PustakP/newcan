'''import datetime
from flask import Flask, request
from threading import Thread
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

app = Flask('ppbot')

# Global variable to store the service instance
global_service = None

@app.route('/')
def hrllo():
    return "hi barbie!"

@app.route('/oauth2callback')
def oauth_callback():
    global global_service  # Declare that you're using the global variable
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', scopes=['https://www.googleapis.com/auth/calendar'])
    flow.redirect_uri = 'https://newcan.pokilopatterson.repl.co'
    authorization_response = request.url
    flow.fetch_token(authorization_response=authorization_response)
    credentials = flow.credentials
    global_service = build('calendar', 'v3', credentials=credentials)  # Store the service instance

    # Rest of the oauth_callback function
    # Iterate through the schedule data and create events
    for time_slot, events_list in schedule_data.items():
        for event_details in events_list:
            event_title = event_details[0].split('-')[0].strip()
            event_description = '\n'.join(event_details)

            event = {
                'summary': event_title,
                'description': event_description,
                'start': {
                    'dateTime': datetime.datetime.now().replace(hour=int(time_slot.split(':')[0]), minute=0, second=0).isoformat(),
                    'timeZone': 'Asia/Calcutta',
                },
                'end': {
                    'dateTime': datetime.datetime.now().replace(hour=int(time_slot.split(':')[0]) + 1, minute=0, second=0).isoformat(),
                    'timeZone': 'Asia/Calcutta',
                },
            }

            created_event = service.events().insert(calendarId='primary', body=event).execute()
            print(f'Event created: {created_event["htmlLink"]}')

# Rest of your code
# Your schedule dictionary
schedule_data = {
    '8:00AM':
    [['MED MED201 - L1Lecture8:00AM -\n        9:25AMS. Floor D Block D217']],
    '9:00AM':
    [['CSD CSD101 - L1Lecture9:30AM -\n        10:55AMT. Floor B Block B315'],
     [
         'MED MED201 - L1Lecture8:00AM -\n        9:25AMS. Floor D Block D217\n        CSD CSD101 - L1Lecture9:30AM - 10:55AMT. Floor B Block B315'
     ],
     ['MED MED201 - L1Lecture9:30AM -\n        10:55AMS. Floor D Block D217']],
    '10:00AM':
    [['MAT MAT103 - L1Lecture10:30AM -\n        11:55AMT. Floor B Block B315'],
     ['CSD CSD101 - L1Lecture9:30AM -\n        10:55AMT. Floor B Block B315'],
     ['MAT MAT103 - L1Lecture10:30AM -\n        11:55AMT. Floor B Block B315']
     ],
    '11:00AM':
    [['PHY PHY101 - L3Lecture11:00AM -\n        11:55AMF. Floor D Block D102'],
     ['PHY PHY101 - L3Lecture11:00AM -\n        11:55AMF. Floor D Block D102'],
     ['PHY PHY101 - L3Lecture11:00AM -\n        11:55AMF. Floor D Block D102']
     ],
    '12:00PM': [],
    '1:00PM':
    [['CSD CSD101 - P2Practicum1:00PM -\n        2:55PMT. Floor D Block D313']
     ],
    '2:00PM': [],
    '3:00PM':
    [['MED MED201 - P4Practicum3:00PM -\n        4:55PMG. Floor C Block C013']
     ],
    '4:00PM': [],
    '5:00PM': [],
    '6:00PM':
    [['PHY PHY101 - T4Tutorial6:00PM -\n        6:55PMT. Floor D Block D306'],
     ['MAT MAT103 - T4Tutorial6:00PM -\n        6:55PMS. Floor B Block B219']]
}
for time_slot, events_list in schedule_data.items():
    for event_details in events_list:
        event_title = event_details[0].split('-')[0].strip()
        event_description = '\n'.join(event_details)

        event = {
            'summary': event_title,
            'description': event_description,
            'start': {
                'dateTime': datetime.datetime.now().replace(hour=int(time_slot.split(':')[0]), minute=0, second=0).isoformat(),
                'timeZone': 'Asia/Calcutta',
            },
            'end': {
                'dateTime': datetime.datetime.now().replace(hour=int(time_slot.split(':')[0]) + 1, minute=0, second=0).isoformat(),
                'timeZone': 'Asia/Calcutta',
            },
        }

        if global_service:  # Check if the service is defined
            created_event = global_service.events().insert(calendarId='primary', body=event).execute()
            print(f'Event created: {created_event["htmlLink"]}')

def start_server():
    app.run(host='0.0.0.0', port=8080)

t = Thread(target=start_server)
t.start()
'''

import datetime
from flask import Flask, request
from threading import Thread
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

app = Flask('ppbot')

@app.route('/')
def hello():
    return "hi barbie!"

def create_events(service, schedule_data):
    for time_slot, events_list in schedule_data.items():
        for event_details in events_list:
            event_title = event_details[0].split('-')[0].strip()
            event_description = '\n'.join(event_details)

            event = {
                'summary': event_title,
                'description': event_description,
                'start': {
                    'dateTime': datetime.datetime.now().replace(hour=int(time_slot.split(':')[0]), minute=0, second=0).isoformat(),
                    'timeZone': 'Asia/Calcutta',
                },
                'end': {
                    'dateTime': datetime.datetime.now().replace(hour=int(time_slot.split(':')[0]) + 1, minute=0, second=0).isoformat(),
                    'timeZone': 'Asia/Calcutta',
                },
            }

            created_event = service.events().insert(calendarId='primary', body=event).execute()
            print(f'Event created: {created_event["htmlLink"]}')

def start_server():
    app.run(host='0.0.0.0', port=8080)

def oauth_flow():
    with app.test_request_context('/oauth2callback'):  # Enter a request context
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', scopes=['https://www.googleapis.com/auth/calendar'])
        flow.redirect_uri = 'https://newcan.pokilopatterson.repl.co'
        authorization_response = request.url
        flow.fetch_token(authorization_response=authorization_response)
        credentials = flow.credentials
        service = build('calendar', 'v3', credentials=credentials)
    return service

if __name__ == '__main__':
    service = None
    t = Thread(target=start_server)
    t.start()
    while not service:
        service = oauth_flow()
    schedule_data = {
    '8:00AM':
    [['MED MED201 - L1Lecture8:00AM -\n        9:25AMS. Floor D Block D217']],
    '9:00AM':
    [['CSD CSD101 - L1Lecture9:30AM -\n        10:55AMT. Floor B Block B315'],
     [
         'MED MED201 - L1Lecture8:00AM -\n        9:25AMS. Floor D Block D217\n        CSD CSD101 - L1Lecture9:30AM - 10:55AMT. Floor B Block B315'
     ],
     ['MED MED201 - L1Lecture9:30AM -\n        10:55AMS. Floor D Block D217']],
    '10:00AM':
    [['MAT MAT103 - L1Lecture10:30AM -\n        11:55AMT. Floor B Block B315'],
     ['CSD CSD101 - L1Lecture9:30AM -\n        10:55AMT. Floor B Block B315'],
     ['MAT MAT103 - L1Lecture10:30AM -\n        11:55AMT. Floor B Block B315']
     ],
    '11:00AM':
    [['PHY PHY101 - L3Lecture11:00AM -\n        11:55AMF. Floor D Block D102'],
     ['PHY PHY101 - L3Lecture11:00AM -\n        11:55AMF. Floor D Block D102'],
     ['PHY PHY101 - L3Lecture11:00AM -\n        11:55AMF. Floor D Block D102']
     ],
    '12:00PM': [],
    '1:00PM':
    [['CSD CSD101 - P2Practicum1:00PM -\n        2:55PMT. Floor D Block D313']
     ],
    '2:00PM': [],
    '3:00PM':
    [['MED MED201 - P4Practicum3:00PM -\n        4:55PMG. Floor C Block C013']
     ],
    '4:00PM': [],
    '5:00PM': [],
    '6:00PM':
    [['PHY PHY101 - T4Tutorial6:00PM -\n        6:55PMT. Floor D Block D306'],
     ['MAT MAT103 - T4Tutorial6:00PM -\n        6:55PMS. Floor B Block B219']]
}
    create_events(service, schedule_data)

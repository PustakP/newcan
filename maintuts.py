import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

# Authenticate using OAuth2
flow = InstalledAppFlow.from_client_secrets_file('credentials.json', scopes=['https://www.googleapis.com/auth/calendar'])
credentials = flow.run_local_server(port=0, open_browser=False)  # Avoid opening a browser for authorization

# Build the Google Calendar service
service = build('calendar', 'v3', credentials=credentials)

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

# Iterate through the schedule data and create events
for time_slot, events_list in schedule_data.items():
  for event_details in events_list:
    event_title = event_details[0].split(
        '-')[0].strip()  # Extract event title from the details
    event_description = '\n'.join(event_details)

    # Create an event
    event = {
        'summary': event_title,
        'description': event_description,
        'start': {
            'dateTime':
            datetime.datetime.now().replace(hour=int(time_slot.split(':')[0]),
                                            minute=0,
                                            second=0).isoformat(),
            'timeZone':
            'Asia/Calcutta',
        },
        'end': {
            'dateTime':
            datetime.datetime.now().replace(hour=int(time_slot.split(':')[0]) +
                                            1,
                                            minute=0,
                                            second=0).isoformat(),
            'timeZone':
            'Asia/Calcutta',
        },
    }

    # Insert event to Google Calendar
    created_event = service.events().insert(calendarId='primary',
                                            body=event).execute()
    print(f'Event created: {created_event["htmlLink"]}')

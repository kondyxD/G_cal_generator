from __future__ import print_function
import datetime
import pickle
import os.path
import Utils.dateFunctions
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/calendar']


class GoogleCalAPI():
    def __init__(self):
        creds = None
        self.calendarId = None
        if os.path.exists('../token.pickle'):
            with open('../token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('Credentials/credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('../token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('calendar', 'v3', credentials=creds)

        self.calendar_list_entry = self.service.calendarList().get(calendarId='primary').execute()

        if not self.calendar_list_entry['accessRole']:
            print('API can\' connect!')

    def get_calendar_list_entry(self):
        return self.calendar_list_entry

    def get_my_calendars(self):
        result = self.service.calendarList().list().execute()['items'][0]
        self.calendarId = result['id']
        return result

    def get_my_events(self, date=None):
        if date is None:
            date = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        else:
            date = Utils.dateFunctions.getDateFromString(date)

        events_result = self.service.events().list(calendarId='primary', timeMin=date, maxResults=10, singleEvents=True,
                                                   orderBy='startTime').execute()

        events = events_result.get('items', [])
        if not events:
            return 'No upcoming events found.'
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            return {start, event['summary']}

    def create_event(self, start_time_str, summary, duration=1, unit='days', attendees=None,
                     description=None, location=None):

        interval = Utils.dateFunctions.getDateInterval(start_time_str, duration, unit)

        emails = []
        if attendees is not None & isinstance(attendees, list):
            for email in attendees:
                emails.append({'email': email})

        event = {
            'summary': summary,
            'location': location,
            'description': description,
            'start': {
                'dateTime': interval['start_time'],
                'timeZone': Utils.dateFunctions.getSystemTimeZone(),
            },
            'end': {
                'dateTime': interval['end_time'],
                'timeZone': Utils.dateFunctions.getSystemTimeZone(),
            },
            'recurrence': [
                'RRULE:FREQ=DAILY;COUNT=2'
            ],
            'attendees': emails,
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }

        event = self.service.events().insert(calendarId='primary', body=event).execute()
        print('Event created: %s' % (event.get('htmlLink')))

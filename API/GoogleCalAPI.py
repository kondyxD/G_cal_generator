from __future__ import print_function
import datetime
import pickle
import os.path
import datefinder
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/calendar']


class GoogleCalAPI():
    def __init__(self):
        if os.path.exists('../token.pickle'):
            with open('../token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    '../Credentials/credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('../token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('calendar', 'v3', credentials=creds)

    def get_my_calendars(self):
        return self.service.calendarList().list().execute

    def get_my_calendars_events(self, calendar_id):
        return self.service.events().list(calendarId=calendar_id, timeZone="Asia/Kolkata").execute()

    def create_event(self, start_time_str, summary, calendar_id = 'primary', duration=1, attendees=None, description=None, location=None):
        matches = list(datefinder.find_dates(start_time_str))
        if len(matches):
            start_time = matches[0]
            end_time = start_time + datetime.timedelta(hours=duration)

        event = {
            'summary': summary,
            'location': location,
            'description': description,
            'start': {
                'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
                'timeZone': datetime.timezone,
            },
            'end': {
                'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
                'timeZone': datetime.timezone,
            },
            'attendees': [
                {'email': attendees},
            ],
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }

        return self.service.events().insert(calendar_id, body=event, sendNotifications=True).execute()

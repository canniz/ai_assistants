from google_services.google_api_service import GoogleAPIService
from google_services.calendar_service import CalendarService
from google_services.email_service import EmailService
import json

SCOPES = [
    'https://www.googleapis.com/auth/calendar.readonly',
    'https://www.googleapis.com/auth/gmail.readonly'
]



class ActionModule:
    def __init__(self):
        # Initialize the Google API service with the necessary scopes
        self.google_api = GoogleAPIService('credentials/client_secret_oauth2.json', scopes=SCOPES)
        self.calendar_service = CalendarService(self.google_api)
        self.email_service = EmailService(self.google_api)

    
    def execute_action(self, action):
        name = action.function.name
        args = json.loads(action.function.arguments)
        if name == "get_emails":
            data = self.email_service.get_unread_emails()
        elif name == "get_calendar_events":
            data = self.calendar_service.get_events(**args)
        else:
            data = ""
            raise Exception("Unexpected Action")
        return data
    
    def get_emails(self):
        return
    
    def get_events(self, start_date_time, end_date_time):
        return
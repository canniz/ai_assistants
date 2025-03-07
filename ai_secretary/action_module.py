from google_services.google_api_service import GoogleAPIService
from google_services.calendar_service import CalendarService
from google_services.email_service import EmailService
from other_services.memory_service import MemoryService

import json

SCOPES = [
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/gmail.readonly'
]



class ActionModule:
    def __init__(self):
        # Initialize the Google API service with the necessary scopes
        self.google_api = GoogleAPIService('credentials/client_secret_oauth2.json', scopes=SCOPES)
        self.calendar_service = CalendarService(self.google_api)
        self.email_service = EmailService(self.google_api)
        self.memory_service = MemoryService()

    def set_assistant(self, assistant):
        self.memory_service.set_assistant(assistant)

    
    def execute_action(self, action):
        name = action.function.name
        args = json.loads(action.function.arguments)
        if name == "get_emails":
            data = self.email_service.get_unread_emails()
        elif name == "get_calendar_events":
            data = self.calendar_service.get_events(**args)
        elif name == "create_event":
            data = self.calendar_service.create_event(**args)
        elif name == "delete_and_update_temporary_memory":
            data = self.memory_service.delete_and_update_temporary_memory(**args)
        elif name == "append_string_to_permanent_memory":
            data = self.memory_service.append_string_to_permanent_memory(**args)
        elif name == "get_temporary_memory":
            data = self.memory_service.get_temporary_memory()
        else:
            data = ""
            raise Exception("Unexpected Action")
        return data

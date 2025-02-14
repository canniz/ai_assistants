# google_api_service.py
import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

class GoogleAPIService:
    def __init__(self, credentials_file, token_file='tokens/token.pickle', scopes=None):
        self.credentials_file = credentials_file
        self.token_file = token_file
        self.scopes = scopes if scopes else []
        self.credentials = self.authenticate()

    def authenticate(self):
        creds = None
        if os.path.exists(self.token_file):
            with open(self.token_file, 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.credentials_file, self.scopes)
                creds = flow.run_local_server(port=0)
            with open(self.token_file, 'wb') as token:
                pickle.dump(creds, token)
        return creds

    def get_service(self, api_name, api_version):
        return build(api_name, api_version, credentials=self.credentials)

# email_service.py
class EmailService:
    def __init__(self, google_api_service):
        self.google_api_service = google_api_service
        self.service = self.google_api_service.get_service('gmail', 'v1')

    def get_unread_emails(self):
        results = self.service.users().messages().list(userId='me', q="is:unread").execute()
        messages = results.get('messages', [])
        emails = []
        for msg in messages:
            message = self.service.users().messages().get(userId='me', id=msg['id']).execute()
            headers = self.parse_headers(message['payload']['headers'])
            mail = {}
            mail["From"] = headers["From"]
            mail["Subject"] = headers["Subject"]
            mail["Body"] = message["snippet"]
            mail["Date"] = headers["Date"]
            emails.append(mail)
        return emails
    
    def parse_headers(self, headers):
        res = {}
        for elem in headers:
            res[elem['name']] =  elem['value']
        return res

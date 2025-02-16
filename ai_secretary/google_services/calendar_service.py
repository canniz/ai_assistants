import json

class CalendarService:
    def __init__(self, google_api_service):
        self.google_api_service = google_api_service
        self.service = self.google_api_service.get_service('calendar', 'v3')

    def get_events(self, start_date_time, end_date_time):
        # Get all calendars
        calendars_result = self.service.calendarList().list().execute()
        clean_events = []

        for calendar in calendars_result['items']:
            calendar_id = calendar['id']
            # Get events for each calendar
            events_result = self.service.events().list(
                calendarId=calendar_id,
                timeMin=start_date_time,
                timeMax=end_date_time,
                singleEvents=True,
                orderBy='startTime'
            ).execute()

            for event in events_result.get('items', []):
                new_event = {}
                new_event['start'] = event['start'].get('dateTime', event['start'].get('date'))
                new_event['end'] = event['end'].get('dateTime', event['end'].get('date'))
                new_event['title'] = event.get('summary', 'No Title')
                new_event['creator'] = event.get('creator', {}).get('email', 'Unknown')
                new_event['link'] = event.get('htmlLink', '')
                new_event['conference_link'] = event.get('hangoutLink', '')
                new_event['calendar_name'] = calendar['summary']  # Add calendar name
                clean_events.append(new_event)
        return clean_events

    def create_event(self, start_date_time, end_date_time, summary):
        event = {
            'summary': summary,
            'start': {
                'dateTime': start_date_time,
                'timeZone': 'CET',  # Adjust the timezone as needed
            },
            'end': {
                'dateTime': end_date_time,
                'timeZone': 'CET',  # Adjust the timezone as needed
            },
        }
        
        # Create the event on the primary calendar
        created_event = self.service.events().insert(calendarId='primary', body=event).execute()
        response = {
            "status": "success",
            "link": created_event['htmlLink'],
            "summary": summary,
            "start": created_event['start']['dateTime'],
            "end": created_event['end']['dateTime']
        }
        return response

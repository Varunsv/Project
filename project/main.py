import google_apis_oauth
from googleapiclient.discovery import build

# Load the stored credentials in a variable say 'stringified_token

# Load the credentials object using the stringified token.
creds, refreshed = google_apis_oauth.load_credentials(stringified_token)

# Using credentials to access Upcoming Events
service = build('calendar', 'v3', credentials=creds)
now = datetime.datetime.utcnow().isoformat() + 'Z'
print('Getting the upcoming 10 events')
events_result = service.events().list(
    calendarId='primary', timeMin=now,
    maxResults=10, singleEvents=True,
    orderBy='startTime').execute()
events = events_result.get('items', [])

if not events:
    print('No upcoming events found.')
for event in events:
    start = event['start'].get('dateTime', event['start'].get('date'))
    print(start, event['summary'])
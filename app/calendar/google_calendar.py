from googleapiclient.discovery import build
from datetime import datetime, timedelta

def get_today_meetings(creds):
    service = build("calendar", "v3", credentials=creds)

    now = datetime.utcnow().isoformat() + "Z"
    end = (datetime.utcnow() + timedelta(days=1)).isoformat() + "Z"

    events_result = service.events().list(
        calendarId="primary",
        timeMin=now,
        timeMax=end,
        singleEvents=True,
        orderBy="startTime"
    ).execute()

    events = events_result.get("items", [])

    meetings = []
    for e in events:
        meetings.append({
            "source": "google",
            "title": e.get("summary"),
            "start": e["start"].get("dateTime"),
            "end": e["end"].get("dateTime"),
            "organizer": e.get("organizer", {}).get("email")
        })

    return meetings

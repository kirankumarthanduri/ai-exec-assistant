import requests
from datetime import datetime, timedelta

GRAPH_BASE = "https://graph.microsoft.com/v1.0"

def get_today_meetings(access_token):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    start = datetime.utcnow().isoformat() + "Z"
    end = (datetime.utcnow() + timedelta(days=1)).isoformat() + "Z"

    url = (
        f"{GRAPH_BASE}/me/calendarView"
        f"?startDateTime={start}&endDateTime={end}"
    )

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    events = response.json().get("value", [])

    meetings = []
    for e in events:
        meetings.append({
            "source": "outlook",
            "title": e.get("subject"),
            "start": e["start"]["dateTime"],
            "end": e["end"]["dateTime"],
            "organizer": e.get("organizer", {}).get("emailAddress", {}).get("name")
        })

    return meetings

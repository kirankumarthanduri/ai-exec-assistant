from ai.summarizer import summarize
from calendar.outlook_calendar import get_today_meetings as outlook_meetings
from calendar.google_calendar import get_today_meetings as google_meetings
from email.outlook import get_unread_emails as outlook_emails
from email.gmail import get_unread_emails as gmail_emails

def run_agent():
    print("🚀 Running AI Executive Assistant...")

    # TODO: replace with real tokens after OAuth
    outlook_token = "OUTLOOK_ACCESS_TOKEN"
    google_creds = None

    emails = []
    meetings = []

    try:
        emails.extend(outlook_emails(outlook_token))
    except Exception as e:
        print("Outlook email skipped:", e)

    try:
        emails.extend(gmail_emails(google_creds))
    except Exception as e:
        print("Gmail skipped:", e)

    try:
        meetings.extend(outlook_meetings(outlook_token))
    except Exception as e:
        print("Outlook calendar skipped:", e)

    try:
        meetings.extend(google_meetings(google_creds))
    except Exception as e:
        print("Google calendar skipped:", e)

    summary_input = {
        "emails": emails,
        "meetings": meetings
    }

    summary = summarize(str(summary_input))
    print("\n📌 DAILY EXECUTIVE BRIEF\n")
    print(summary)

if __name__ == "__main__":
    run_agent()
from googleapiclient.discovery import build

def get_unread_emails(creds):
    service = build("gmail", "v1", credentials=creds)
    results = service.users().messages().list(
        userId="me",
        q="is:unread"
    ).execute()
    return results.get("messages", [])

import requests

GRAPH_BASE = "https://graph.microsoft.com/v1.0"

def get_unread_emails(access_token):
    """
    Fetch unread Outlook emails using Microsoft Graph API.
    """
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    url = (
        f"{GRAPH_BASE}/me/mailFolders/inbox/messages"
        "?$filter=isRead eq false"
        "&$top=10"
    )

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    messages = response.json().get("value", [])

    emails = []
    for msg in messages:
        emails.append({
            "source": "outlook",
            "from": msg.get("from", {}).get("emailAddress", {}).get("address"),
            "subject": msg.get("subject"),
            "received": msg.get("receivedDateTime"),
            "body": msg.get("bodyPreview")
        })

    return emails

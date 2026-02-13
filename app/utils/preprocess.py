def normalize_email(email, source):
    return {
        "source": source,
        "sender": email.get("from", ""),
        "subject": email.get("subject", ""),
        "body": clean_text(email.get("body", "")),
        "received": email.get("receivedDateTime", "")
    }

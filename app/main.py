def daily_brief():
    emails = get_all_emails()
    meetings = get_today_meetings()

    email_summary = summarize(emails)
    calendar_summary = summarize(meetings)

    return f"""
    DAILY BRIEF
    {email_summary}
    {calendar_summary}
    """
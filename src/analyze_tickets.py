from datetime import datetime, timedelta

def analyze_tickets(df):
    now = datetime.now()

    # Tickets updated in last 24 hours
    last_24h = df[df["updated"] >= now - timedelta(hours=24)]

    # Critical tickets (Priority = High or P1)
    critical = df[df["priority"].str.contains("high|p1", case=False, na=False)]

    # Tickets not updated for > 3 days
    stale = df[df["updated"] <= now - timedelta(days=3)]

    return last_24h, critical, stale

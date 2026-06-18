import plotly.express as px
import pandas as pd

def chart_by_status(df):
    return px.bar(
        df.groupby("status").size().reset_index(name="count"),
        x="status",
        y="count",
        title="Tickets by Status",
        color="status"
    )

def chart_by_priority(df):
    return px.pie(
        df,
        names="priority",
        title="Tickets by Priority"
    )

def chart_ticket_aging(df):
    df["days_since_update"] = (pd.Timestamp.now() - df["updated"]).dt.days
    return px.histogram(
        df,
        x="days_since_update",
        nbins=10,
        title="Ticket Aging (Days Since Last Update)"
    )

def chart_last_24h(df):
    df["updated_date"] = df["updated"].dt.date
    return px.bar(
        df.groupby("updated_date").size().reset_index(name="count"),
        x="updated_date",
        y="count",
        title="Updates in Last 24 Hours"
    )

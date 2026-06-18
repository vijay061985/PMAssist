from src.ingest_excel import load_ticket_data
from src.analyze_tickets import analyze_tickets
from src.generate_summary import generate_morning_summary

df = load_ticket_data("data/tickets.xlsx")

last_24h, critical, stale = analyze_tickets(df)

email_text = generate_morning_summary(last_24h, critical, stale)

print("\n===== MORNING SUMMARY EMAIL =====\n")
print(email_text)

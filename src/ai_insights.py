from openai import OpenAI
import os

import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def generate_ai_insights(df, last_24h, critical, stale):
    prompt = f"""
You are an AI Project Manager Assistant.

Analyse the ticket dataset and produce the following insights:

1. **Risks** — items that may impact delivery, deadlines, or quality.
2. **Blockers** — items stuck, waiting on others, or not progressing.
3. **Trends** — patterns in updates, priorities, workload, or delays.
4. **Recommendations** — specific actions the PM should take today.

Use the data below:

All Tickets:
{df.to_string(index=False)}

Updated in last 24 hours:
{last_24h.to_string(index=False)}

Critical Tickets:
{critical.to_string(index=False)}

Stale Tickets (>3 days no update):
{stale.to_string(index=False)}

Provide insights in bullet points, concise, and PM‑friendly.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

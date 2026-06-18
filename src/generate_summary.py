from openai import OpenAI
import os

import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def generate_morning_summary(last_24h, critical, stale):
    prompt = f"""
You are an AI PM Assistant. Create a clear, concise morning summary email.

Include:

1. Tickets updated in last 24 hours
2. Critical tickets
3. Tickets not updated for more than 3 days

Format it professionally.

---

Tickets updated in last 24 hours:
{last_24h.to_string(index=False)}

---

Critical tickets:
{critical.to_string(index=False)}

---

Stale tickets (>3 days no update):
{stale.to_string(index=False)}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

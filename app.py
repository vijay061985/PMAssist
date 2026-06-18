import streamlit as st
import pandas as pd

from src.ingest_excel import load_ticket_data
from src.analyze_tickets import analyze_tickets
from src.generate_summary import generate_morning_summary
from src.ai_insights import generate_ai_insights
from src.charts import (
    chart_by_status,
    chart_by_priority,
    chart_ticket_aging,
    chart_last_24h,
)

st.set_page_config(page_title="AI PM Assistant", layout="wide")

st.title("📊 AI PM Assistant")
st.write("Upload your ticket Excel file, view analytics, generate summaries, and get AI-driven insights.")

uploaded_file = st.file_uploader("Upload tickets Excel file", type=["xlsx"])

if uploaded_file:
    # Show raw data
    raw_df = pd.read_excel(uploaded_file)
    st.subheader("Raw Ticket Data")
    st.dataframe(raw_df, use_container_width=True)

    # Process using ingestion logic
    df = load_ticket_data(uploaded_file)

    # Run analysis
    last_24h, critical, stale = analyze_tickets(df)

    st.subheader("Tickets Updated in Last 24 Hours")
    st.dataframe(last_24h, use_container_width=True)

    st.subheader("Critical Tickets")
    st.dataframe(critical, use_container_width=True)

    st.subheader("Stale Tickets (>3 days no update)")
    st.dataframe(stale, use_container_width=True)

    # Charts dashboard
    st.subheader("📈 Ticket Analytics Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(chart_by_status(df), use_container_width=True)

    with col2:
        st.plotly_chart(chart_by_priority(df), use_container_width=True)

    st.plotly_chart(chart_ticket_aging(df), use_container_width=True)

    if not last_24h.empty:
        st.plotly_chart(chart_last_24h(last_24h), use_container_width=True)

    # Morning summary email
    st.subheader("📧 Morning Summary Email")

    if st.button("Generate Morning Summary Email"):
        with st.spinner("Generating summary..."):
            summary = generate_morning_summary(last_24h, critical, stale)

        st.text_area("Email Content", summary, height=320)

    # AI Insights
    st.subheader("🤖 AI Insights")

    if st.button("Generate AI Insights"):
        with st.spinner("Analyzing tickets and generating insights..."):
            insights = generate_ai_insights(df, last_24h, critical, stale)

        st.text_area("AI‑Generated Insights", insights, height=350)

else:
    st.info("Please upload an Excel file to get started.")

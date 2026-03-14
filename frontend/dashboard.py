import streamlit as st
from notion_client import Client
from ai_processor import analyze_tasks
import os
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = "32374c21bc8a8009b9b2d773cf8ff40f"

notion = Client(auth=NOTION_TOKEN)

st.title("🤖 AI Productivity Dashboard")

response = notion.databases.query(database_id=DATABASE_ID)

tasks = []
for result in response["results"]:
    title_property = result["properties"]["Name"]["title"]
    if title_property:
        task_name = title_property[0]["plain_text"]
        if task_name.strip():
            tasks.append(task_name)

st.subheader("📋 Tasks from Notion")
for task in tasks:
    st.markdown(f"- {task}")

analysis = analyze_tasks(tasks)

st.subheader("⚡ Priority Order")
for item in analysis["priority_order"]:
    st.markdown(f"- {item}")

st.subheader("🛠 Generated Subtasks")
for task, subs in analysis["subtasks"].items():
    if task in tasks:
        st.markdown(f"**{task}**")
        for sub in subs:
            st.markdown(f"- {sub}")

st.subheader("📅 Daily Productivity Plan")
for item in analysis["daily_plan"]:
    st.markdown(f"- {item}")
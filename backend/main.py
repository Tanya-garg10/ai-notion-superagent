from notion_client import Client
import os
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = "32374c21bc8a8009b9b2d773cf8ff40f"

notion = Client(auth=NOTION_TOKEN)

response = notion.databases.query(database_id=DATABASE_ID)

tasks = []
for result in response["results"]:
    title_property = result["properties"]["Name"]["title"]
    if title_property:
        tasks.append(title_property[0]["plain_text"])
    else:
        tasks.append("Untitled Task")

print(tasks)
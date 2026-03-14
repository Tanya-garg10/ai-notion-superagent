# AI Workflow SuperAgent

AI Workflow SuperAgent is a simple AI-powered productivity system that connects a Notion task database with a Streamlit dashboard.

It fetches tasks directly from Notion, analyzes them using a lightweight AI workflow layer, and presents:
- task list
- priority order
- generated subtasks
- daily productivity plan

This project demonstrates how Notion can be turned into an intelligent workflow assistant.

## Features

- Fetch tasks from a Notion database
- Display tasks in a Streamlit dashboard
- Generate priority order
- Suggest subtasks for major tasks
- Create a daily productivity plan

## Project Structure

```text
AI-NOTION-SUPERAGENT
│
├── backend
│   ├── main.py
│   └── workflow_engine.py
│
├── frontend
│   ├── ai_processor.py
│   └── dashboard.py
│
├── README.md
└── requirements.txt
````

## Tech Stack

* Python
* Notion API
* Streamlit

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-notion-superagent.git
cd ai-notion-superagent
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your Notion credentials

Open `frontend/dashboard.py` and update these values:

```python
NOTION_TOKEN = "YOUR_NOTION_TOKEN"
DATABASE_ID = "YOUR_DATABASE_ID"
```

Make sure:

* your Notion integration token is valid
* your Notion database is shared with the integration

### 4. Run the app

```bash
streamlit run frontend/dashboard.py
```

## How It Works

1. Tasks are stored in a Notion database.
2. The Streamlit app fetches tasks using the Notion API.
3. The AI workflow layer analyzes the tasks.
4. The dashboard displays:

   * tasks from Notion
   * priority order
   * generated subtasks
   * daily productivity plan

## Example Tasks

* Build AI dashboard
* Apply for internships
* Finish hackathon project

## Use Case

This project is useful for students, builders, and professionals who want to convert a simple Notion task list into a smarter AI-assisted productivity workflow.

## Future Improvements

* Real LLM-based task analysis
* Task status updates back to Notion
* Deadline-aware prioritization
* Authentication and deployment support

## License

This project is for educational and demonstration purposes.

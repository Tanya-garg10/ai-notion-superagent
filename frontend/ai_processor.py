def analyze_tasks(tasks):
    priority_order = sorted(tasks, key=lambda x: len(x), reverse=True)

    subtasks = {
        "Build AI dashboard": [
            "Design UI",
            "Connect backend",
            "Test dashboard"
        ],
        "Apply for internships": [
            "Update resume",
            "Search companies",
            "Submit applications"
        ],
        "Finish hackathon project": [
            "Complete core features",
            "Prepare demo video",
            "Submit final project"
        ]
    }

    daily_plan = [
        "Work on Build AI dashboard",
        "Complete Finish hackathon project",
        "Apply to 2 internships"
    ]

    return {
        "priority_order": priority_order,
        "subtasks": subtasks,
        "daily_plan": daily_plan
    }
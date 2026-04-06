import sys
import json

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 clickup_task_export.py <task_url>")
        sys.exit(1)

    task_url = sys.argv[1]
    # Mock implementation for demonstration
    task_id = task_url.split("/")[-1]
    
    response = {
        "task_id": task_id,
        "task_name": "Finance Sensitive Task 001",
        "task_status": "In Progress",
        "task_priority": "High",
        "task_due_date": "2026-04-15",
        "task_description": "Confidential financial analysis required",
        "subtasks": [
            {
                "subtask_id": "sub-001",
                "subtask_name": "Data Collection",
                "subtask_status": "To Do",
                "subtask_due_date": "2026-04-10",
                "subtask_completed": False
            },
            {
                "subtask_id": "sub-002",
                "subtask_name": "Analysis",
                "subtask_status": "In Progress",
                "subtask_due_date": "2026-04-12",
                "subtask_completed": False
            }
        ]
    }

    print(json.dumps(response, indent=2))

if __name__ == "__main__":
    main()
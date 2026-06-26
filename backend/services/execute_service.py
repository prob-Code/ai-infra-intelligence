def execute_ai_action(action: str):

    if action == "Create Storage Alert":
        return {
            "status": "success",
            "executed": action,
            "message": "Storage alert created."
        }

    elif action == "Notify Administrator":
        return {
            "status": "success",
            "executed": action,
            "message": "Administrator notified."
        }

    elif action == "Run Disk Cleanup Task":
        return {
            "status": "success",
            "executed": action,
            "message": "Disk cleanup started."
        }

    return {
        "status": "ignored",
        "executed": action,
        "message": "Unknown action."
    }

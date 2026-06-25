from services.ai_service import run_ai_analysis


def execute_action():

    result = run_ai_analysis()

    analysis = result.get(
        "analysis",
        ""
    ).lower()

    if "provider error" in analysis:

        return {
            "actions": [
                "AI provider unavailable"
            ]
        }

    actions = []

    if "high" in analysis and "cpu" in analysis:

        actions.append(
            "Create CPU Alert"
        )

    if "disk" in analysis and "capacity" in analysis:

        actions.append(
            "Create Storage Alert"
        )

    if len(actions) == 0:

        actions.append(
            "No action required"
        )

    return {
        "actions": actions
    }

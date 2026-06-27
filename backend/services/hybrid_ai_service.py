from services.memory_service import search_similar_incident
from services.ai_service import run_ai_analysis
from services.save_event_service import save_ai_event


def hybrid_ai_engine(root_cause: str):

    # Step 1: Search previous incidents
    memory = search_similar_incident(root_cause)

    # Step 2: Return historical solution if found
    if memory["found"]:

        return {
            "source": "memory",
            "result": memory
        }

    # Step 3: Call AI
    analysis = run_ai_analysis()

    # Step 4: Save new knowledge
    save_ai_event(
        risk=analysis["risk"],
        confidence=analysis["confidence"],
        root_cause=analysis["root_cause"],
        recommendation=analysis["recommendation"],
        action=analysis["actions"][0],
        status="OPEN"
    )

    # Step 5: Return AI response
    return {
        "source": "glm",
        "result": analysis
    }

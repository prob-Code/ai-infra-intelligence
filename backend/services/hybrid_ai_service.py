memory = search_similar_incident(root_cause)

if memory["found"]:
    return memory

analysis = run_ai_analysis()

save_ai_event(...)

return analysis

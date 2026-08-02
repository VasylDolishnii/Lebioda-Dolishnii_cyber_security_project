def analyze_agents(data):
    risks = []

    agents = data.get("data", {}).get("affected_items", [])

    for a in agents:
        if a.get("status") != "active":
            risks.append({
                "level": "HIGH",
                "type": "AGENT_OFFLINE",
                "message": f"Agent DOWN: {a['name']} ({a['id']})"
            })

        if a.get("os", {}).get("platform") == "windows":
            risks.append({
                "level": "INFO",
                "type": "WINDOWS_HOST",
                "message": f"Windows host detected: {a['name']}"
            })

    return risks

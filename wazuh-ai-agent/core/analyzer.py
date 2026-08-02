def analyze_agents(data):

    risks = []

    agents = data.get("data", {}).get("affected_items", [])


    for agent in agents:

        if agent.get("status") != "active":
            risks.append({
                "level": "HIGH",
                "type": "AGENT_OFFLINE",
                "message": f"Agent DOWN: {agent['name']} ({agent['id']})"
            })


        if agent.get("os", {}).get("platform") == "windows":
            risks.append({
                "level": "INFO",
                "type": "WINDOWS_HOST",
                "message": f"Windows host detected: {agent['name']}"
            })


    return risks

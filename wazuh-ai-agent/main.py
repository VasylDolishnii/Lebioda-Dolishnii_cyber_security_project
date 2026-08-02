from services.wazuh_api import WazuhAPI
from core.analyzer import analyze_agents


def main():

    wazuh = WazuhAPI()

    data = wazuh.get_agents()

    risks = analyze_agents(data)


    print("\n🚨 SECURITY EVENTS 🚨\n")


    if not risks:
        print("No risks detected")
        return


    for risk in risks:
        print(
            f"[{risk['level']}] "
            f"{risk['type']} - "
            f"{risk['message']}"
        )


if __name__ == "__main__":
    main()

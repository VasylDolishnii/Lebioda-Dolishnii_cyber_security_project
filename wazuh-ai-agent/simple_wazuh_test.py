import os
import requests
import urllib3
import json
from dotenv import load_dotenv

from analyzer import analyze_agents
from ai_analyzer import explain_risk

urllib3.disable_warnings()
load_dotenv()

WAZUH_URL = os.getenv("WAZUH_URL")
USER = os.getenv("WAZUH_USER")
PASSWORD = os.getenv("WAZUH_PASSWORD")


def get_token():
    r = requests.post(
        f"{WAZUH_URL}/security/user/authenticate",
        auth=(USER, PASSWORD),
        verify=False
    )
    r.raise_for_status()
    print("TOKEN OK")
    return r.json()["data"]["token"]


def get_agents(token):
    headers = {"Authorization": f"Bearer {token}"}

    r = requests.get(
        f"{WAZUH_URL}/agents",
        headers=headers,
        verify=False
    )
    r.raise_for_status()
    return r.json()


def main():
    token = get_token()
    data = get_agents(token)

    risks = analyze_agents(data)

    if not risks:
        print("✅ No risks detected")
        return

    print("\n🚨 AI SOC ANALYSIS 🚨\n")

    for risk in risks:
        print("\n-----------------------")
        print(f"RAW: {risk}")

        ai_result = explain_risk(risk)

        print("\nAI ANALYSIS:")
        print(ai_result)


if __name__ == "__main__":
    main()

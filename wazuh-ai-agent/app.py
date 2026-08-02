import json
import time
import urllib3
import requests

from dotenv import load_dotenv
from openai import OpenAI
import os

urllib3.disable_warnings()

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

WAZUH_URL = os.getenv("WAZUH_URL")
WAZUH_USER = os.getenv("WAZUH_USER")
WAZUH_PASSWORD = os.getenv("WAZUH_PASSWORD")

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", 60))
MIN_ALERT_LEVEL = int(os.getenv("MIN_ALERT_LEVEL", 8))

processed = set()
token = None
token_expire = 0

def get_token():
    response = requests.post(
        f"{WAZUH_URL}/security/user/authenticate",
        auth=(WAZUH_USER, WAZUH_PASSWORD),
        verify=False,
        timeout=30
    )

    response.raise_for_status()

    return response.json()["data"]["token"]

def get_alerts(jwt_token):

    headers = {
        "Authorization": f"Bearer {jwt_token}"
    }

    response = requests.get(
        f"{WAZUH_URL}/alerts?limit=50&sort=-timestamp",
        headers=headers,
        verify=False,
        timeout=30
    )

    response.raise_for_status()

    return response.json()["data"]["affected_items"]


def is_important(alert):

    level = alert.get("rule", {}).get("level", 0)

    return level >= MIN_ALERT_LEVEL

def analyze_with_ai(alert):

    prompt = f"""
You are a SOC analyst.

Analyze this Wazuh alert.

Return:

1. Risk level (LOW/MEDIUM/HIGH/CRITICAL)
2. Short explanation
3. Recommended actions

Alert:

{json.dumps(alert, indent=2)}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.1
    )

    return response.choices[0].message.content

def send_telegram(message):

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={
            "chat_id": CHAT_ID,
            "text": message[:4000]
        },
        timeout=30
    )

while True:

    try:

        token = get_token()

        alerts = get_alerts(token)

        for alert in alerts:

            alert_id = alert.get("id")

            if not alert_id:
                continue

            if alert_id in processed:
                continue

            processed.add(alert_id)

            if not is_important(alert):
                continue

            analysis = analyze_with_ai(alert)

            message = (
                f"🚨 Wazuh Alert\n\n"
                f"Agent: {alert.get('agent', {}).get('name', 'unknown')}\n"
                f"Level: {alert.get('rule', {}).get('level')}\n"
                f"Rule: {alert.get('rule', {}).get('description')}\n\n"
                f"{analysis}"
            )

            send_telegram(message)

            print("Alert sent")

    except Exception as e:
        print(e)

    time.sleep(CHECK_INTERVAL)

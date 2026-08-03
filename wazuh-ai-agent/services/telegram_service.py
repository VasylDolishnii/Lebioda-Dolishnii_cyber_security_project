import requests
import json
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def send_telegram_alert(alert):
    """Wysyła czysty alert z Wazuha bezpośrednio na Telegram bez AI."""
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("[!] Błąd: Brak TELEGRAM_BOT_TOKEN lub TELEGRAM_CHAT_ID w .env")
        return

    rule = alert.get("rule", {})
    rule_id = rule.get("id", "N/A")
    rule_desc = rule.get("description", "Brak opisu")
    level = rule.get("level", 0)
    groups = ", ".join(rule.get("groups", []))
    
    agent = alert.get("agent", {})
    agent_name = agent.get("name", "Manager/VPS")
    agent_ip = agent.get("ip", "Lokalny")

    # Pobranie surowego logu
    full_log = alert.get("full_log", "")
    if not full_log and "data" in alert:
        full_log = json.dumps(alert["data"], indent=2)

    # Przycięcie zbyt długich logów
    if len(full_log) > 500:
        full_log = full_log[:500] + "\n... [przycięte]"

    msg = (
        f"🚨 *WAZUH ALERT (Poziom {level}/15)*\n\n"
        f"💻 *Host:* `{agent_name}` ({agent_ip})\n"
        f"📌 *Reguła:* `{rule_id}` - {rule_desc}\n"
        f"🏷 *Kategorie:* `{groups}`\n"
    )

    if full_log:
        msg += f"\n📄 *Surowy log:*\n```\n{full_log}\n```"

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": msg,
        "parse_mode": "Markdown"
    }

    try:
        res = requests.post(url, json=payload, timeout=5)
        if res.status_code == 200:
            print(f"[+] [Poziom {level}] Alert wysłany na Telegram: {rule_desc}")
        else:
            print(f"[!] Błąd Telegrama API ({res.status_code}): {res.text}")
    except Exception as e:
        print(f"[!] Błąd połączenia z Telegramem: {e}")

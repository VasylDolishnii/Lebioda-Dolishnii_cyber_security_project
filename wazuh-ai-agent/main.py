import asyncio
import json
import os

from config import WAZUH_ALERTS_FILE, MIN_ALERT_LEVEL
from services.telegram_service import TelegramService
from core.storage import is_new_event


async def main():
    telegram = TelegramService()
    print("🚀 SOC Agent uruchomiony!")
    print(f"👀 Nasłuchuję nowych alertów z {WAZUH_ALERTS_FILE}...")

    try:
        with open(WAZUH_ALERTS_FILE, "r") as f:
            # Przechodzimy na sam koniec pliku (przetwarzamy tylko nowe alerty)
            f.seek(0, os.SEEK_END)

            while True:
                line = f.readline()
                if not line:
                    await asyncio.sleep(0.5)  # Asynchroniczny czas na pojawienie się nowych logów
                    continue

                try:
                    alert = json.loads(line)
                    rule = alert.get("rule", {})
                    level = rule.get("level", 0)

                    # Filtrujemy tylko ważne alerty (np. >= 10)
                    if level >= MIN_ALERT_LEVEL:
                        agent_name = alert.get("agent", {}).get("name", "Manager/VPS")
                        rule_desc = rule.get("description", "Brak opisu")
                        rule_id = rule.get("id", "N/A")

                        # Przygotowujemy obiekt ryzyka do sprawdzenia deduplikacji
                        risk_event = {
                            "id": f"{rule_id}_{alert.get('id', '')}",
                            "level": level,
                            "type": rule_desc,
                            "agent": agent_name
                        }

                        # Jeśli alert był już wysłany -> pomijamy
                        if not is_new_event(risk_event):
                            print(f"[-] Duplikat pominięty: {rule_desc}")
                            continue

                        # Formatujemy treść wiadomości
                        message = (
                            f"🚨 *WAZUH ALERT (Poziom {level}/15)*\n\n"
                            f"💻 *Host:* `{agent_name}`\n"
                            f"📌 *Reguła:* `{rule_id}` - {rule_desc}\n"
                        )

                        full_log = alert.get("full_log", "")
                        if full_log:
                            if len(full_log) > 400:
                                full_log = full_log[:400] + "... [przycięte]"
                            message += f"\n📄 *Log:*\n```\n{full_log}\n```"

                        print(f"[+] Nowy alert (Poziom {level}): {rule_desc}")
                        
                        # Wysyłamy wiadomość na Telegram
                        await telegram.send_message(message)

                except json.JSONDecodeError:
                    continue
                except Exception as e:
                    print(f"[!] Błąd przetwarzania linii: {e}")

    except FileNotFoundError:
        print(f"[ERROR] Nie znaleziono pliku {WAZUH_ALERTS_FILE}.")
        print("Upewnij się, że uruchamiasz skrypt z prawami sudo na VPS!")


if __name__ == "__main__":
    asyncio.run(main())

import json
import os


FILE = "logs/events.json"


def load_events():

    if not os.path.exists(FILE):
        return []

    with open(FILE, "r") as f:
        return json.load(f)



def save_events(events):

    with open(FILE, "w") as f:
        json.dump(events, f, indent=4)



def is_new_event(event):

    events = load_events()

    event_id = (
        event["type"],
        event["message"]
    )


    for old in events:
        old_id = (
            old["type"],
            old["message"]
        )

        if event_id == old_id:
            return False


    events.append(event)

    save_events(events)

    return True

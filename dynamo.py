import json
import os
from datetime import datetime, timedelta

DATA_FILE = "data/locks.json"

def load_locks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def get_stale_locks():
    """Return locks not checked in the last 30 days."""
    try:
        locks = load_locks()
        cutoff = datetime.utcnow() - timedelta(days=30)

        stale = []
        for lock in locks:
            last_checked = datetime.fromisoformat(lock["last_checked"])
            if last_checked < cutoff:
                stale.append(lock)

        return stale

    except Exception as e:
        print("Error reading local lock data:", e)
        return []

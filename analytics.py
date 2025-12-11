import json
import os
from datetime import datetime

SENT_LOG = "data/sent_notifications.json"
CLICK_LOG = "data/click_logs.json"


# --------------------------
# Saving SENT notifications
# --------------------------
def log_sent_notification(lock_id, campaign_id):
    entry = {
        "lock_id": lock_id,
        "campaign_id": campaign_id,
        "timestamp": datetime.utcnow().isoformat()
    }

    _append_json(SENT_LOG, entry)
    print(f"Logged SENT notification for {lock_id}")


# --------------------------
# Logging user CLICKS
# --------------------------
def log_click(lock_id, campaign_id):
    entry = {
        "lock_id": lock_id,
        "campaign_id": campaign_id,
        "timestamp": datetime.utcnow().isoformat()
    }

    _append_json(CLICK_LOG, entry)
    print(f"Logged CLICK for {lock_id}")


# --------------------------
# INTERNAL HELPER
# --------------------------
def _append_json(path, obj):
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump([obj], f, indent=4)
        return

    with open(path, "r") as f:
        data = json.load(f)

    data.append(obj)

    with open(path, "w") as f:
        json.dump(data, f, indent=4)


# --------------------------
# Campaign SUMMARY
# --------------------------
def campaign_summary(campaign_id):
    sent = _load_all(SENT_LOG)
    clicks = _load_all(CLICK_LOG)

    sent_count = sum(1 for e in sent if e["campaign_id"] == campaign_id)
    click_count = sum(1 for e in clicks if e["campaign_id"] == campaign_id)

    if sent_count == 0:
        ctr = 0
    else:
        ctr = round((click_count / sent_count) * 100, 2)

    print("\n🔍 Campaign Summary")
    print("-------------------------")
    print(f"Campaign ID: {campaign_id}")
    print(f"Notifications Sent: {sent_count}")
    print(f"Clicks: {click_count}")
    print(f"CTR: {ctr}%")

    return {
        "sent": sent_count,
        "clicks": click_count,
        "ctr": ctr
    }


def _load_all(path):
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return json.load(f)


# --------------------------
# CLI MODE
# --------------------------
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage:")
        print(" python -m src.analytics click <lock_id> <campaign_id>")
        print(" python -m src.analytics summary <campaign_id>")
        sys.exit()

    command = sys.argv[1]

    if command == "click":
        lock = sys.argv[2]
        camp = sys.argv[3]
        log_click(lock, camp)

    elif command == "summary":
        camp = sys.argv[2]
        campaign_summary(camp)

    else:
        print("Unknown command")

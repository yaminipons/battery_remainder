import uuid
from src.dynamo import get_stale_locks
from src.analytics import log_sent_notification

def send_fcm_notification(lock):
    # Mocking FCM — just print
    print(f"Sending FCM notification to lock {lock['lock_id']}")
    return True


def main():
    print("Starting weekly battery reminder job...")

    campaign_id = str(uuid.uuid4())
    print("Campaign ID:", campaign_id)

    stale_locks = get_stale_locks()
    print(f"Found {len(stale_locks)} stale locks.")

    for lock in stale_locks:
        print(f"Processing the lock id {lock['lock_id']}...")
        ok = send_fcm_notification(lock)
        if ok:
            log_sent_notification(lock["lock_id"], campaign_id)

    print("Job complete.")


if __name__ == "__main__":
    main()

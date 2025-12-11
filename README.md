🔋 Battery Reminder Automation

A simple Python-based automation system that sends weekly battery reminders for IoT smart locks.
This project scans for locks that haven’t checked in recently and sends notification triggers.

📌 Features

Weekly job that checks for stale locks (inactive for X days)

Auto-generates unique campaign IDs

Logs and prints notifications sent

Fully standalone, no AWS, no external services

Clean and modular Python structure

📂 Project Structure
battery_remainder/
│
├── src/
│   ├── main.py                
│   ├── analytics.py            
│   ├── __init__.py               
│   └── dynamo.py               
|
├── data/
│   ├── locks.json              
│   ├── sent_notifications.json      
│   └── click_logs.json            
│
└── README.md

🚀 **How It Works**

main.py starts the weekly reminder job

Loads lock data from locks.json

Identifies locks inactive for > 7 days

Creates a campaign

Sends simulated notifications

Logs:

sent notifications

user click events

campaign performance

▶️ **Running the Project**
1. Activate venv
.\venv\Scripts\activate

2. Run main job
python -m src.main

3. Output Example
Starting weekly battery reminder job...
Campaign ID: 0f2e4d50-6adf-4512-ba2a-a4dd59f89abe
Found 3 stale locks.
Sent notification to LOCK#23
Sent notification to LOCK#78
Sent notification to LOCK#91
Job complete.

**Click Tracking**

The system supports simple click analytics.
To simulate a click:
python -m src.analytics click <lock_id> <campaign_id>
All clicks are saved in data/clicks.json.
Campaign summary:
python -m src.analytics summary <campaign_id>

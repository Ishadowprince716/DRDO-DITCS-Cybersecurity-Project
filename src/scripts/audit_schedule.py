# audit_schedule.py

import schedule
import time
from modules.audit_management.audit_runner import run_audit

def job():
    print("Running scheduled audit...")
    run_audit()

schedule.every().day.at("01:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)

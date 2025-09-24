# app/tasks.py
import time
import logging

logging.basicConfig(level=logging.INFO)

def send_email(recipient: str):
    print(f"Sending email to {recipient}...")
    time.sleep(5)  # Simulate delay
    print(f"Email sent to {recipient}")



def send_email(recipient: str):
    logging.info(f"📧 Sending email to {recipient}...")
    # Simulate delay or actual logic
    logging.info(f"✅ Email sent to {recipient}")
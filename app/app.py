# app/app.py
import time
import logging
import random
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
    handlers=[logging.FileHandler("/fluentbit/logs/app.log")]
)

users = ["alice", "bob", "charlie", "diana"]
actions = ["login", "logout", "view_page", "click_button", "submit_form"]

def generate_log():
    user = random.choice(users)
    action = random.choice(actions)
    logging.info(f"User '{user}' performed '{action}' action.")

while True:
    generate_log()
    time.sleep(random.randint(2, 5))

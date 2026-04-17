import os
from dotenv import load_dotenv

load_dotenv()
USERNAME = os.getenv("ORANGE_USER")
PASSWORD = os.getenv("ORANGE_PASS")

CREDENTIALS = [
    ("some_username", "pass", "fail"),
    ("Admin", "wrong_pass", "fail"),
    ("idk", "just_password", "fail"),
    ("adilkhan", "my_pass", "fail"),
    (USERNAME, PASSWORD, "success")
]
from database import insert_into_notes
from datetime import datetime

with open("input.txt", "r") as f:
    data = f.read()

dt = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")

insert_into_notes(data, dt)

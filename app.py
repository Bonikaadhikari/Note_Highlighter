from database import insert_into_notes, insert_into_keywords
from datetime import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file", type=str, help="Enter the name of file")
parser.add_argument("--keywords", type=str, help="Enter keywords to search for")

args = parser.parse_args()
with open(args.file, "r") as f:
    data = f.read()

dt = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")

keyword_id = insert_into_keywords(args.keywords)
insert_into_notes(data, dt, keyword_id)


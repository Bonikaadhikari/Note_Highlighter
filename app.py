from database import insert_into_notes, insert_into_keywords, retrieve_keyword_and_notes
from datetime import datetime
import argparse
import sys

# import nltk
# nltk.download('punkt_tab')
from nltk.tokenize import sent_tokenize

parser = argparse.ArgumentParser()
parser.add_argument("--file", type=str, help="Enter the name of file")
parser.add_argument("--keywords", type=str, help="Enter keywords to search for")
parser.add_argument(
    "--list", help="List the available keywords and notes", action="store_true"
)

args = parser.parse_args()
if args.list:
    data = retrieve_keyword_and_notes()
    print("-" * 100)
    for keyword, note in data:
        print(keyword)
        print(note)
        print("-" * 100)

else:
    if not args.file:
        print("No files found")
        sys.exit()
    with open(args.file, "r") as f:
        data = f.read()
        sentences = sent_tokenize(data)
        for sentence in sentences:
            if args.keywords.lower() in sentence.lower():
                print(sentence)
            elif not args.keywords.lower():
                print("Empty keywords")
            else:
                print("No matching keywords in the sentence")

        dt = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
        keyword_id = insert_into_keywords(args.keywords)
        insert_into_notes(data, dt, keyword_id)

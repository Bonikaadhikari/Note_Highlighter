# Note Highlighter

A simple Python + PostgreSQL project that highlights sentences containing specific keywords from a text file. Useful for text analysis, summaries, and keyword-based content filtering.
## Features

- Reads .txt files and splits content into sentences
- Stores notes and keywords in PostgreSQL
- Searches for matching sentences containing keywords
- Command-line interface with options to process, list, and view results


## Setup
1. **Install Dependencies** 
```python
pip install psycopg2-binary nltk 
```
2. **Download NLTK Data (once)**
```python
import nltk
nltk.download('punkt_tab')
```
3. **Set Up PostgreSQL Database**
```
Create a PostgreSQL database and ensure your database.py connects correctly. 
```

## Usage
- Insert and Highlight Sentences from a File
``` 
python app.py --file sample.txt --keywords python
```
- List All Keywords and Notes
```
python main.py --list
```

## Example
**If sample.txt contains:**
<i>Python is great for scripting. SQL is used for data. I love using both!</i><br>
**And you run:** 
<i>python main.py --file sample.txt --keywords python</i><br>
**You'll get:**
<i>Python is great for scripting.</i>


## To-Do
- Handle multiple keywords
- Export highlights to a file
- Prevent duplicate keyword inserts


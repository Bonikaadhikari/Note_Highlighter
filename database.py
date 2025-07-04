import psycopg2


def create_db_connection():
    try:
        conn = psycopg2.connect(
            dbname="nh_db",
            user="postgres",
            password="mypassword",
            host="localhost",
            port=5432,
        )
        return conn
    except Exception as e:
        print("Error: ", str(e))


def create_tables():
    conn = create_db_connection()
    cur = conn.cursor()
    query1 = """ CREATE TABLE IF NOT EXISTS Keywords(
                Id SERIAL PRIMARY KEY,
                Word TEXT)"""
    cur.execute(query1)
    query2 = """ CREATE TABLE IF NOT EXISTS Notes(
            Id SERIAL PRIMARY KEY,
            Content TEXT,
            date_added TIMESTAMP,
            keywords_id INT references Keywords(Id))"""

    cur.execute(query2)
    conn.commit()
    cur.close()
    conn.close()


def insert_into_notes(data, time, keyword_id):
    conn = create_db_connection()
    cur = conn.cursor()
    insert_query = f""" INSERT INTO Notes (
                    content, 
                    date_added, keywords_id)
                    VALUES ('{data}', '{time}', {keyword_id})"""
    cur.execute(insert_query)
    conn.commit()
    cur.close()
    conn.close()


def insert_into_keywords(keywords):
    conn = create_db_connection()
    cur = conn.cursor()
    insert_query = (
        f""" INSERT INTO keywords (Word) VALUES ('{keywords}') RETURNING Id"""
    )
    cur.execute(insert_query)
    keywords_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return keywords_id


def retrieve_keyword_and_notes():
    conn = create_db_connection()
    cur = conn.cursor()
    retrieve_query = f"""SELECT k.Word, n.content from keywords k
                        INNER JOIN Notes n on n.keywords_id = k.id"""
    cur.execute(retrieve_query)
    rows = cur.fetchall()
    # conn.commit()
    cur.close()
    conn.close()
    return rows

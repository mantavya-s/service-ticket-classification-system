import psycopg2
import os
from dotenv import load_dotenv
from psycopg2.extras import RealDictCursor

load_dotenv()

def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

def get_all_tickets():
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)

        cur.execute("""
        SELECT * FROM tickets
        ORDER BY created_at DESC;
        """)

        return cur.fetchall()

    except Exception as e:
        if conn:
            conn.rollback()

        print("Failed to get tickets: ")
        print(e)
        raise

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

def get_specific_ticket(ticket_id: str):
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)

        cur.execute("""
        SELECT * FROM tickets
        WHERE ticket_id = %s;
        """, 
        (ticket_id,),
        )

        return cur.fetchone()

    except Exception as e:
        if conn:
            conn.rollback()

        print("Failed to get ticket: ")
        print(e)
        raise

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
    
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

def update_data(
    ticket_id: str, confirmed_category: str
) -> bool:
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
        UPDATE tickets
        SET
            confirmed_category = %s,
            reviewed_at = CURRENT_TIMESTAMP
        WHERE
            ticket_id = %s
        """, (
            confirmed_category, 
            ticket_id,
        ),
        )

        ticket_found = cur.rowcount > 0

        conn.commit()

        return ticket_found

    except Exception as e:
        if conn:
            conn.rollback()

        print("Failed to review ticket: ")
        print(e)
        raise

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
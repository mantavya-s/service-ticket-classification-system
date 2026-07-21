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

def insert_data(
    ticket_id: str, subcategory: str, priority: str,
    description: str | None, predicted_category: str, predicted_confidence: float 
) -> None:
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
        INSERT INTO tickets(
        ticket_id, subcategory, priority,
        description, predicted_category,
        predicted_confidence
        )
        VALUES(%s, %s, %s, %s, %s, %s)
        ON CONFLICT (ticket_id) DO UPDATE SET
            subcategory = EXCLUDED.subcategory,
            priority = EXCLUDED.priority,
            description = EXCLUDED.description,
            predicted_category = EXCLUDED.predicted_category,
            predicted_confidence = EXCLUDED.predicted_confidence
        """, (
            ticket_id, subcategory, priority,
            description, predicted_category, predicted_confidence
        ))

        conn.commit()

    except Exception as e:
        if conn:
            conn.rollback()

        print("Failed to insert ticket: ")
        print(e)
        raise

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
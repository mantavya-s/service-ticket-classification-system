import psycopg2
import os
from dotenv import load_dotenv
from psycopg2.extras import RealDictCursor
import pandas as pd

load_dotenv()

def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )


def retrain_model():
    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT COUNT(*)
            FROM tickets
            WHERE confirmed_category IS NOT NULL
                AND used_for_training IS FALSE
            """)

        count = cur.fetchone()[0]

        if count >= 5:
            cur.execute("""
            SELECT 
                ticket_id AS "Ticket ID", 
                confirmed_category AS "Category", 
                subcategory AS "Subcategory", 
                priority AS "Priority", 
                description AS "Description", 
                source AS "Source"
            FROM tickets
            WHERE confirmed_category IS NOT NULL
                AND used_for_training IS FALSE
            """)

            rows = cur.fetchall()
            ticket_ids = [row[0] for row in rows]
            columns = [desc[0] for desc in cur.description]

            new_data = pd.DataFrame(rows, columns=columns)
            synthetic_data = pd.read_csv("data/synthetic_tickets.csv")
            synthetic_data = pd.concat(
                [synthetic_data, new_data],
                ignore_index=True
            )
            synthetic_data.to_csv("data/synthetic_tickets.csv", index=False)

            cur.execute("""
            UPDATE tickets
            SET used_for_training = TRUE
            WHERE ticket_id = ANY(%s)
            """, (ticket_ids,))

            conn.commit()
            
    except Exception as e:
        if conn:
            conn.rollback()

        print("Failed to connect to database: ")
        print(e)
        raise

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    retrain_model()
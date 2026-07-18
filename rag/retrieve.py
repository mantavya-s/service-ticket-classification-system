from sentence_transformers import SentenceTransformer
import psycopg2
import os
from dotenv import load_dotenv
from pgvector.psycopg2 import register_vector

load_dotenv()

def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

test = input("Subcategory + Description: ")

model = SentenceTransformer(MODEL_NAME)
embedding = model.encode(test, normalize_embeddings=True)

cur = None 
conn = None

try:
    conn = get_connection()
    register_vector(conn)
    cur = conn.cursor()

    cur.execute("""
    SELECT 
        file_name, 
        category, 
        subcategory, 
        section,
        chunk_text,
        embedding <=> %s AS distance
    FROM knowledge_vdb
    WHERE section = 'Troubleshooting Steps'
    ORDER BY distance
    LIMIT 3;
    """, (embedding,))

    rows = cur.fetchall()
    for row in rows:
        print(row)
    
except Exception as e:
    print("Connection failed:")
    print(e)

finally:
    if cur:
        cur.close()
    if conn:
        conn.close()




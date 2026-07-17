# things to do:
# create an object that looks like: chunk_id, file_name, title, category, section, chunk_text, embedding
# Use sentence transformer MiniLM to convert the documents in knowledge base to chunks
# loop through each file and convert each section in the file to a chunk_id
# Use regex to identify sections (split by section headings)
# Create an embedding per section
# store the embedding plus all the aforementioned data together

from pathlib import Path 
import re
from sentence_transformers import SentenceTransformer 

KNOW_BASE_DIR = Path("knowledge_base")

# function to replace delimiters in a string with underscores. 
def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9]", "_", text.lower()).strip("_")

# function to find and return the title (recognized by a piece of text with a leading #)
def get_title(file: str, file_path: Path) -> str:
    title_pattern = r"^#\s+(.+)$"
    title = re.search(title_pattern, file, re.MULTILINE)

    if title:
        return title.group(1).strip()
    return file_path.stem.replace("_", " ").title()

# function to find other sections in the file
def get_section(file: str, section_name: str) -> str:
    section_pattern = rf"^##\s+{re.escape(section_name)}\s*$\n(.*?)(?=~##\s+|\Z)"
    section = re.search(section_pattern, file, re.MULTILINE | re.DOTALL)

    if section:
        return section.group(1).strip()
    return ""

# function to create chunks of the file by each section and create metadata which will be stored with teh embedding
def chunk_file(file_path: Path) -> list[dict]:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    
    title = get_title(content, file_path)
    category = get_section(content, "Category")
    subcategory = get_section(content, "Subcategory")
    sections = ["Symptoms", "Likely Causes", "Troubleshooting Steps", "Escalation Notes", "Suggested Ticket Comment"]

    chunks = []

    for i, section in enumerate(sections):
        section_text = get_section(content, section)

        if not section_text:
            continue

        chunk_id = f"{file_path.stem()}__{normalize(title)}__{i}"

        embedding_text = f""""
            Title: {title}
            Category: {category}
            Subcategory: {subcategory}
            Section: {section}

            {section_text}
        """.strip()
        
        chunks.append({
            "chunk_id": chunk_id,
            "file_name": file_path.name,
            "file_path": str(file_path),
            "title": title,
            "category": category,
            "subcategory": subcategory,
            "section": section,
            "chunk_index": i,
            "chunk_text": section_text,
            "embedding_text": embedding_text
        })

    return chunks

# Function to iterate over all files in the knowledge base and create chunks
def  build_all_chunks() -> list[dict]:
    all_chunks = []

    for file_path in KNOW_BASE_DIR.glob("*.md"):
        file_chunks = chunk_file(file_path)
        all_chunks.extend(file_chunks)

    return all_chunks




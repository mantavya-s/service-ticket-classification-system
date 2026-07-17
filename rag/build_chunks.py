# things to do:
# create an object that looks like: chunk_id, file_name, title, category, section, chunk_text, embedding
# Use sentence transformer MiniLM to convert the documents in knowledge base to chunks
# loop through each file and convert each section in the file to a chunk_id
# Use regex to identify sections (split by section headings)
# Create an embedding per section
# store the embedding plus all the aforementioned data together

from pathlib import Path 
import re

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
    return ""


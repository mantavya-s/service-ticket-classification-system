#!/bin/bash

FILE1="public_it_tickets.csv"
FILE2="synthetic_tickets.csv"
OUTPUT_FILE="combined_ticket.csv"

head -n 1 "$FILE1" > "$OUTPUT_FILE"
tail -n +2 "$FILE1" >> "$OUTPUT_FILE"
tail -n +2 "$FILE2" >> "$OUTPUT_FILE"
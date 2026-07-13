import re
import pandas as pd

df = pd.read_csv("synthetic_tickets.csv")
df = df.drop(columns=['Price','Stock'])
df.to_csv("synthetic_tickets.csv", index=False)
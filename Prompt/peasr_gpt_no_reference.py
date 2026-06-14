# -*- coding: utf-8 -*-

import csv
from openai import OpenAI

CSV_PATH = ""

API_KEY = "" # needs to set API_KEY, connecting via OpenAI's API
MODEL = "gpt-4.1-mini-2025-04-14" # which model is supposed to be in use

client = OpenAI(api_key=API_KEY)


with open(CSV_PATH, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)

for i, row in enumerate(rows):
  english_text = row[0].strip() # text to be corrected


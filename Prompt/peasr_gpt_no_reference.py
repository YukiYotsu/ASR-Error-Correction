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
        
        prompt = (f"""
                    You are performing post-editing for an ASR transcript of an academic presentation.
        
                    Your task is ONLY to correct clear ASR recognition errors.
        
                    IMPORTANT RULES:
        
                    - Preserve the original wording and phrasing whenever possible.
                    - Do NOT paraphrase, rewrite, summarize, or improve fluency.
                    - Prefer the ASR transcript whenever both versions are plausible.
                    - Only make minimal local edits for obvious ASR mistakes.
                    - Do not introduce new content not present in the ASR transcript.
                    - If the transcript is already plausible, keep it unchanged.
        
                    Return ONLY the post-edited ASR transcript.
        
                    ASR transcript:
                    {english_text}
                    """
                    )
                    
                    response = client.responses.create(
                        model=MODEL,
                        input=prompt,
                        temperature=0.0,
                    )

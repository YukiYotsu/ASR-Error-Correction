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

  slide_index = row[3].strip() # corresponds the tagged slide's number
  slide_image = ""
  if slide_index.isdigit():
      slide_num = int(slide_index)
      slide_file = f"{paper_tag}-Scene-{slide_num:03d}.jpg"
      slide_image = os.path.join(slides_dir, slide_file)

  encoded_images_list = [] #基本1個しか画像はないが、拡張性のため配列にしておいた。
  if os.path.exists(slide_image):
      if slide_image.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
          try:
              encoded_images_list.append(
                  encode_image(slide_image)
              )
          except Exception as e:
              print(f"❌ Failed image {slide_image}: {e}")
  else:
      print(f"⚠ Image directory not found: {slide_image}")

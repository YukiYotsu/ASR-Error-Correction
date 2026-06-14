# -*- coding: utf-8 -*-

import csv
from openai import OpenAI
import base64

CSV_PATH = ""

API_KEY = "" # needs to set API_KEY, connecting via OpenAI's API
MODEL = "gpt-4.1-mini-2025-04-14" # which model is supposed to be in use

client = OpenAI(api_key=API_KEY)

# -----------------------------
# 画像エンコード（Base64方式）
# -----------------------------
def encode_image(image_path: str) -> str:
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

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

  try:
        prompt = (f"""
            You are performing post-editing for an ASR transcript of an academic presentation.
        
            You are also given the corresponding presentation slide.
                      
            Your task is ONLY to correct clear ASR recognition errors.
        
            IMPORTANT RULES:
        
            - Preserve the original wording and phrasing whenever possible.
            - Do NOT paraphrase, rewrite, summarize, or improve fluency.
            - Do NOT replace sentences with slide text.
            - The spoken presentation may differ from the slide.
            - Prefer the ASR transcript whenever both versions are plausible.
            - Only make minimal local edits for obvious ASR mistakes.
            - Do not introduce new content not present in the ASR transcript.
            - If the transcript is already plausible, keep it unchanged.
        
            Return ONLY the post-edited ASR transcript.
        
            ASR transcript:
            {english_text}
            """
            )
        
            final_content = []
            
            # 1. 画像を1つ追加
            if encoded_images_list: #もしリストが空でなければ
                for b64 in encoded_images_list:
                    final_content.append({
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{b64}",
                    })
                    print(f"Using slide: {slide_image}")
            
            else: #もしリストが空であれば
                print(f"⚠ Using slide: No Slides")


            # 2. プロンプトを追加
            final_content.append({
                "type": "input_text",
                "text": prompt,
            })

            messages = [{
                "role": "user",
                "content": final_content
            }]

            response = client.responses.create(
                model=MODEL,
                input=messages,
                temperature=0.0,
            )

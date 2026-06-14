# -*- coding: utf-8 -*-

import csv
from openai import OpenAI
import base64 # 画像Base64方式エンコード用

CSV_PATH = ""
RESOURCE_PATH = f"{BASE_DIR}/{paper_tag}_raw_commanded.txt"
IMAGE_DIR_PATH = f"{BASE_DIR}/人手抽出写真/{paper_tag}"

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

# -----------------------------
# 📄 論文テキスト読み込み
# -----------------------------
with open(resource_path, "r", encoding="utf-8") as f:
    text = f.read()
    print(f"{resource_path}のテキストの長さは{text.__len__()}です")

# -----------------------------
# 🖼️ 画像読み込み
# -----------------------------
encoded_images_list = []
if os.path.exists(IMAGE_DIR_PATH):
    for filename in os.listdir(IMAGE_DIR_PATH):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
            try:
                encoded_images_list.append(
                    encode_image(os.path.join(IMAGE_DIR_PATH, filename))
                )
            except Exception as e:
                print(f"❌ Failed image {filename}: {e}")
else:
    print(f"⚠ Image directory not found: {IMAGE_DIR_PATH}")
      
for i, row in enumerate(rows):

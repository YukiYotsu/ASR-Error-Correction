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

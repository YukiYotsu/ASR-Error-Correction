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

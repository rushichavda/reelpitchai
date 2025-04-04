import openai

def summarize_slide_texts(slides):
    narrations = []
    for text in slides:
        prompt = f"Convert this slide into a 2-sentence narration:\n{text}"
        res = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        narrations.append(res['choices'][0]['message']['content'])
    return narrations

import pandas as pd
import ollama

df = pd.read_csv("refined.csv")

ollama_model = "phi3:mini"

def generate_response(text, explain, level="6th grade"):

    explain_text = "Simply explain all medical terminology" if explain else "Avoid all medical terminology"

    prompt = f"""
    Rewrite the medical discharge instructions below into plain language a {level}r can understand.

    Strict rules:
    - Use short sentences. Maximum 15 words per sentence.
    - Write one idea per sentence.
    - {explain_text}
    - Do NOT add extra information, stories, or feelings.
    - Do NOT summarize or restate.
    - Use a kind, friendly tone.
    - Output only the rewritten instructions, starting with "Rewrite:".
    - Do not add introductions, conclusions, or extra commentary.
    - Limit output to 100 words maximum.
    - Do not use numbered or bulleted lists.
    - Each sentence should be separated by a line break.

    Examples:

    Patient to follow up with cardiology for echocardiogram to evaluate LV function.
    Goes to
    See your heart doctor soon.
    They will check how well your heart works.

    Continue lisinopril 10mg PO daily. Start furosemide 40mg PO BID for fluid retention.
    Writes as
    Keep taking 10mg of lisinopril once a day.
    Take 40mg of furosemide twice daily.

    Follow a low sodium diet and avoid processed foods.
    Also is
    Eat less salt.
    Avoid packaged or salty foods.

    Take acetaminophen 500mg every 6 hours as needed for pain.
    Goes to
    Take 500mg of acetaminophen every 6 hours if you feel pain.

    Now rewrite this:

    """

    model_response = ollama.chat(
        model=ollama_model,
        messages = [{
            "role": "user",
            "content": prompt + text
        }]
    )

    return model_response.message.content

# test_res = generate_response(df.iloc[0]["note"])
# print(test_res)

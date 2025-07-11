from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

MODEL = "llama-3.3-70b-versatile"
REQUEST_URL = "https://9fdd348e5927.ngrok-free.app"
API_KEY = os.getenv("API_KEY")

client = Groq(api_key=API_KEY)

def generate_response(text, explain, word_count, level="6th grade"):

    explain_text = "Simply explain all medical terminology including medicine needed, and their purpose" if explain else "Avoid all medical terminology"

    prompt = f"""
    Rewrite the medical discharge instructions below into plain language a {level} could understand.

    Strict rules:
    - {explain_text}
    - Do NOT add extra information.
    - Do NOT summarize or restate.
    - Use a kind, friendly tone.
    - Output only the rewritten instructions, without "Rewrite:".
    - Do not add introductions, conclusions, or extra commentary.
    - Have output be exactly, or around, {word_count} words.
    - Do not use numbered or bulleted lists

    Examples (Modify so that a {level} could understand):

    Patient to follow up with cardiology for echocardiogram to evaluate LV function.
    Goes to
    See your heart doctor soon, they will check how well your heart works.

    Continue lisinopril 10mg PO daily. Start furosemide 40mg PO BID for fluid retention.
    Writes as
    Keep taking 10mg of lisinopril once a day and take 40mg of furosemide twice daily.

    Follow a low sodium diet and avoid processed foods.
    Also is
    Eat less salt and avoid packaged or salty foods.

    Take acetaminophen 500mg every 6 hours as needed for pain.
    Goes to
    Take 500mg of acetaminophen every 6 hours if you feel pain.

    Now rewrite this:

    """

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=MODEL,
    )

    return chat_completion.choices[0].message.content
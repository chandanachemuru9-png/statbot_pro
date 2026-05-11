from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_agent(question, csv_summary):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a data analyst AI called StatBot Pro. "
                        "You ONLY answer questions about the CSV data provided. "
                        "If the question is not related to the data, reply with: "
                        "'I can only answer questions about the uploaded CSV data. "
                        "Please ask something related to the data.' "
                        "Do not answer general knowledge questions."
                    )
                },
                {
                    "role": "user",
                    "content": (
                        f"Here is the CSV data summary:\n{csv_summary}\n\n"
                        f"User Question: {question}\n\n"
                        "Give a clear, simple answer."
                    )
                }
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


client = Groq(api_key=os.getenv("GROQ_API_KEY"))
def summarize_paper(text):

    prompt = f"""
    Analyze the following research paper and respond in this format:

    Summary:
    (3-4 sentences)

    Key Contributions:
    - point 1
    - point 2
    - point 3

    Methodology:
    Explain the method used.

    Simple Explanation:
    Explain it for beginners.

    Research Paper:
    {text[:2000]}
    """

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.1-8b-instant"
    )

    return response.choices[0].message.content


def ask_question(text, question):

    prompt = f"""
    You are an AI research assistant.

    Answer the question based ONLY on the research paper below.

    Research Paper:
    {text[:2000]}

    Question:
    {question}
    """

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.1-8b-instant"
    )

    return response.choices[0].message.content
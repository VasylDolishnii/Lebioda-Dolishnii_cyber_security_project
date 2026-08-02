import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def explain_risk(risk):
    prompt = f"""
You are a SOC analyst.

Analyze this security event:

TYPE: {risk['type']}
LEVEL: {risk['level']}
MESSAGE: {risk['message']}

Return STRICT JSON only:
{{
  "severity": "low|medium|high|critical",
  "explanation": "...",
  "recommendation": "..."
}}
"""

    resp = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a cybersecurity SOC analyst."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return resp.choices[0].message.content

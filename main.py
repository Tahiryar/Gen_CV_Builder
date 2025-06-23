import pandas as pd
import google.generativeai as genai
import os

genai.configure(api_key="API_Key")

data = {
    'Name': ['Tahir', 'Ali', 'Zara'],
    'Skills': ['Python, GenAI', 'Java, SQL', 'React, ML'],
    'Experience': ['2 years in dev', '1 year backend', 'Intern in AI']
}

df = pd.DataFrame(data)

model = genai.GenerativeModel('gemini-1.5-flash')

summaries = []

for index, row in df.iterrows():
    prompt = f"""You are a CV assistant. Write a 3-line professional summary for:

Name: {row['Name']}
Skills: {row['Skills']}
Experience: {row['Experience']}"""

    print(f"\n🔹 Prompt for {row['Name']}:\n{prompt}")
    print(" Generating summary...")

    response = model.generate_content(prompt)
    summary = response.text.strip()
    print(f" Summary for {row['Name']}:\n{summary}")
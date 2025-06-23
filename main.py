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
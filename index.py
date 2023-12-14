
from dotenv import load_dotenv
import os
import argparse
import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
load_dotenv()
GOOGLE_API_KEY = os.getenv('API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')
question=""
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))



def get_Response(question):
    response = model.generate_content(question)
    return response.text


while True:
    try:
        question=input("Write your Prompt here :")
        print(get_Response(question))
    except Exception as e:
        print(f'{type(e).__name__}: {e}')

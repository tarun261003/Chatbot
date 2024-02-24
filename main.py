import google.generativeai as genai
import config 
import textwrap

def to_markdown(text):
  text = text.replace('•', '  *')
  return textwrap.indent(text, '', predicate=lambda _: True)
if __name__=="__main__":
  genai.configure(api_key=config.api)
  model = genai.GenerativeModel('gemini-pro')
  text=model.generate_content('write a python program to print "helloworld" ')
  k=to_markdown(text.text)
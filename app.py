from flask import Flask,render_template,request
from main import to_markdown
import google.generativeai as genai
#pip install -q -U google-generativeai
import config 

app=Flask(__name__,template_folder='./templates')

@app.route('/',methods=['POST','GET'])
def home():
    if request.method=='POST':
        chat=request.form['chat']
        print(chat)
        t=model.generate_content(chat)
        s=to_markdown(t.text)
        return render_template('index.html',data=(chat,s))
    return render_template('index.html')
if __name__=="__main__":
    genai.configure(api_key=config.api)
    model = genai.GenerativeModel('gemini-pro')
    app.run(debug=True)
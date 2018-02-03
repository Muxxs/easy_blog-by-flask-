#coding=utf-8
from flask import Flask,render_template
app = Flask(__name__)
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import uniout
def get_text():
    content=open("text.txt")
    content=str(content.read())
    content_list=content.split("=====*=====")
    text=[]
    for i in content_list:
        title=i.split("===*")[0].split("***")[-2]
        content=i.split("===*")[1]
        content_title=title,content
        text.append(content_title)
    return text
all_content=get_text()
print all_content[0]
@app.route('/page/<int:text_number>')
def show_text(text_number):
    global all_content
    print text_number
    title=str(all_content[text_number][0])
    content=all_content[text_number][1]
    return render_template('main.html', title=title,content=content)

def hello_world():
    return 'Hello World!'

app.run(host='0.0.0.0')
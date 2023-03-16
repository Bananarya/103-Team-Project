'''
gptwebapp shows how to create a web app which ask the user for a prompt
and then sends it to openai's GPT API to get a response. You can use this
as your own GPT interface and not have to go through openai's web pages.

We assume that the APIKEY has been put into the shell environment.
Run this server as follows:

On Mac
% pip3 install openai
% pip3 install flask
% export APIKEY="......."  # in bash
% python3 gptwebapp.py

On Windows:
% pip install openai
% pip install flask
% $env:APIKEY="....." # in powershell
% python gptwebapp.py
'''
from flask import request,redirect,url_for,Flask
from gpt import GPT
import os
import random

app = Flask(__name__)
gptAPI = GPT(os.environ.get('APIKEY'))


# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q789789uioujkkljkl...8z\n\xec]/'

@app.route('/')
def index():
    ''' display a link to the general query page '''
    print('processing / route')
    return f'''
        <h1>GPT Demo</h1>
        <a href="{url_for('gptdemo')}">Ask questions to GPT</a>
        <a href="{url_for('CCgpt')}">Caesar Cipher GPT</a>
    '''


def CC(str, key):
    ans = ''
    for i in str:
        if (i != ' '):
            convert = ord(i) + key
            if convert > 122:
                convert = convert - 58
            if convert < 65:
                convert = convert + 58
            ans = ans + chr(convert)
        else:
            ans = ans + ' ' 
    return ans


@app.route('/Caesar-Cipher-gpt', methods = ['GET', 'POST'])
def CCgpt():
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getResponse(prompt)
        key = random.randint(1,26)
        return f'''
        <h1>Caesar Cipher GPT</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Caesar Cipher text:
        <div style="border:thin solid black">{CC(answer,key)}</div>
        <hr>
        <h1>Translate</h1>
        <div style="border:thin solid black">{answer}</div>
        <hr>
        <a href={url_for('CCgpt')}> make another query</a>
        <a href={url_for('index')}> home page </a>
        '''
    else:
        return '''
        <h1>Caesar Cipher GPT</h1>
        Enter your query below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit name="response" value="get response">
        </form>
        '''



@app.route('/gptdemo', methods=['GET', 'POST'])
def gptdemo():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getResponse(prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('gptdemo')}> make another query</a>
        '''
    else:
        return '''
        <h1>GPT Demo App</h1>
        Enter your query below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''

if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)

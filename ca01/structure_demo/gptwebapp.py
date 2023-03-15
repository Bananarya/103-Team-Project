# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 08:18:41 2023

@author: Bananarya
"""
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

app = Flask(__name__)
gptAPI = GPT(os.environ.get('APIKEY'))

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q789789uioujkkljkl...8z\n\xec]/'

@app.route('/')
def index():
    ''' display a link to the general query page '''
    print('processing / route')
    return f'''
        <h1>Index Page</h1>
        <a href="{url_for('gptdemorongzi')}">Ask questions to Rongzi's GPT</a> <br />
        <a href="{url_for('about')}">Go to the about page</a> <br />
        <a href="{url_for('team')}">Go to the team page</a> <br />
        <a href="{url_for('index')}">Back to the index page</a> <br />
    '''


@app.route('/gptdemorongzi', methods=['GET', 'POST'])
def gptdemorongzi():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        #happyn = request.form['happynumber']
        #answer = gptAPI.getResponse(prompt)
        answer1=gptAPI.getifhappy(prompt)
        return f'''
        <h1>Rongzi's FormPage</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in happynumber mode:
        <div style="border:thin solid black">{answer1}</div>
        <a href={url_for('gptdemorongzi')}> make another query</a><br />
        <a href="{url_for('index')}">Back to the index page</a> 
        '''
    else:
        return f'''
        <h1>Rongzi's FormPage</h1>
        Enter a number below, I'll help you determine if this number is happy!>v<'
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        <a href="{url_for('index')}">Back to the index page</a> <br />
        '''
@app.route('/about')
def about():
    return '''
    <h1>Index Page</h1>
    <h2> Rongzi Xie </h1>
    My program determine if the input number is a happy number. A happy number is defined based on if the summation of the dquare of each digits can finally becomes 1 <br />
    For example:<br />
    13-->1^2+3^2=10<br />
    10-->1^2+0=1<br />
    13 is a happy number<br />
    Here is the link to it: 
    '''+f'''<a href="{url_for('gptdemorongzi')}">Go to Rongzi's chatgpt to check if a number is happy</a><br />
    <a href="{url_for('index')}">Back to the index page</a> '''

@app.route('/team')
def team():
    return f'''
    <h1>Team Page</h1>
    <h2> Rongzi Xie </h2>
    Hi, My name is Rongzi Xie. I'm a Junior who major in CS and Applied Math. I'm also an Office Assistant in the department, so welcome to come by and say hi when I'm in the office. <br />
    I'm responsible for the getifhappy method and also the demo of a structure<br />
    <a href="{url_for('index')}">Back to the index page</a> 
    '''


    
if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)
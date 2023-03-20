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
        <h1>Index Page</h1>
        <a href="{url_for('gptdemorongzi')}">Ask questions to Rongzi's GPT</a> <br />
        <a href="{url_for('CCgpt')}">Ask questions to James's GPT</a> <br />
        <a href="{url_for('gptdemokeer')}">Ask questions to Keer's GPT</a> <br />
        <a href="{url_for('gptdemoliulu')}">Ask questions to Liulu's GPT</a> <br />
        <a href="{url_for('about')}">Go to the about page</a> <br />
        <a href="{url_for('team')}">Go to the team page</a> <br />
        <a href="{url_for('index')}">Back to the index page</a> <br />
    '''



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
        <div style="border:thin solid black">{gptAPI.CC(answer,key)}</div>
        <hr>
        <h1>Translate</h1>
        <div style="border:thin solid black">{answer}</div>
        <hr>
        <a href={url_for('CCgpt')}> make another query</a>
        <a href={url_for('index')}> home page </a>
        '''
    else:
        return f'''
        <h1>Caesar Cipher GPT</h1>
        Enter your query below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit name="response" value="get response">
        </form>
        <a href={url_for('index')}> home page </a>  
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
    
@app.route('/gptdemoliulu', methods=['GET', 'POST'])
def gptdemoliulu():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer1=gptAPI.getProductTable(prompt)
        return f'''
        <h1>Liulu's FormPage</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is your product table:
        <div style="border:thin solid black">{answer1}</div> 
        <a href={url_for('gptdemoliulu')}> make another query</a><br />
        <a href="{url_for('index')}">Back to the index page</a>
        '''
    else:
        return f'''
        <h1>Liulu's FormPage</h1>
        Enter two numbers below, I will produce a product table for you.
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        <a href="{url_for('index')}">Back to the index page</a> <br />
        '''
    
@app.route('/gptdemokeer', methods=['GET', 'POST'])
def gptdemokeer():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer1=gptAPI.isPalindrome(prompt)
        return f'''
        <h1>Keer's FormPage</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer to check whether the input word is a palindrome:
        <div style="border:thin solid black">{answer1}</div>
        <a href={url_for('gptdemokeer')}> make another query</a><br />
        <a href="{url_for('index')}">Back to the index page</a>  
        '''
    else:
        return f'''
        <h1>Keer's FormPage</h1>
        Enter a word, I will tell you whether that word is a palindrome or not.
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
    <a href="{url_for('index')}">Back to the index page</a> 
    
    <h2> James Ma </h2>
    The website create a chatGPT answer encrypted in Caesar Cipher. The key is randomly generated and the translation is provided. <br>
    Here is the link to it: 
    '''+f'''<a href="{url_for('CCgpt')}">Caesar Cipher GPT for encrypted answer</a><br />

    <h2> Keer Xu </h2>
    I created a webpage to check whether an input word is palindrome or not. A palindrome is defined as a word or phrase that is exactly the same
    reading from the front or back. </br>
    For example: racecar and madam are palindrome but dog or cat are not palindrome. <br />
    '''+f'''<a href="{url_for('gptdemokeer')}">A web page to tell you whether a word is palindrome</a><br />

    <h2> Liulu Yue </h2>
    I created a webpage to produce product table with user specified lower and upper bound. <br />
    Entering two numbers separated by a space, the webpage will produce a product table with multipliers being all integers between the two entered numbers. </br>
    Here is the link to it:
    '''+f'''<a href="{url_for('gptdemoliulu')}">A web page to generate product table</a><br />
    <a href="{url_for('index')}">Back to the index page</a> 
    
    
    '''



@app.route('/team')
def team():
    return f'''
    <h1>Team Page</h1>
    <h2> Rongzi Xie </h2>
    Hi, My name is Rongzi Xie. I'm a Junior who major in CS and Applied Math. I'm also an Office Assistant in the department, so welcome to come by and say hi when I'm in the office. <br />
    I'm responsible for the getifhappy method and also the demo of this project<br />
    <h3> James Ma </h3>
    I am James Ma. I am a Junior majoring in CS and Math. I am also an Office Assistant in the department. I am TAing for 12 and 121 as well.  I coded the Caeser Cipher ChatGPT which returns encrypted answers. <br>
    <h2> Keer Xu </h2>
    I am Keer Xu, a junior student major in computer science and Applied Math. I am interested in Frontend Development and NLP (natural language processing).<br />
    I am the contributor of isPalindrome() method which helps you check whether a word is palindrome or not. 
    <br>
    <h2> Liulu Yue </h2>
    Hi, this is Liulu Yue, a junior majoring in Computer Science and Applied Mathematics. I'm interested in Artificial Intelligence and NLP. I'm responsible for the webpage that can help the user to produce a product table.
    <br>
    <a href="{url_for('index')}">Back to the index page</a> 
    '''


    
if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)

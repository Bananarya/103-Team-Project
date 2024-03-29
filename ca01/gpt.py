# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 08:15:17 2023

@author: Bananarya
"""
'''
Demo code for interacting with GPT-3 in Python.

To run this you need to 
* first visit openai.com and get an APIkey, 
* which you export into the environment as shown in the shell code below.
* next create a folder and put this file in the folder as gpt.py
* finally run the following commands in that folder

On Mac
% pip3 install openai
% export APIKEY="......."  # in bash
% python3 gpt.py

On Windows:
% pip install openai
% $env:APIKEY="....." # in powershell
% python gpt.py
'''
import openai


class GPT():
    ''' make queries to gpt from a given API '''
    def __init__(self,apikey):
        ''' store the apikey in an instance variable '''
        self.apikey=apikey
        # Set up the OpenAI API client
        openai.api_key = apikey #os.environ.get('APIKEY')

        # Set up the model and prompt
        self.model_engine = "text-davinci-003"

    def getResponse(self,prompt):
        ''' Generate a GPT response '''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response
    def CC(self,str, key):
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
    def getifhappy(self,specialn):
        '''Get if the input number is a happy number'''
        seen = set()
        n=specialn
        while n != 1:
            n = sum(int(i) ** 2 for i in str(n))
            if n in seen:
                return "This nummber is not a happy number, so sad"
            seen.add(n)
        return "This number is a happy number, yeah!"
    
    def isPalindrome(self, word):
        '''Check if the input word is palindrome'''
        char_list = [char for char in word]
        for i in range(len(char_list)//2):
            if char_list[i] != char_list[len(char_list)-i-1]:
                return "This input word is not a palindrome."
        return "Great! the input word is a palindrome!"
    
    def getProductTable(self,prompt):
        '''Show product table'''
        input = prompt.split()
        result = ""
        for i in range(int(input[0]),int(input[1])+1):
            for j in range(int(input[0]),int(input[1])+1):
                result += str(i)+"*"+str(j)+"="+str(i*j)+"\t"
            result += "<br />"
        return result

if __name__=='__main__':
    '''
    '''
    import os
    g = GPT(os.environ.get("APIKEY"))
    print(g.getResponse("what does openai's GPT stand for?"))

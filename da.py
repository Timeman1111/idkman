import os
import openai
from colorama import Fore
import json
import time
from datetime import datetime
openai.api_key = "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"
textpath = "log.txt"

def readtext():
  f = open(textpath,'r')
  return f.readlines()

def writetext(text):
  f = open(textpath,'a')
  f.write(text)
  f.close()
  return
def currenttime():
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  return current_time
lines = readtext()
configpath = "config.json"
def readjson(file):
  f = open(file,'r')
  data = json.load(f)
  f.close()
  return data
def writejson(data,file):
  f = open(file,'w')
  json.dump(data,f)
  f.close()
def clear():
    os.system('clear')
settings = readjson(configpath)
clear()
def getinfo(prompt):

    response = openai.Completion.create(
        
        model="text-davinci-002",
        prompt=prompt,
        max_tokens=settings["max_tokens"],
        temperature=settings["temperature"]
    )
    text = response["choices"]
    text1 = list(text)
    text2 = text1[0]
    text3 =text2["text"]
    text =  text3.strip("\n")
    fin = text
    string = fin
    print(Fore.BLUE + string)
    writetext(f"\n[{currenttime()}]RESPONSE: " + string + "\n")



while True:
    userinput = input(Fore.RED + "DAVINCI > ")
    if userinput == 'clear':
        clear()
        continue

    if userinput == 'exit':
        exit()
        continue

    if userinput == 'readlog':
      lines = readtext()
      for i in lines:
        print(i)
        time.sleep(0.05)
      continue

    if userinput == 'temperature':
        data = readjson(configpath)
        temp = data["temperature"]
        print(f"Current Temperature {temp}")
        edit = input("Edit Current Temperature: \n[y/n] > ")
        if 'y' in edit:
            userinput = input("ENTER NEW TEMPERATURE: ")
            data["temperature"] = float(userinput)
            writejson(data,configpath)
            clear()
            settings = readjson(configpath)
            continue

        if 'n' in edit:
            clear()
            continue



    if userinput == 'max_tokens':
        data = readjson(configpath)
        max_token = data["max_tokens"]
        clear()
        print(f"Current max_tokens: {max_token}")

        edit = input("Edit Current Max Tokens: \n[y/n] > ")
        edit = edit.lower()
        if 'y' in edit:
            userinput = input("ENTER NEW TOKENS: ")
            data["max_tokens"] = int(userinput)
            writejson(data,configpath)
            clear()
            settings = readjson(configpath)
            continue
        if 'n' in edit:
            clear()
            continue
        continue
    writetext(f"\n\n[{currenttime()}]YOU: "+userinput)
    getinfo(userinput)

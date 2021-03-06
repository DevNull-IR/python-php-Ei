# Version : 1.1
# Coded by https://github.com/DevNull-IR


import requests
from pathlib import Path
import socket
import json

def echo(value) : 
    print(value)

def print_r(**value) :
    print(value)

def file_put_contents(FileName:str,Value:str = None) : 
    if (Value == None):
        open(FileName, "w")
    
    else :
        f = open(FileName, "w")
        f.write(Value)
        f.close()
    
def substr(str,offset,end = None) :
    return str[offset:end]

def strlen(value = None) :
    return len(value)

def file_exists(file:str) : 
    if Path(file).is_file():
        return 'true'
    else :
        return 'false'

def unlink(file:str) : 
    if Path(file).is_file():
        Path(file).unlink()
        return 'true'
    else :
        return 'false'

def readfile(n:str):
    return open(n,"r").read()

def fopen(filename:str,mode:str):
    return open(filename,mode)

def fwrite(m,txt:str):
    m.write(txt)

def fclose(m):
    m.close()
    
def json_encode(data,flag=None):
    if flag==448:
        return json.dumps(data,indent=4)
    else:
        return json.dumps(data)

def json_decode(data):
    return json.loads(data)

def gethostbyname(url:str):
    return socket.gethostbyname(url)

def gethostbynamel(url:str):
    return socket.gethostbyname_ex(url)

def gethostname(url:str):
    return socket.gethostname(url)

def gethostbyaddr(url:str):
    return socket.gethostbyaddr(url)

def getprotobyname(url:str):
    return socket.getprotobyname(url)

def getservbyport(num:int,url:str):
    return socket.getservbyport(num,url)

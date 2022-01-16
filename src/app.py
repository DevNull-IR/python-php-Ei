# soon Code's
import requests
from pathlib import Path

def echo(value) : 
    print(value)

def print_r(**value) :
    print(value)

def file_put_contents(FileName,Value = None) : 
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

def file_exists(file) : 
    if Path(file).is_file():
        return 'true'
    else :
        return 'false'

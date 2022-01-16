# soon Code's
import requests

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
    
file_put_contents('test.py','sdsd')

from .passlib import *

def pass(list,path):
    a=on_pass(list)
    a.pass_all(path)
    a,b,c=return_pass(list)

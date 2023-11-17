'''
This model is an inside model.
You can not use the model.
'''
#################################################################################
#########################HELLO EVERYONE!########################################
###################################################################################


import sys
import os
#import re
#import jieba as jb
import numpy as np
import random as r

def read_txt(path):
    with open(path,"r+") as f:
        sth=f.readlines()
    return sth

class on_pass():
    def __init__(self,things):
        pass
    def num_on_pass(path):
        things=str(things)
        s =things
        num=[]
        for a in s:
            if int(a) in range(0,9):
               num.append(a)
            else:
                sys.exit()
                raise ValueError(f"things must be all int")
        x=r.randint(0,9)
        out=[]
        for a in num:
            a+=x
            if a>=10:
                a=a-10
                out.append(a)
                pass
            else:
                out.append(a)
        with open(path,"w+") as f:
            f.write(out,"/nx+",x)
        return out
        pass
    def alp_on_pass(path):
        things=str(things)
        s =things
        alp=[]
        for a in s:
            if str(a) in (np.arange(97,123) or np.arange(65,91)):
               alp.append(a)
            else:
                sys.exit()
                raise ValueError(f"things must be all atr")
        x=r.randint(0,25)
        out=[]
        sml=np.arange(97,123)
        sml.extend(np.arange(97,123))
        big=np.arange(65,91)
        big.extend(np.arange(65,91))
        for a in alp:
            vale=alp.index(a)
            vale+=x
            if a in sml:
                a=sml[vale]
                out.append(a)
                pass
            elif a in big:
                a=big[vale]
                out.append(a)
        with open(path,"w+") as f:
            f.write(out,"/nx+",x)
        return out
        pass
    def pass_all(path):
        things=str(things)
        s =things
        all=[]
        for a in s:
            if str(a) in (np.arange(97,123) or np.arange(65,91)):
               all.append(a)
            elif int(a) in range(0,9):
               all.append(a)
            else:
                sys.exit()
                raise ValueError(f"things must be numbers or letters")
        xp=r.randint(0,25)
        xn=r.randint(0,9)
        out=[]
        sml=np.arange(97,123)
        sml.extend(np.arange(97,123))
        big=np.arange(65,91)
        big.extend(np.arange(65,91))
        num=range(0,9)
        num.extend(range(0,9))
        for a in all:
            vale=all.index(a)
            vale+=x
            if a in sml:
                a=sml[vale]
                out.append(a)
            elif a in big:
                a=big[vale]
                out.append(a)
            elif a in num:
                a=num[vale]
                out.append(a)
        with open(path,"w+") as f:
            f.write(out,"/nx+",x)
        return out
        pass
def return_pass(list):
    '''
    things=str(things)
    s =things
    all=[]
    for a in s:
        if str(a) in (np.arange(97,123) or np.arange(65,91)):
           all.append(a)
        elif int(a) in range(0,9):
           all.append(a)
        else:
            sys.exit()
            raise ValueError(f"things must be numbers or letters")
    '''
    xp=r.randint(0,25)
    xn=r.randint(0,9)
    out=[]
    sml=np.arange(97,123)
    sml.extend(np.arange(97,123))
    big=np.arange(65,91)
    big.extend(np.arange(65,91))
    num=range(0,9)
    num.extend(range(0,9))
    for a in list:
        vale=list.index(a)
        vale+=x
        if a in sml:
            a=sml[vale]
            out.append(a)
        elif a in big:
            a=big[vale]
            out.append(a)
        elif a in num:
            a=num[vale]
            out.append(a)
    '''
    with open(path,"w+") as f:
        f.write(out,"/nx+",x)
    '''
    waynum="x+",xn
    wayalp="x+",xp
    return out,waynum,wayalp
    pass
        



import os
import time
import random
res=''
def lcalc(n1,n2):
    global name1,name2,result
    if len(n1) < 1 or len(n2)<1:
        result=':('
        return result
    name1,name2=n1,n2
    if n1==n2:
        result=100
        return result
    else:
        r=random.randint(1,10)
        ln1=len(n1)
        ln2=len(n2)
        sum=ln1+ln2
        lsum(sum)
def lsum(sum):
    global result
    if sum > 20:
        while sum>=20:
            sum-=3
        result =sum*5
    elif sum<= 10:
        while sum<=10:
            sum+=3
        result=sum*5
    else:
        result=sum*5
    lfinal(result)

def lfinal(result):
    global res
    if name1[0]==name2[0]:
        result+=result//21
    else:
        try:
            if name1[5]==name2[5]:
                result+=result//19
            elif name1[3]==name2[7]:
                result+=result//17
        except:
            result+=result/23
    if result>70:
        if result==99:
            result-=random.randint(0,3)
        result=str(int(result))
        result+=':)'
    else:
        result=str(int(result))
        result+=':('

    res=result
    return res



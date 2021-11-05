"""
>>>>>>>>>>>>>>>>>BEHOLD THE SCRIPT<<<<<<<<<<<<<<<<<

"""
data=''
def write(n1,n2):
    f=open('data.txt','a+')
    data=n1+'--__--'+n2+'\n'
    f.write(data)
    f.close()

def read():
    global data
    f=open('data.txt','r')
    data=f.readlines()
    f.close()
    return data

def cod403():
    f=open('data.txt','r+')
    f.truncate(0)
    f.close()
    return 'Done'

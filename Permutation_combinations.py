def fac(x):
    if(x==1):
        return 1
    else:
        return x*fac(x-1)
def percom(n,r) :
    p=(fac(n)//fac(n-r)) 
    print(p) 
    c=(fac(n)//(fac(r)*fac(n-r))) 
    print(c) 
n=int(input()) 
r=int(input()) 
percom(n,r) 

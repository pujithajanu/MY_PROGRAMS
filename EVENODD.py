def evenodd(n);
    if(n&1==0):
        return 0
    else:
        return 1
n=int(input("enter:"))
p=evenodd(n)
if(p==0):
    print("even")
else:
    print("odd")

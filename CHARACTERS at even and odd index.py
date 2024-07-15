#CHARACTERS at even and odd index
st=input()
print("entered string:",st)
a=''
b=''
for i,ch in enumerate(st):
    if(i%2==0):
        a=a+ch
    else:
        b=b+ch
print('characters at even index:',a)
print('characters at odd index:',b)

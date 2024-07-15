#MERGE characters oftwo strings
a=input()
b=input()
if(len(a)>len(b)):
    l=len(a)
else:
    l=len(b)
c=''
for i in range(l):
    c=c+a[i]+b[i]
print(c)

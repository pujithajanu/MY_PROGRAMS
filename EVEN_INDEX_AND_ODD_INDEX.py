#print the characters at even index and odd index
st=input()
n=len(st)
print('characters of even index:')
for i in range(,n,2):
    print(st[i],end='')
print('charaters at odd index:')
for i in range(1,n,2):
    print(st[i],end='')

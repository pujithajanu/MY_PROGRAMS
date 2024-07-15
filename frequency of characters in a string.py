#frequency of characters in a string
st=input('enter string:')
ch=input('enter character:')
a=0
for i in st:
    if(i==ch):
        a+=1
print('frequency of',ch,'in',st,'is',a)

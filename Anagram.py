#Using sorted() 
a=sorted(input()) 
b=sorted(input()) 
if(a==b):
    print('Anagram')
else:
    print('not')

#Using sort() 
a=list(input()) 
b=list(input()) 
a.sort() 
b.sort() 
if(a==b) :
    print('Anagram') 
else:
    print('Not') 

#Vowel counter in a string
st=input()
a=0
for i in st:
    if i in ['a','i','e','o','u','A','E','I','O','U']:
        a+=1
print('no of vowels in',st,'is',a)

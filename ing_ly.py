#add the string 'ing' at the end of the given string if the length is more than 3.if the given string already exists then add 'ly'
str1=input()
if(len(str1)>3):
    if(str1[-1]=='g' and str1[-2]=='n' and str1[-3]=='i'):
        print(str1+'ly')
    else:
        print(str1+'ing')
else:
    print(str1)

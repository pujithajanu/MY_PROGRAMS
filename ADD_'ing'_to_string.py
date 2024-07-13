#12.ADD 'ing' to string if length>3 and if string ends with 'ing' add 'ly' and if string length <3 leave it unchanged
str1=input()
if(len(str1))>3:
    if(str1[-1]=='g' and str1[-2]=='n' and str1[-3]=='i'):
        print(str1+'ly')
    else:
        print(str1+'ing')
else:
    print(str1) 
year=int(input()) 
if(year//100!=0 or year//400==0):
    if(year//4==0) :
        print('leap year') 
    else:
        print('not')
else:
    print ('not') 

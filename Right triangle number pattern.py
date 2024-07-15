#Right triangle number pattern
a=1
for i in range(5):
    
    for j in range(5):
        if(j<5-i-1):
            print(' ',end='\t')
        else:
            print(a,end='\t')
            a=a+1
   
    print('\n')

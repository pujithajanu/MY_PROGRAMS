#HALD DIAMOND STAR PROBLEM

for i in range(5):
    for j in range(5):
        if(j<5-i-1):
            print(' ',end='\t')
        else:
            print('*',end='\t')
    print('\n',end='')
for i in range(5):
    for j in range(5):
        if(j>i+0):
            print('*',end='\t')
        else:
            print(' ',end='\t')
    print('\n',end='')

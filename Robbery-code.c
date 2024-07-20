n=int(input()) 
Li=list(map(int, input())) 
sum=0
for I in range(0, n) :
    for j in range(I+2, n) :
        if((Li[I]+Li[j]) >sum) :
            sum=Li[I]+Li[j]
print(sum) 

def factors(n):
    li=[]
    for i in range(1,n+1):
        if(n%i==0):
            li.append(i)
    
    return li
n=int(input())
print(factors(n))

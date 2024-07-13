#5.NO OF PRIMES
def Prime(n):
    for i in range(1,n+1):
        count=0
        for j in range(1,i+1):
            if(i%j==0):
                count=count+1
        if(count==2):
            print(i,"is Prime")
n=int(input())
Prime(n)
#4.sum of n
def sumcal(n):
    s=0
    for i in range(1,n+1):
        s=s+i
    return s
n=int(input())
print(sumcal(n))

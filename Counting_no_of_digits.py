#with recursion
n=int(input()) 
count=0
if(n>0) :
    while(n!=0) :
        count+=1
        n=n//10
print(count)  

#with recursion
def recur(n):
    if(n<10):
        return 1
    else:
        return 1+recur(n//10)        
n=int(input()) 
print(recur(n)) 
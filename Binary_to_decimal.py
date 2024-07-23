#without using predefined function
n=int(input()) 
st=''
while(n!=0) :
    st=st+str(n%2) 
    n//2
print(st[::-1]) 

#Using predefined function
n=int(input()) 
print(bin(n) [2:]) 

#using reversed function
n=input()
n=''.join(reversed(n))
n=int(n)
print(n)
#without using reversed function
n=input()
rev=n[::-1]
print(rev)

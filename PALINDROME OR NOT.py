#PALINDROME OR NOT
st=input()
if(st[::1]==st[::-1]):
    print("yes palindrome")
else:
    print("not a palindrome")

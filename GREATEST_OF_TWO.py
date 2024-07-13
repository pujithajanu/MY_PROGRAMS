#1.GREATEST OF TWO NUMBERS
def greatest(a,b):
    c=abs(a-b)
    return (a+b+c)//2
a=int(input("enter:"))
b=int(input("enter:"))
print(greatest(a,b))
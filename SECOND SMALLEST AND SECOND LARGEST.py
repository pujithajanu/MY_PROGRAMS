#SECOND SMALLEST AND SECOND LARGEST
a=input("Enter a list of numbers seperated by spaces:")
a=a.split()
a=list(map(int,a))
a=sorted(a)
print('second smallest:', a[1] ,',second largest:',a[-2])

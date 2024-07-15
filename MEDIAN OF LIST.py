#MEDIAN OF LIST
ST=input("enter a list of numbers by dividing them with spaces:")
ST=ST.split()
ST=list(map(int,ST))
ST=sorted(ST)
a=(len(ST))
print('median of entered list of numbers is',ST[a//2])

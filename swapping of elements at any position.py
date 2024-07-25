#swapping of elements at any position
li=list(input().split()) #since elements in the console entered with spaces for seperating elements in the list,so for eliminating spaces we used split()
#read positions of elements to be swapped
p,q=map(int,input().split())
sw=li[p]
li[p]=li[q]
li[q]=sw
print(li)

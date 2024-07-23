def is_perfect_square (n):
    if(n<0):
        return 0
    else:
        for i in range(1,n//2+1):
            if(i*i==n):
                return 1
    return 0
n=int(input())
print('True') if is_perfect_square(n) else print ('False')

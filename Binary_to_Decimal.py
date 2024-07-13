#14.Binary_to_Decimal
inp=int(input("enter binary values:"))
i=0
decimal=0
while(inp>0):
    p=inp%10
    power=2**i
    decimal=decimal+(p*power)
    inp=inp//10
    i=i+1
print("decimal value:",decimal)
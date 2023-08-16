#Functions
def increment(a: int):
    a = int(a*1.03)
    print(a)
    rem = a%10
    if rem == 0:
        return a
    else:
        return a+(10-rem)
        
try:
    while True:
        inp = int(input("Present Value: "))
        print(increment(inp))
        
except:
    print("Error has occured")
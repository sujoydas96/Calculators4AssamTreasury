
inp = 0
rem = 0

try:
    while True:
        inp = int(input("Present Value: "))
        ans = int(inp*1.03)
        rem = ans%10

        if rem != 0:
            rem = 10-rem
            print(ans+rem)
        else:
            print(ans)
except:
    print("Error has occured")


    
    

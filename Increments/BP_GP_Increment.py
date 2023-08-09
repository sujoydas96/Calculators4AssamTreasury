BP = 0
GP = 0
Tot_old = 0
Tot_new = 0


while True:
    BP = int(input("BP: "))
    GP = int(input("GP: "))

    Tot_old = BP + GP
    print("Total Pay Old : ",Tot_old)

    Tot_new = Tot_old*1.03
    print("Total Pay New : ",Tot_new)
    
    print("New Basic Pay: ",Tot_new-GP)
    print("___________________________________________________")



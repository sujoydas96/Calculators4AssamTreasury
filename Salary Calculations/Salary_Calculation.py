#Dependencies
import os
import math

#Global Variables
sal_type = ""
eGrade = 0  #employee Grade
TotalPay = 0
DearA = 0
HouseR = 0
Gross = 0
Net = 0
GIS = 0
GPF = 0
PTax = 208
Ded = 0
NPS = 0
custom = 0


def GIS_calculator(level:int):
    tmp = 0
    if level == 1:
        tmp = 400
    elif level == 2:
        tmp = 300
    elif level == 3:
        tmp = 200
    elif level == 4:
        tmp = 100
    else:
        tmp = 400
    
    if sal_type == 'y' or sal_type == "Y":
        return int(tmp*0.3)
    else:
        return tmp

def deductions(t:int,tp:int,da:int):

    if type == 1:    #NPS
        NPS = int(round(0.1*(tp+da),0))
        return NPS+GIS+PTax
    elif type == 2:  #GPF
        print("Minimum Limits of GPF                        : ",round(tp*0.0625))
        print("Maximum Limits of GPF                        : ",round(tp*0.156))
        GPF_con = int(input("Enter the GPF Deduction Amount(Contribution) :  "))
        GPF_ref = int(input("Enter the GPF Deduction Amount(Refund)       :  "))
        GPF = GPF_con + GPF_ref
        print("Total GPF : ",GPF)
        return GPF+GIS+PTax
    elif type == 3:   #custom deductions
        custom = int(input('Enter the total deduction : '))
        return custom
    else:
        return 0  #no deductions

os.system("cls")
DA = int(input("Enter the DA percentage for the month                                          : "))
HRA = int(input("Enter the HRA percentage for the month                                         : "))
eGrade = int(input("Enter the Grade of the Employee(1,2,3,4)                                       : "))
sal_type = str(input("Provisional Salary? (Y/N)                                                      : "))
type = int(input("Enter the Type of Deduction (NPS-1, GPF-2, Custom Deduction-3, No Deduction-4) : "))
MA = int(input("Enter the Medical Allowance for the month                                      : "))
os.system("cls")

try:
    while True:
        print("\n## ALLOWANCES ##")
        print("_____________________________________________________________________________________")

        BP = int(input("Enter Pay            : "))
        GP = int(input("Enter Grade Pay      : "))
    
        # All Calculations
        print("\n")

        TotalPay = BP+GP
        DearA = int(round((DA/100)*TotalPay))
        HouseR = int(round((HRA/100)*TotalPay))
        Gross = TotalPay+DearA+HouseR+MA
        NPS = int(round(0.1*(TotalPay+DearA),0))
        GIS = GIS_calculator(eGrade)
        Ded = round(deductions(type,TotalPay,DearA))

        print("________________________________")
        print("Basic Pay           : ",BP)
        print("Grade Pay           : ",GP)
        print("Total Pay           : ",TotalPay)

        print("\nDearness Allowance  : ", DearA)
        print("House Rent Allowance: ", HouseR)
        print("Medical Allowance   : ", MA)

        print("________________________________")
        print("Gross Salary        : ",Gross)
        print("________________________________")

        print("\n\n")
        print("\n## DEDUCTIONS ##")
        print("_____________________________________________________________________________________")

        if type == 1:
            print("NPS Contribution    : ",NPS)
        elif type == 2:
            print("GPF Contribution    : ",GPF)
        elif type == 2:
            print("Custom Deduction    : ",custom)
        else:
            pass
        
        print("GIS                 : ",GIS)
        print("Professional Tax    : ",PTax)

        print("________________________________")
        print("Total Deduction     : ",Ded)
        print("In-hand Salary        : ",Gross-Ded)
        print("________________________________")

        print("\n\n")

        os.system("pause")
        os.system("cls")

except:
    print("An error has occured!")

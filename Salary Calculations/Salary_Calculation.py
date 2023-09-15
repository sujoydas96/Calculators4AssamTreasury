#ISSUES
#All calculations have to be rounded. Eg. NPS is to be rounded to its nearest whole number.
#Calculation of GIS, Medical Allowances, Professional Taxes needs to be implemented
#A small introduction and explanation of the program is to appear on the CLI so that users can understand the operations of the program. 

#Calculation for Provitional salary. In Provisional salary, Gis is 30% for each Grade. eg. for Grade4 it will be 30, for grade3 it will be 60.
#if more than 25000 gross than ptax is 208 otherwise 150
#GIS  for G4 is 100, g3 is 200, g2 is 300 and g4 is 400
#For Provisional Salary, the GIS is 30% of the actual value mentioned above.


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
PTax = 208
Ded = 0
NPS = 0
prov_flag = 0


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
        print("Minimum Limits of GPF                    : ",tp*0.0625)
        print("Maximum Limits of GPF                      : ",tp*0.156)
        GPF_con = int(input("Enter the GPF Deduction Amount(Contribution) : "))
        GPF_ref = int(input("Enter the GPF Deduction Amount(Refund)      : "))
        GPF_Total = GPF_con + GPF_ref
        print("Total GPF : ",GPF_Total)
        return GPF_Total+GIS+PTax
    elif type == 3:   #custom deductions
        return int(input('Enter the total deduction : '))
    else:
        return 0  #no deductions

os.system("cls")
DA = int(input("Enter the DA percentage for the month                                          : "))
HRA = int(input("Enter the HRA percentage for the month                                         : "))
eGrade = int(input("Enter the Grade of the Employee(1,2,3,4)                                       : "))
sal_type = str(input("Regular Salary/Provisional Salary? (Y/N)                                       : "))
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

        print("________________________________")
        print("Gross Salary        : ",Gross)
        print("________________________________")

        print("\n\n")
        print("\n## DEDUCTIONS ##")
        print("_____________________________________________________________________________________")

        print("NPS Contribution    : ",NPS)
        print("GIS                 : ",GIS)
        print("Professional Tax    : ",PTax)

        print("________________________________")
        print("Total Deduction     : ",Ded)
        print("Gross Salary        : ",Gross-Ded)
        print("________________________________")

        print("\n\n")

        os.system("pause")
        os.system("cls")

except:
    print("An error has occured!")

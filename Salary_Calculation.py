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
NPS = 0
Gross = 0
Net = 0
GIS = 0
PTax = 208
Ded = 0


DA = int(input("Enter the DA percentage for the month: "))
HRA = int(input("Enter the HRA percentage for the month: "))
eGrade = int(input("Enter the Grade of the Employee: "))
sal_type = str(input("Regular Salary/ Provisional Salary? (Y/N) : "))

MA = int(input("Enter the Medical Allowance for the month: "))
os.system("cls")

try:
    while True:
        print("\n## ALLOWANCES ##")
        print("__________________________________________")

        BP = int(input("Enter Basic Pay: "))
        GP = int(input("Enter Grade Pay: "))
    
        # All Calculations
        print("\n")

        

        TotalPay = BP+GP
        DearA = (DA/100)*TotalPay
        HouseR = (HRA/100)*TotalPay
        Gross = TotalPay+DearA+HouseR+MA
        NPS = 0.1*(TotalPay+DearA)
        Ded = NPS+GIS+PTax

        print("__________________________________________")
        print("Basic Pay: ",BP)
        print("Grade Pay: ",GP)
        print("Total Pay: ",TotalPay)

        print("\nDearness Allowance  : ", DearA)
        print("House Rent Allowance: ", HouseR)

        print("__________________________________________")
        print("Gross Salary        : ",Gross)
        print("__________________________________________")

        print("\n\n\n")
        print("\n## DEDUCTIONS ##")
        print("__________________________________________")

        print("NPS Contribution    : ",NPS)
        print("GIS                 : ",GIS)
        print("Professional Tax    : ", PTax)

        print("__________________________________________")
        print("Total Deduction     : ",Ded)
        print("Gross Salary        : ",Gross-Ded)
        print("__________________________________________")

        print("\n\n")

        os.system("pause")
        os.system("cls")
except:
    print("An error has occured!")

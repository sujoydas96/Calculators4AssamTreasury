#Dependencies
from treasury_calculators import calculators

#Functions

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

#main program
try:
    BP = int(input("Enter the Basic Salary : "))
    GP = int(input("Enter the Grade Pay : "))

    start_date = int(input("Enter the starting date of the leave period : "))        #starting date of leave date
    end_date = int(input("Enter the final date of the leave period : "))             #ending date of end date
    total_days = int(input("Enter the total number of days in the month : "))        #total number of days in the month

    TotalPay = BP+GP
    DearA = (DA/100)*TotalPay
    HouseR = (HRA/100)*TotalPay
    Gross = TotalPay+DearA+HouseR+MA
    NPS = 0.1*(TotalPay+DearA)
    Ded = NPS+GIS+PTax

except:
    print("An error has occured!")
#Dependencies
#from treasury_calculators import calculators

#Functions

#Global Variables
GIS = 0
PTax = 208


#main program
try:
    BP = int(input("Enter the Basic Salary : "))
    GP = int(input("Enter the Grade Pay : "))
    HRA = int(input("Enter the Percentage of House Rent Allowance : "))
    DA = int(input("Enter the Percentage of Dearness Allowance : "))
    MA = int(input("Enter the Medical Allowance : "))

    start_date = int(input("Enter the starting date of the leave period : "))        #starting date of leave date
    end_date = int(input("Enter the final date of the leave period : "))             #ending date of end date
    total_days = int(input("Enter the total number of days in the month : "))        #total number of days in the month
    absent_days = end_date-start_date+1

    TotalPay = ((BP+GP)/total_days)*absent_days
    DearA = (((DA/100)*TotalPay)/total_days)*absent_days
    HouseR = (((HRA/100)*TotalPay)/total_days)*absent_days
    Gross = TotalPay+DearA+HouseR+MA
    NPS = 0.1*(TotalPay+DearA)
    Ded = NPS+GIS+PTax

    print("Gross Amount : ",Gross)
    print("Deduction Amount : ", Ded)

except:
    print("An error has occured!")
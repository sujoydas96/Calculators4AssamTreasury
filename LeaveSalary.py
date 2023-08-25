#Dependencies
from treasury_calculators import calculators

#Functions

#Global Variables

#main program
try:
    BP = int(input("Enter the Basic Salary : "))
    GP = int(input("Enter the Grade Pay : "))

    start_date = int(input("Enter the starting date of the leave period : "))   #starting date of leave date
    end_date = int(input("Enter the final date of the leave period : "))     #ending date of end date
    total_days = int(input("Enter the total number of days in the month : "))    #total number of days in the month

except:
    print("An error has occured!")
#Dependencies
import os
import math

#Global Variables
present = ''
Leave_Last_Date = 0
Days_in_month = 30
p_month_totalpay = 0
l_totalPay = 0
n_month_totalpay = 0


#Functions
def next10(a: int):
    remainder = a%10
    if remainder != 0:
        return a+(10-remainder)
    else:
        return a

def increment(a: int):
    return int(next10(a*1.03))

#Introduction
os.system("cls")
print("This program is to be used for calculation of Increment for an Incumbent who is on Leave.\nIt is important for the incumbent to be on leave on the 1st of July for this calculator.")
print("The No. of Days in this calculator is the number of days in the month in which the leave period ends.")
print("The Leave End Date is the date on which the Leave ends i.e. the last date of the Leave period.")
os.system("pause")

try:
    while True:
        Leave_Last_Date = int(input("Enter the last date of leave              : "))
        Days_in_month = int(input("Enter the number of days in the final month               : "))
        p_month_totalpay = int(input("Enter the total pay (Basic + Grade) prior to increment         : "))
        print("__________________________________________________________________")

        #Calculations
        l_totalPay = next10((p_month_totalpay/Days_in_month)*Leave_Last_Date)
        n_month_totalpay = next10((increment(p_month_totalpay)/Days_in_month)*(Days_in_month-Leave_Last_Date))
        print("LEAVE SALARY CALCULATION")
        print("Total Pay for the Leave Salary is:                                      ",l_totalPay)

        print("\n__________________________________________________________________")
        print("REGULAR SALARY CALCULATION")
        print("Total Pay for Reg. Salary for remainder of the month is(after increment):    ",n_month_totalpay)

        print("\nThis Calculator does not calculate total salary.\nUse the total salary to compute total salary with all allowances and deductions with other calculators.")
        os.system("pause")
        os.system("cls")

except:
    print("An Error has occured!")

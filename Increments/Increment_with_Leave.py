#Dependencies
import os
import math

#Global Variables
present = ''
Leave_Last_Date = 0
Days_in_month = 30


#Functions


#Introduction
os.system("cls")
print("This program is to be used for calculation of Increment for an Incumbent who is on Leave.\nIt is important for the incumbent to be on leave on the 1st of July for this calculator.")
print("The No. of Days in this calculator is the number of days in the month in which the leave period ends.")
print("The Leave End Date is the date on which the Leave ends i.e. the last date of the Leave period.")
os.system("pause")

try:
    print("__________________________________________")
    present = input("Whether Present on First Day of July(Y/N)")
    if(present == 'Y' or present == 'y'):
        print("y")
    elif(present == 'N' or present == 'n'):
        print("n")
    else:
        print("An Error has occured!")
except:
    print("An Error has occured!")

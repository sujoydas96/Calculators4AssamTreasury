#Dependencies
import os

#Main
try:
    DA = int(input("Enter the new DA : "))
    os.system("cls")
    while True:
        salary = int(input("Enter the Total Pay (BP + GP)     : "))
        print("Increased DA                      : ",int(salary*(DA/100)),"\n")
except:
    print("An Error has occured!")
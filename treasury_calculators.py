import math

#create a class of calculators that have the all important functions necessary of the calculations
class treasury_calculators:
    def next10(self, num: float):
        num = int(num)
        rem = num%10
        if rem == 0:
            return num
        else: return num+(10-rem)

    def next100(self):
        num = int(num)
        rem = num%100
        if rem == 0:
            return num
        else: return num+(100-rem)

    def DA(self,princi:int,DA:int):   #DA is a whole number denoting the current percentage
        return princi*(DA/100)
    
    def increment(self,princi:int ,per:int):
        return princi*(per/100)
    
    def round(self, number:float):
        return int(math.round(number))


class time_calc:

    def leap_year(self,yr):
        pass
        
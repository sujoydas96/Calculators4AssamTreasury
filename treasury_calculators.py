import math

#create a class of calculators that have the all important functions necessary of the calculations
class calculators:
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
        return int(round(number))


class time_calc:
    def leap_year(self,yr):
        if yr%4 == 0:
            if yr%100 == 0:
                if yr%400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
        
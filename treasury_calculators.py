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

#create a class of calculators that have the all important functions necessary of the calculations
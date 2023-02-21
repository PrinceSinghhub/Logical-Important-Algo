import math
class nthPhenonachi:

    def phebonachi(self,n):

        phi = (1+math.sqrt(5))/2

        power = (pow(phi,n))

        return round(power/math.sqrt(5))

ans = nthPhenonachi()
n = 7
print(ans.phebonachi(n))
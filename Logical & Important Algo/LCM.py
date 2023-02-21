class LCM:
    def hcf(self,a,b):
        if a == 0:
            return b
        return self.hcf(b%a,a)

    def lcm(self,a,b):

        return (a*b) // self.hcf(a,b)


ans = LCM()
print(ans.lcm(4,6))
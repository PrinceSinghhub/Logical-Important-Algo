class LCM:
    # ecluid alforithm
    def hcf(self,a,b):
        if a == 0:
            return b
        return self.hcf(b%a,a)


ans = LCM()
print(ans.hcf(4,6))
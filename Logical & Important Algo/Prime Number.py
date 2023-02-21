class PrimeNumber:

    def CheckPrime(self,n):

        if n < 2:
            return "Valid Number"

        count = 2

        while count * count <= n:

            if n%count == 0:
                return 0

            count+=1
        return 1
ans = PrimeNumber()
print(ans.CheckPrime(4))


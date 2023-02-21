class PascalTraingle:

    def solve(self,n):

        if n == 0:
            return []

        elif n == 1:
            return [[1]]

        Tri = [[1]]

        for i in range(1,n):

            row = [1]

            for j in range(1,i):

                row.append(Tri[i-1][j-1] + Tri[i-1][j])
            row.append(1)
            Tri.append(row)

        return Tri

ans = PascalTraingle()
n = 5
print(ans.solve(n))
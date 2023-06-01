class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def prime(n: int) -> list[bool]:
            is_prime: list[bool] = [True for _ in range(n + 1)]
            is_prime[0] = is_prime[1] = False

            i = 2
            while i <= n:
                if is_prime[i]:
                    j = 2 * i
                    while j <= n:
                        is_prime[j] = False
                        j += i
                i += 1

            return is_prime
        
        
        
        result=prime(right)
        ind=[]
        for i in range(left,len(result)):
            if result[i]==True:
                ind.append(i)
        dis=inf
        print(ind)
        if len(ind)<2:
            return [-1,-1]
        else:
            posOne=-1
            posTwo=-1
            for i in range(len(ind)-1):
                if ind[i+1]-ind[i]<dis:
                    dis=ind[i+1]-ind[i]
                    posOne=ind[i]
                    posTwo=ind[i+1]
                

        return [posOne,posTwo]

            



        
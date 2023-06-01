class Solution:
    def countPrimes(self, n: int) -> int:
        def prime_sieve(n: int) -> list[bool]:
            is_prime: list[bool] = [True for _ in range(n + 1)]
            is_prime[0] = is_prime[1] = False

            i = 2

            while i * i <= n:
                if is_prime[i]:
                    j = i * i
                    while j <= n:
                        is_prime[j] = False
                        j += i
                i += 1

            return is_prime.count(True)

        if n==2 or n==1 or n==0:
            return 0
         
        return prime_sieve(n-1)


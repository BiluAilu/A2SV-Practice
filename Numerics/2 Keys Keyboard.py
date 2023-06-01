class Solution:
    def minSteps(self, n: int) -> int:
        '''
        1->0
        2->2
        3->3
        4->4->2+2
        5->5
        6->5->3+2
        7->7
        8->6->4+2
        9->6->3+2+1
        10->7->5+2
        11->11
        12->7->5+2
        13->13
        14->9->7+2
        15->8->5+2+1

        '''
        def trial_division_simple(n: int) -> list[int]:
            factorization: list[int] = []
            d = 2

            while d * d <= n:
                while n % d == 0:
                    factorization.append(d)
                    n //= d
                d += 1
            if n > 1:
                factorization.append(n)
            
            return factorization
            
        print(sum(trial_division_simple(n)))
        return sum(trial_division_simple(n))
        

        

        
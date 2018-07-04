from operator import mul

class Solution:
    def shoppingOffers(self, prices, specials, needs):
        memo = {}
        def shoppingIteration(cur):
            total = [cur[i]*prices[i] for i in range(len(needs))]
            for special in specials:
                diff = [cur[i] - special[i] for i in range(len(needs))]
                
                if min(diff) >= 0:
                    total = min(total, memo.get(tuple(diff), shoppingIteration(diff)) + special[-1])
            memo[tuple(diff)] = total

            return total
        
        return shoppingIteration(needs)
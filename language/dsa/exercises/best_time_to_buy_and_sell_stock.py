from typing import List

class Solution:
    def maxProfit2(self, prices: List[int]) -> int:
        best_time = 0
        for c in range(len(prices)):
            for v in range(c + 1,len(prices)):
                calc = prices[v] - prices[c]
                if calc > best_time:
                    best_time = calc
        return best_time
    
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        max_profit = 0
        min_price = prices[0]

        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)

        return max_profit
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit(prices = [7,1,5,3,6,4]))
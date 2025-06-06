class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = float('-inf')
        buy2 = float('-inf')    
        sell1 = 0
        sell2 = 0 
        for i in range(len(prices)):
            buy1 = max(buy1,-prices[i])
            sell1 = max(sell1,buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])
        return sell2
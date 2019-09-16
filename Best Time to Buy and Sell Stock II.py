class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        return self.maxProfitR(prices, 0, 0, 0)

    def maxProfitR(self, prices: List[int], index, have_stock, total_profit) -> int:
        if len(prices) - 1 == index:
            if have_stock:
                return total_profit + prices[index]
            return total_profit

        sell_option = 0

        if have_stock:
            sell_option = self.maxProfitR(prices, index + 1, False,
                                          total_profit + prices[index])

        buy_option = self.maxProfitR(prices, index + 1, True, total_profit - prices[index])

        hold_option = self.maxProfitR(prices, index + 1, have_stock,
                                      total_profit)

        return max(sell_option, buy_option, hold_option)

    def maxProfitDP(self, prices: List[int]):
        # best_profit[0][i] = don't have stock on day i
        # best_profit[1][i] = have stock on day i

        best_profit = [[0] * 2 for i in range(len(prices))]

        best_profit[len(prices) - 1][0] = 0
        best_profit[len(prices) - 1][1] = prices[-1]

        for i in range(len(prices) - 2, -1, -1):
            bought = best_profit[i + 1][1] - prices[i]
            sold = best_profit[i + 1][0] + prices[i]

            best_profit[i][0] = max(bought, best_profit[i + 1][0])
            best_profit[i][1] = max(sold, best_profit[i + 1][1])

            # 7 7 3 3 0 0
            # 14 8 8 6 6 4

        return best_profit[0][0]

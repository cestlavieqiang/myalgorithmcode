"""
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

"""

class Solution():
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        # 存储最小值
        min_price = prices[0]
        # 存储最大利润
        max_profit = 0
        for i in range(len(prices)):
            flag = prices[i] - min_price
            if prices[i] < min_price:
                min_price = prices[i]
            elif  flag > max_profit:
                max_profit = flag
        return max_profit
# 这是特别耗时的一种解法，不知为什么，时间复杂度明明是O(N)


#运行了一下别人的代码，基本上都稳定在100ms左右，应该还有更好的解法

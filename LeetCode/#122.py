def maxProfit(prices):
    res = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            res += prices[i] - prices[i-1]
    return res


print(maxProfit([7,6,4,3,1]))

#if stock is increasing: wait till most amount
#if stock is decreasing: dont sell
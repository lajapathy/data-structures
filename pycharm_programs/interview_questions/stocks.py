'''
The cost of a stock on each day is given in an array, find the max profit that you can make by buying
and selling in those days. For example, if the given array is {100, 180, 260, 310, 40, 535, 695},
the maximum profit can earned by buying on day 0, selling on day 3. Again buy
on day 4 and sell on day 6. If the given array of prices is sorted in decreasing order,
then profit cannot be earned at all.
'''

def profit_max(list1):
    min = list1[0]
    max = list1[0]
    prev_price = list1[0]
    sell_pairs = []
    for price in list1:
        if price > max:
            max = price
        if (price < min) and (price > prev_price) and (min!=max):
            #sell
            sell_pairs.append((max,min))
            max = 0
            min = price
        prev_price = price
    if max > min :
        sell_pairs.append((max, min))
    return sell_pairs


print(profit_max([100, 180, 260, 310, 40, 535, 695]))
print(profit_max([4 , 3, 8, 10]))
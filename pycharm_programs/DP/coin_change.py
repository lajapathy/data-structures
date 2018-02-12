# Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm}
# valued coins, how many ways can we make the change? The order of coins doesn’t matter.
#
# For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}.
# So output should be 4. For N = 10 and S = {2, 5, 3, 6},
# there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}.
# So the output should be 5.

import pdb

def coin_change_recursive(sum, coin_set):
    #pdb.set_trace()
    if coin_set == []:
        return 0
    if sum == 0:
        return 1
    if sum < 0:
        return 0
    if len(coin_set)==1 and sum%coin_set[0] == 0 :
        return 1
    return coin_change_recursive(sum, coin_set[:len(coin_set)-1]) + coin_change_recursive(
        sum-coin_set[len(coin_set)-1], coin_set)

def min_num_coins(sum, coin_set):
    if sum==0:
        return 1
    if sum<0:
        return


print(coin_change_recursive(5, [1,3,4]))

# def coin_change_dp(sum, coin_set):
#     result = [[0 for x in range(len(coin_set))] for x in range(sum+1)]
#     for i in range(sum+1):
#         for j in range(len(coin_set)):
#             if i < j:
#                 result[j][i] = max(0,result[j-1][i])
#             if
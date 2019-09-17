
#coin_set=[2,3,5]
#n=20

def coinChange(desired_sum, coinset):
    #import pdb;pdb.set_trace()
    flag = None
    for coin in coinset:
        if coin==desired_sum:
            return 1
        if coin<desired_sum:
            flag = coin
    if flag:
        return 1 + coinChange(desired_sum-flag, coinset)
    return


def coinChange2(desired_sum, coinset, result_dict={}):

    if (desired_sum, len(coinset)) in result_dict:
        return result_dict[(desired_sum, len(coinset))]
    flag = None
    for coin in coinset:
        if coin==desired_sum:
            result_dict[desired_sum] = coin
            return [coin]
        if coin<desired_sum:
            flag = coin
    if flag:
        result_dict[(desired_sum, len(coinset))] = [flag]
        return [flag] + coinChange2(desired_sum-flag, coinset, result_dict)
    return []



print coinChange(9, [3,6,7])
print coinChange2(9, [3,6,7])
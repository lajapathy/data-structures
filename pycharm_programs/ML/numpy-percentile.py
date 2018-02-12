
import numpy as n

a = n.array([1,5,8,10,11,11,11,11,12,11,11,10])
percentile_value = n.percentile(a,70)
filtered_list = [x for x in a.tolist() if x >= percentile_value]
print filtered_list
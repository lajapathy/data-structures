#Given a csv file, generate a new csv file, only with the given set of columns

import csv
from collections import OrderedDict


desired_columns = ['TIME','AVERAGE_PACKET_SIZE','CPU_0_5MIN_AVG_SESSMGR_CPUS']
with open('3.csv','r') as csvfile:
    dr = csv.reader(csvfile)
    key_list = dr.next()
    #print key_list
    csv_dict = OrderedDict()
    for key in key_list:
        csv_dict[key] = []
    for row in dr:
        for i in xrange(len(key_list)):
            csv_dict[key_list[i]].append(row[i])

    csv_dict_desired = OrderedDict((k,v) for k,v in csv_dict.items() if k in desired_columns)

    with open("3-modified.csv", "w") as f:
        f.write(",".join(csv_dict_desired.keys()) + "\n")
        for row in zip(*csv_dict_desired.values()):
            f.write(",".join(str(n) for n in row) + "\n")
        f.close()
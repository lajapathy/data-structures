
import re

def show_active_charging_nat():
    dict = {}
    stats_encountered = False
    for line in open("nat_output",'r'):
        if re.match('\s*Realm Name\s*:\s*(.*)\s*Context\s*:\s*(.*)',line):
            realm_name = re.match('\s*Realm Name\s*:\s*(.*)\s*Context\s*:\s*(.*)',line).group(1)
            context_name = re.match('\s*Realm Name\s*:\s*(.*)\s*Context\s*:\s*(.*)', line).group(2)
            dict[realm_name]={'context_name':context_name}
            stats_encountered = False
            continue
        if re.match('\s*Statistics:.*',line):
            stats_encountered = True
        if stats_encountered:
            if re.match('\s*(.*?)\:\s*(\d+)\s*(.*)\:\s*(\d+)\s*',line):
                stats1 = re.match('\s*(.*?)\:\s*(\d+)\s*(.*)\:\s*(\d+)\s*',line).group(1)
                stats1_value = re.match('\s*(.*?)\:\s*(\d+)\s*(.*)\:\s*(\d+)\s*', line).group(2)
                stats2 = re.match('\s*(.*?)\:\s*(\d+)\s*(.*)\:\s*(\d+)\s*', line).group(3)
                stats2_value = re.match('\s*(.*?)\:\s*(\d+)\s*(.*)\:\s*(\d+)\s*', line).group(4)
                dict[realm_name][stats1] = stats1_value
                dict[realm_name][stats2] = stats2_value
            if re.match('\s*(.*?)\:\s*(\d+)',line):
                stats1 = re.match('\s*(.*?)\:\s*(\d+)',line).group(1)
                stats1_value = re.match('\s*(.*?)\:\s*(\d+)', line).group(2)
                dict[realm_name][stats1] = stats1_value
    return dict

for k,v in show_active_charging_nat().items():
    print str(k) +' : ' +str(v)


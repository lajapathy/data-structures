import re

def parser1(output_str):
    tuple_list1 = []
    dict1 = {}
    for line in output_str.readlines():
        #print line
        match_obj = re.match('\s*(\d+)\s*(\d+)\s*(.*[Module|Controller])\s+(.*?)\s+(.*)',line)
        if match_obj:
            mod = match_obj.group(1)
            ports = match_obj.group(2)
            mod_type = match_obj.group(3)
            model = match_obj.group(4)
            status = match_obj.group(5)
            tuple_list1.append((mod,ports,mod_type,model,status))
            dict1[mod] = {'ports' : ports, 'mod_type' : mod_type, 'model' : model, 'status' : status}

    return dict1


dict1 = parser1(open('module_output','r'))
for k,v in dict1.items():
    print k,v
print dict1['28']['status']
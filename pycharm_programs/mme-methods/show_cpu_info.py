
import re
def show_cpu_info(self):
    '''
    This method parses show cpu info verbose output
    '''
    cpu_num = 0
    card_num = 0
    reading = ''
    free_memory = 0
    dict = {}
    for line in open('show_cpu_info.txt','r'):
        if re.match('\s*Card\s*(\d+),\s*CPU\s*(\d+):.*',line):
            cpu_num = re.match('\s*Card\s*(\d+),\s*CPU\s*(\d+):.*',line).group(1)
            card_num = re.match('\s*Card\s*(\d+),\s*CPU\s*(\d+):.*',line).group(2)
        if re.match('\s*(Last Reading|5-Minute Average|Maximum/Minimum)\s*\:\s*',line):
            reading = re.match('\s*(Last Reading|5-Minute Average|Maximum/Minimum)\:\s*',line).group(1)
        #Add more extractions here later, if needed. Currently, we extract MEMORY DETAILS (Free) alone
        if re.match('\s*Free\s*:\s*(\d+)M\s*Free',line):
            free_memory = re.match('\s*Free\s*:\s*(\d+)M\s*Free',line).group(1)
            dict[(card_num,cpu_num,reading)] = free_memory
    if not dict.keys():
        return CollectResult(1, dict)
    return CollectResult(0, dict)




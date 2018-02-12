from collections import defaultdict
from collections import OrderedDict
import re

# Applications
def fun1():
    return 12


db_dict = {('psc', '19.2'): 13, ('psc2', '20.0'): 14}
db_default_dict = defaultdict(fun1,db_dict)

print db_default_dict[('psc','20.3')]


#Application2

#-rw-------  1 nobody nogroup 7850648 2016-03-21 19:41 bulkstat20160302031500.txt
#-rw-------  1 nobody nogroup 7850484 2016-03-21 19:42 bulkstat20160302030000.txt
#-rw-------  1 nobody nogroup 7850299 2016-03-21 19:43 bulkstat20160302024500.txt
#-rw-------  1 nobody nogroup 7850142 2016-03-21 19:44 bulkstat20160302023000.txt
#-rw-------  1 nobody nogroup  327680 2016-03-21 19:45 bulkstat20160302053000.txt

def exec_command():
    pass

cli_output = exec_command('ls -lart')
dict = {}
##### dict = OrderedDict()
for line in cli_output:
    timestamp = re.match('ssss',line)
    filename = re.match('dddd',line)
    dict[timestamp] = filename





import logging
import sys

#logging.basicConfig(level=logging.DEBUG,
#                    format='%(asctime)s %(levelname)s %(message)s',
#                    filename='myapp.log',
#                    filemode='w')
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    stream=sys.stdout)
print logging.INFO
logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything


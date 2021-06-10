import logging

logging.basicConfig(level=logging.DEBUG)

import helper

print()

#! 5 logging levels
logging.debug('This is a debug message')      #! Level 1
logging.info('This is a info message')        #! Level 2
logging.warning('This is a warning message')  #! Level 3
logging.error('This is a error message')      #! Level 4
logging.critical('This is a critical message')#! Level 5

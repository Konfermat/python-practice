# There is two modules that will  help you work with time
# time and datetime

import time
#return convert seconds in arguments to time since epoch
# print(time.gmtime(120))
# return time.time() if no arg
# print(time.gmtime())

# like gmtime but converts to local time
# print(time.localtime())
# DST flag is set to 1 when DST applies to a given time
# print(time.localtime(120))

import datetime
print(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
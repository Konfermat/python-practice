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


import time
from datetime import datetime

# Get the current time as a time object
current_time_struct = time.localtime() 

# Format the time object into a string
formatted_time_str = time.strftime("%Y-%m-%d %H:%M:%S", current_time_struct)
print(f"Formatted time using time.strftime: {formatted_time_str}")

# Alternatively, using datetime for more common use cases:
now = datetime.now()
formatted_datetime_str = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted time using datetime.strftime: {formatted_datetime_str}")
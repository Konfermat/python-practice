import time
'''
The epoch is the point where the time starts, 
the return value of time.gmtime(0). 
It is January 1, 1970, 00:00:00 (UTC) on all platforms.
'''
print(time.gmtime(0))
current_timestamp = time.time() # float


# synchronous way of calling

import time

ST = time.perf_counter()

def doJob():
    print("Going to sleep for 2 secs")
    time.sleep(2)
    print("Just woke up from sleep")

doJob()
doJob()
doJob()

ET = time.perf_counter()
print(f"The total time taken by the task is {ET - ST}")

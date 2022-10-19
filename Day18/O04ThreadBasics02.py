# asynchronous execution code

import threading
import time

ST = time.perf_counter()

def doJob():
    print(f"Going to sleep for 2 secs......{threading.current_thread().name}")
    time.sleep(2)
    print(f"Just got up from sleep........{threading.current_thread().name}")

thrd1 = threading.Thread(target=doJob, name = "th1")
thrd2 = threading.Thread(target=doJob, name = "th2")
thrd3 = threading.Thread(target=doJob, name = "th3")

thrd1.start()
thrd2.start()
thrd3.start()

thrd1.join()
thrd2.join()
thrd3.join()

ET = time.perf_counter()
print(f"The total time taken by the task is {ET - ST}")

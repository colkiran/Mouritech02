

import time
import threading
import concurrent.futures

ST = time.perf_counter()

def doJob(secs):
    print(f"Sleeping for {secs} seconds .......{threading.current_thread().name}")
    time.sleep(secs)
    print(f"Just woke up from sleep ...... {threading.current_thread().name}")

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [6, 5, 4, 3, 2, 1]
    results = executor.map(doJob, secs)

    for result in results:
        result

ET = time.perf_counter()
print(f"The total time taken by the task is {ET - ST}")

import time
import threading
import concurrent.futures

ST = time.perf_counter()

def doJob(secs):
    print(f"Going to sleep for {secs} seconds.....{threading.current_thread().name}")
    time.sleep(secs)
    print(f"Just woke up from sleep ............{threading.current_thread().name}")

with concurrent.futures.ThreadPoolExecutor() as executor:
    thrd1 = executor.submit(doJob, 2)
    thrd2 = executor.submit(doJob, 2)
    thrd3 = executor.submit(doJob, 2)

    thrd1.result()
    thrd2.result()
    thrd3.result()

ET = time.perf_counter()
print(f"The total time taken by the task is {ET - ST}")
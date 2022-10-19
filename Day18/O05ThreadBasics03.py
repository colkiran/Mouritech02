
import threading
import time

ST = time.perf_counter()

def doJob(secs, tname):
    print(f"Going to sleep for 2 secs......{tname} -> {threading.current_thread().name}")
    time.sleep(secs)
    print(f"Just got up from sleep........{tname} -> {threading.current_thread().name}")

threads = []

for i in range(50):
    t = threading.Thread(target=doJob, name="th" + str(i), args=[2, "thrd" + str(i)])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

ET = time.perf_counter()
print(f"The total time taken by the task is {ET - ST}")
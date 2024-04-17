import psutil
import time

cpu = psutil.cpu_times(percpu=True)
for c in cpu:
    d = 0
    for t in c:
        d += t
    print(d)
print(time.time()-psutil.boot_time())
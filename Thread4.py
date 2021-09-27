import time
from threading import Thread

COUNT = 500_000_000


def countdown(n):
    while n > 0:
        n -= 1


start = time.time()
t1 = Thread(target=countdown, args=(COUNT//2,))
t2 = Thread(target=countdown, args=(COUNT//2,))
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
print("Tempo em segundos:", round((end-start), 2))

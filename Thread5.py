import time
from multiprocessing import Process

COUNT = 500_000_000


def countdown(n):
    while n > 0:
        n -= 1


# necessário para processos
if __name__ == "__main__":
    start = time.time()
    p1 = Process(target=countdown, args=(COUNT//2,))
    p2 = Process(target=countdown, args=(COUNT//2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.time()
    print("Tempo em segundos:", round((end-start), 2))

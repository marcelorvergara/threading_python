import time
from threading import Thread
from multiprocessing import Process

COUNT = 50_000_000_000


def countdown(n):
    while n > 0:
        n -= 1


# variável de ambiente (escopo abaixo)
if __name__ == "__main__":
    # Thread (mais rápido)
    start = time.time()
    t = Thread(target=countdown, args=(COUNT,))
    t.start()
    end = time.time()
    print("Tempo em segundos:", round((end - start), 4))

    # Processo (mais lento)
    start = time.time()
    p = Process(target=countdown, args=(COUNT,))
    p.start()
    end = time.time()
    print("Tempo em segundos:", round((end - start), 4))

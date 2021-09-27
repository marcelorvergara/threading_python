import threading, time, os, random


# Produtor e consumidor com exclusão mútua e sincronização condicional

def thread_prod():
    print("TID prdutor:", str(threading.get_ident()))
    valor = 0
    while True:
        time.sleep(random.randint(2, 5))
        vazio.acquire()
        mutex.acquire()  # Início da região crítica
        buffer[0] = valor
        print("Produtor ->", buffer[0])
        mutex.release()  # Fim da região crítica
        cheio.release()
        valor += 1


def thread_cons():
    print("TID consumidor:", str(threading.get_ident()))
    valor = 0
    while True:
        time.sleep(random.randint(2, 5))
        cheio.acquire()
        mutex.acquire()
        buffer[0] = valor
        print("Consumidor ->", buffer[0])
        mutex.release()
        vazio.release()
        valor += 1


TAMBUF = 1
buffer = [0] * TAMBUF
mutex = threading.Lock()
cheio = threading.Semaphore(0) # cheio = 0
vazio = threading.Semaphore(TAMBUF) # vazio = 1
print("PID:", str(os.getpid()))
produtor = threading.Thread(target=thread_prod)
consumidor = threading.Thread(target=thread_cons)
produtor.start()
consumidor.start()

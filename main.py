import threading, time, random, os


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def trabalhador(n):
    while True:
        msg = "Thread " + str(n) + ' - TID ' + str(threading.get_ident())
        print(msg)
        time.sleep(random.randint(2,6))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Threading')
    print("PID", os.getpid())
    # criar lista de threads
    threads = []
    for i in range(2):
        t = threading.Thread(target=trabalhador, args=(i,))
        threads.append(t)
    # iniciar as threads
    for t in threads:
        t.start()

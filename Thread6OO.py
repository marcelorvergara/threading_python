import threading, random, time


class Thread(threading.Thread):

    def __init__(self, id):
        super(Thread, self).__init__()
        self.id = id

    def run(self):
        while True:
            msg = "Thread " + str(self.id) + " - TID " + str(threading.get_ident())
            print(msg)
            time.sleep(random.randint(2, 5))


threads = []
for i in range(4):
    t = Thread(i)
    threads.append(t)
    t.start()

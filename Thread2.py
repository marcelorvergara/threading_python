import sched, threading, time

scheduler = sched.scheduler(time.time, time.sleep)
contador = 0


def aumenta_contador(nome):
    global contador
    print("EVENTO:", time.ctime(), nome)
    contador +=1
    print("Contador atual:", contador)


print("Início:", time.ctime())
e1 = scheduler.enter(2, 1, aumenta_contador, ("E1",))
e2 = scheduler.enter(4, 1, aumenta_contador, ("E2",))

t = threading.Thread(target=scheduler.run)
print(scheduler.queue)
t.start()

# cancelar uma tarefa
scheduler.cancel(e1)

# aguardar o fim das threads para printar "Contador final:"
t.join()

print("Contador final:", contador)

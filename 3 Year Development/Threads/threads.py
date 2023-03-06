import threading

lock = threading.Lock()

counter = 0

def game_loop():
    global counter
    for i in range(0, 1000000):
        lock.acquire()
        counter += 1
        lock.release()
    print(counter)

t = threading.Thread(target = game_loop)

#t.daemon = True

t.start()

t1 = threading.Thread(target = game_loop)
t1.start()

t.join()
t1.join()

print('Goodbye')
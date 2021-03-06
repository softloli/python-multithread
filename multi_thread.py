# -*- coding: UTF-8 -*-
import threading,random,queue,random,time
queue = []

con = threading.Condition()

class Producer(threading.Thread):
    def run(self):
        while True:
            if con.acquire():
                if len(queue) > 10:
                    con.wait()
                else:
                    elem = random.randrange(100)
                    queue.append(elem)
                    print("Producer a elem {}, Now size is {}".format(elem, len(queue)))
                    time.sleep(random.random())
                    con.notify()
                con.release()

class Consumer(threading.Thread):
    def run(self):
        while True:
            if con.acquire():
                if len(queue) <= 0:
                    con.wait()
                else:
                    elem = queue.pop()
                    print("Consumer a elem {}. Now size is {}".format(elem, len(queue)))
                    time.sleep(random.random())
                    con.notify()
                con.release()

if __name__ == '__main__':
    for i in range(3):
        Producer().start()

    for i in range(2):
        Consumer().start()

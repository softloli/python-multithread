import Queue,random,threading,time

queue = Queue.Queue(10)

class Producer(threading.Thread):

    def run(self):
        while True:
            elem = random.randrange(100)
            queue.put(elem)
            print("Producer a elem {}, Now size is {}".format(elem, queue.qsize()))
            time.sleep(random.random())

class Consumer(threading.Thread):

    def run(self):
        while True:
            elem = queue.get()
            queue.task_done()
            print("Consumer a elem {}. Now size is {}".format(elem, queue.qsize()))
            time.sleep(random.random())

def main():

    for i in range(3):
        Producer().start()

    for i in range(2):
        Consumer().start()

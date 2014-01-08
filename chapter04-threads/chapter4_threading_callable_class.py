import threading
from time import sleep, ctime

class loop():
    def __init__(self, loop_id, secs):
        self.loop_id = loop_id
        self.secs = secs

    def __call__(self):
        print('start loop', self.loop_id, 'at:', ctime())
        sleep(self.secs)
        print('loop', self.loop_id, 'done at:', ctime())

def main():
    print("starting time", ctime())
    threads = []

    t1 = threading.Thread(target=loop(1,4))
    threads.append(t1)
    
    t2 = threading.Thread(target=loop(2, 2))
    threads.append(t2)

    # start threads
    for t in threads:
        t.start()

    # wait for all threads to end
    for t in threads:
        t.join()

    print("ending time", ctime())
    

if __name__=="__main__":
    main()

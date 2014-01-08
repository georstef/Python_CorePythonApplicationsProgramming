import threading
from time import sleep, ctime

class loop(threading.Thread):
    def __init__(self, loop_id, secs):
        super().__init__() # the same with the call below
        # threading.Thread.__init__(self) # the same with the call above
        self.loop_id = loop_id
        self.secs = secs

    # when we subclass threading.Thread we must have the "run" method
    def run(self):
        #print('start loop', self.loop_id, 'at:', ctime())
        sleep(self.secs)
        print('loop', self.loop_id, 'done at:', ctime())

def main():
    print("starting time", ctime())
    threads = []

    t1 = loop(1,4)# <- instanciate a "loop" object here
    threads.append(t1)
    
    t2 = loop(2, 2)# <- instanciate a "loop" object here
    threads.append(t2)

    # start threads 
    for t in threads:
        t.start() # <- in this case it calls loop.run

    print('----')
    print('No of threads: ', len(threading.enumerate()))
    print('threads: ', threading.enumerate())
    print('----')

    # wait for all threads to end
    for t in threads:
        t.join()

    print("ending time", ctime())
    

if __name__=="__main__":
    main()

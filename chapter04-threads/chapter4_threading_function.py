import threading
from time import sleep, ctime

def loop(loop_id, secs):
    print('start loop', loop_id, 'at:', ctime())
    sleep(secs)
    print('loop', loop_id, 'done at:', ctime())

def main():
    print("starting time", ctime())
    threads = []

    t1 = threading.Thread(target=loop, args=(1, 4))
    threads.append(t1)
    
    t2 = threading.Thread(target=loop, args=(2, 2))
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

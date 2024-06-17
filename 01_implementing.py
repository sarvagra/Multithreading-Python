#basic idea of how multithreading works.

import logging
import threading
import time

logging.basicConfig(filename="logging.log",level=logging.DEBUG, format='%(asctime)s%(message)s')
def test(id):
    for i in range(10):
        logging.info("test1 %d printing %d %s" %(id,i,time.ctime()))
        time.sleep(1)
test(1)

ther=[threading.Thread(target=test, args = (i,)) for i in range(3)]
for t in ther:
    t.start()

shared_var=0
lock_var=threading.Lock()

def test2(id):
    global shared_var 
    with lock_var:
        shared_var = shared_var+1
        logging.info("test2 id is %d has increased the shared variable by %d"%(id, shared_var))
        time.sleep(1)

thread1=[threading.Thread(target=test2, args = (id,))for i in range(3)]
for t in thread1 :
    t.start()

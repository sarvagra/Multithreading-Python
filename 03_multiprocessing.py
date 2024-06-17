# how to use multiprocessing 

import multiprocessing
import logging
import multiprocessing.queues

logging.basicConfig(filename="logging1.log",level=logging.DEBUG, format='%(asctime)s%(message)s')

def test():
    logging.info("this is my multiprocessing program")

#how to use process:

if __name__ =='__main__':
    m = multiprocessing.Process(target=test)
    logging.info("this is my main program")
    m.start()
    m.join()

def square(n):
    return n*n

#use of pool:

if __name__ =='__main__' :
    with multiprocessing.Pool(processes=4) as pool :
        out =pool.map(square,[1,2,3,4,5,6,7,8,9])
        logging.info(out)

# use of queue:

def producer(q):
    for i in range(10):
        q.put(i)

def consume(q):
    while True:
        item=q.get()
        if item is None:
            break 
        logging.info(item)
if __name__ == '__main__':
    queue=multiprocessing.Queue()
    m1= multiprocessing.Process(target=producer,args=(queue,))
    m2=multiprocessing.Process(target=consume,args=(queue,))
m1.start()
m2.start()
queue.put("sarv")
m1.join




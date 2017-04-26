import threading
import time

class MythreadLock(threading.Thread):
    def __init__(self,threadID,threadName,counter):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.threadName=threadName
        self.counter=counter
    def run(self):
        print 'Staring '+self.threadName
        threadLock.acquire()
        print_time(self.name,self.counter,3)
        threadLock.release()

def print_time(threadName,delay,counter):
    while counter:
        time.sleep(delay)
        print '%s,%s' %(threadName,time.ctime(time.time()))
        counter-=1

threadLock=threading.Lock()
threads=[]

thread1=MythreadLock(1,'thread-1',1)
thread2=MythreadLock(2,'thread-2',2)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)
#
for t in threads:
    t.join()
print 'Exiting main thread'
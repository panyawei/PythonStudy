import threading
import  time

exitFlag=0

class Mythread(threading.Thread):
    def __init__(self,threadId,name,counter):
        threading.Thread.__init__(self)
        self.threadId=threadId
        self.name=name
        self.counter=counter
    def run(self):
        print 'Staring '+self.name
        print_time(self.name,5,self.counter)
        print 'exiting '+self.name

def print_time(threadName,delay,counter):
    while counter:
        if exitFlag:
            threading.exit()
        time.sleep(delay)
        print '%s,%s' %(threadName,time.ctime(time.time()))+'\n'
        counter-=1

thread1=Mythread(1,'thread-1',1)
thread2=Mythread(2,'thread-2',2)

thread1.start()
thread2.start()
print 'Exiting Main thread'

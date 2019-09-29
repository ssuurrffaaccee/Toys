import threading
class WorkerThread(threading.Thread):
    def __init__(self,Worker):
        threading.Thread.__init__(self)
        self.Worker=Worker
    def run(self):
        while True:
            self.Worker.Run()
class Worker:
    def __init__(self,WorkerIdx):
        self.WorkerIdx=WorkerIdx
        self.TaskProxyQueue=[]
        self.LocalLock=threading.Lock()
        #self.Condition=threading.Condition(threading.Lock())
        #self.Condition.acquire()
        #print("Condition Acquired!")
    def EnqueueTaskProxy(self,TaskProxy):
        self.LocalLock.acquire()
        self.TaskProxyQueue.append(TaskProxy)
        self.LocalLock.release()
        #self.Condition.notify()
    def DequeueTaskProxy(self):
        if len(self.TaskProxyQueue)<1:
            return None
            #self.Condition.wait()
        else:
            self.LocalLock.acquire()
            TopTaskProxy=self.TaskProxyQueue.pop(0)
            self.LocalLock.release()
            return TopTaskProxy
    def Run(self):
        TaskProxyToRun=self.DequeueTaskProxy()
        if TaskProxyToRun==None:
            pass
        else:
            AuxInfo="Worker "+str(self.WorkerIdx)+" is doing this Task"
            TaskProxyToRun.ExecuteTask(AuxInfo)

class TaskSystem:
    def __init__(self,WorkerNumber):
            self.Workers=[Worker(i) for i in range(WorkerNumber)]
            self.WorkerThreads=[WorkerThread(self.Workers[i]) for i in range(WorkerNumber)]
            [self.WorkerThreads[i].start() for i in range(WorkerNumber)]
    def ReleaseTaskProxy(self,WorkerIdx,TaskProxy):
         self.Workers[WorkerIdx].EnqueueTaskProxy(TaskProxy)
GWorkerNumber=3
GSystem=TaskSystem(GWorkerNumber)

class TaskProxy:
    def __init__(self,Task):
        self.Task=Task
    def ExecuteTask(self,AuxInfo):
        self.Task.DoTask(AuxInfo)
    def Dispatch(self,WorkerIdx):
        GSystem.ReleaseTaskProxy(WorkerIdx,self)

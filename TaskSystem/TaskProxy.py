import TaskSystem as TS

class TaskProxy:
    def __init__(self,Task):
        self.Task=Task
    def ExecuteTask(self):
        Task.Dotask()
    def Dispatch(self,WorkerIdx):
        TS.GSystem.ReleaseTaskProxy(WokerIdx,self)








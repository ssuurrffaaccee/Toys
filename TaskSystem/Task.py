import TaskSystem as TS
import random as rd
class Task:
    def __init__(self):
        self.Result=[]
        self.Arg=[]
    def DoTask(self,AuxInfo):
        pass

class CalTask(Task):
    def __init__(self,a,b):
        super().__init__()
        self.Arg=[a,b]
    def DoTask(self,AuxInfo):
        self.Result.append(self.Arg[0]+self.Arg[1])
        print("Cal:"+str(self.Arg[0])+"+"+str(self.Arg[1])+"|"+AuxInfo)



pairs=[[i,j] for i in range(10) for j in range(10)]

CalTasks=[CalTask(p[0],p[1]) for p in pairs]
for t in CalTasks:
    TS.TaskProxy(t).Dispatch(rd.randint(0,2))
        

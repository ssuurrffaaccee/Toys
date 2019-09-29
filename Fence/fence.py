import threading as th
GlobalLock=th.Lock()

class Th(th.Thread):
    def __init__(self,func):
        super().__init__()
        self.f=func
    def run(self):
        self.f()


que=[]
l=th.Lock()
def putcmd(cmd):
    l.acquire()
    que.append(cmd)
    l.release()
def getcmd():
    l.acquire()
    if len(que)>0:
        cmd=que.pop(0)
    else:
        cmd=None
    l.release()
    return cmd
def f1():
    while True:
        cmd=getcmd()
        if cmd !=None:
            cmd()
def f2():
    while True:
        print('put comd1')
        putcmd(lambda  : print("do comd1"))
        print("put comd2")
        putcmd(lambda :print("do comd2"))
        print("acquire")
        GlobalLock.acquire()
        print('put release')
        putcmd(lambda :( GlobalLock.release(),print("release")))
        print("acquire")
        GlobalLock.acquire()
        GlobalLock.release()

if __name__ =="__main__":
    Th(f1).start()
    f2()

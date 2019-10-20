class Stream:
    def __init__(self,String):
        self.String=String
        self.Len=len(String)
        self.Count=0
    def Peek(self):
        if self.Count>=self.Len:
            return "E"
        else:
            return self.String[self.Count]
    def Deque(self):
        if self.Count>=self.Len:
            return "E"
        else:
            Char=self.String[self.Count]
            self.Count=self.Count+1
            return Char
CharStream=Stream("[[1,2],[1,2,[1,23,4,56]]]")
def Parser(CharStream):
    LocalListResult=[]
    while(True):
        #Peek
        NextChar=CharStream.Peek()
        #Dispatch
        if NextChar=="E":
            pass
        if NextChar=="[":
            LocalListResult.append(ListParser(CharStream))
            return LocalListResult
def ListParser(CharStream):
    LocalListResult=[]
    CharStream.Deque()
    while(True):
        NextChar=CharStream.Peek()
        print(NextChar)
        if NextChar in ["0","1","2","3","4","5","6","7","8","9"]:
            print("This")
            LocalListResult.append(IntegerParser(CharStream))
        if NextChar in[","," "]:
            CharStream.Deque()
        if NextChar =="]":
            CharStream.Deque()
            return LocalListResult
        if NextChar =="[":
            LocalListResult.append(ListParser(CharStream))
def IntegerParser(CharStream):
    IntegerString=""
    IntegerString=IntegerString+CharStream.Deque()
    print(IntegerString)
    while(True):
        NextChar=CharStream.Peek()
        print(NextChar)
        if NextChar in ["0","1","2","3","4","5","6","7","8","9"]:
            IntegerString=IntegerString+CharStream.Deque()
        else:
            print(IntegerString)
            return int(IntegerString)
print(ListParser(CharStream))
        


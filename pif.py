class pifEntry():
    def __init__(self, code, pos):
        self.code = code
        self.pos = pos

    def getCode(self):
        return self.code
    
    def getPos(self):
        return self.pos
    
    def setCode(self, code):
        self.code = code

    def setPos(self, pos):
        self.pos = pos

    def __str__(self): 
        code = "Code: " + str(self.code) 
        pos = " Pos: " + str(self.pos)
        cap = 15
        if (cap - len(code))>=0:
            return code + " " * (cap - len(code)) + pos
        else:
            return "Code: " + str(self.code) + " Pos: " + str(self.pos)

        
class pif():
    def __init__(self):
        self.elems=[]

    def add(self, code, pos):
        self.elems.append(pifEntry(code, pos))
    
    def get(self, index):
        return self.elems[index]
     
    def display(self):
        for elem in self.elems:
            print(elem)
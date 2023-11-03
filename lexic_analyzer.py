#Statement: Implement a scanner (lexical analyzer): Implement the scanning algorithm and use ST from lab 2 for the symbol table.

# Input: Programs p1/p2/p3/p1err and token.in (see Lab 1a)

# Output: PIF.out, ST.out, message “lexically correct” or “lexical error + location”
from symbol_table import SymbolTable
from pif import pif

class lexicScanner:
    def __init__(self):
        self.pif = pif()
        self.st = SymbolTable(100)         
        with open("./rules/tokens.txt", "r") as f:
            token_lines = f.readlines()
        self.token_list = []
        for line in token_lines:
            tokens = line.split(", ")
            for t in tokens:
                tc = t.strip("\n")
                self.token_list.append(tc)

    def getPif(self):
        return self.pif
    
    def getSt(self):
        return self.st

    def process_file(self,input_file):
        with open(input_file, "r") as f:
            content = f.readlines()
        lines = [line.split() for line in content]
        return lines

    def isIdentifier(self, token):
        # check if string contains only letters and numbers and is shorterthan 100 characters
        return token.isalnum() and len(token) < 50
    
    def isConstant(self, token):
        if token.isnumeric():
            return True
        
        if token == "Adevarat" or token == "Fals":
            return True 
        
        if token[0] == '"' and token[-1] == '"':
            return True
        
    def isToken(self, token):
        return token in self.token_list
    
    def run(self, file_name):
        content = self.process_file(file_name)

        for line in content:
            for element in line:
                if self.isToken(element):
                    self.pif.add(element, [-1,-1])
                elif self.isConstant(element):
                    pos = self.st.insert(element)
                    self.pif.add("const", pos)
                elif self.isIdentifier(element):
                    pos = self.st.insert(element)
                    self.pif.add("ID", pos)
                else:
                    print("Lexical error at " + element)

if __name__  == "__main__":
    ls = lexicScanner()

    # print("Running p1.txt")
    # ls.run("./problems/p1.txt")

    # print("Running p2.txt")
    # ls.run("./problems/p2.txt")
    # ls.pif.display()

    print("Running p3.txt")
    ls.run("./problems/p3.txt")
    ls.pif.display()
    ls.st.display()


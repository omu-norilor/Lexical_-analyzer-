from transition import Transition
from helpers import readFileToList, splitString, readUserInput
class FiniteAutomata ():

    def __init__(self,filename): 
        self.filename = filename
        self.states = [] # list of strings
        self.alphabet = [] # list of strings
        self.finalStates = []# list of strings
        self.transitions = [] # list of transitions
        self.initialState = ""
        self.readFromFile()

    def readFromFile(self) :
        lines = readFileToList(self.filename)
        self.states = splitString(lines[0])
        self.alphabet = splitString(lines[1])
        self.initialState = lines[2]
        self.finalStates = splitString(lines[3])
        for i in range(4, len(lines)):
            tokens = lines[i].split(" ")
            self.transitions.append(Transition(tokens[0], tokens[2], tokens[1]))

    def isDeterministic(self):
        for state in self.states:
            for  symbol in self.alphabet:
                if (len(self.getTransitionsFromStateAndSymbol(state, symbol)) > 1):
                    return False
        return True

    def getTransitionsFromStateAndSymbol(self,state,symbol): 
        result = []
        for transition in self.transitions:
            if transition.getFromState()==state and transition.getSymbol()==symbol:
                result.append(transition)
        return result

    def printElements(self, elements):
        result = []
        for state in elements:
            result.append(state)
        print(result)

    def printStates(self):
        self.printElements(self.states)

    def printAlphabet(self):
        self.printElements(self.alphabet)

    def printFinalStates(self):
        self.printElements(self.finalStates)

    def printTransitions(self): 
        for transition in self.transitions:
            print(transition)

    def printInitialState(self):
        print(self.initialState)

    def printMenu(self):
        print("1. Print states")
        print("2. Print alphabet")
        print("3. Print transitions")
        print("4. Print initial state")
        print("5. Print final states")

    def displayThings(self):
        while (True):
            self.printMenu()
            input = readUserInput("Enter the input: ")
            if (input == ""):
                print("The input is empty.")
                return
        
            if input == "1": self.printStates()
            elif input == "2": self.printAlphabet()
            elif input == "3": self.printTransitions()
            elif input == "4": self.printInitialState()
            elif input == "5": self.printFinalStates()
            else: print("My work is done here."); return

    def checkAccepted(self, sequence):
        return self.checkAcceptedRec(sequence, self.initialState, 0)
        
    def checkAcceptedRec(self, sequence, currentState, count):

        if (count == len(sequence)):
            return currentState in self.finalStates
        
        if (count > len(sequence)):
            return False
        
        if (count < len(sequence)):
            symbol = str(sequence[count])
            
            transitions = self.getTransitionsFromStateAndSymbol(currentState, symbol)
            if (len(transitions)== 0):
                return False
            
            values=[]
            for transition in transitions:
                values.append(self.checkAcceptedRec(sequence, transition.getToState(), count+1))
            return True in values


if __name__ == "__main__":
    fa = FiniteAutomata("./rules/fa.in")
    if fa.isDeterministic():
        print("The automata is deterministic.")
        print(f"for 0  accepted status is {fa.checkAccepted('0')}")
        print(f"for 01 accepted status is {fa.checkAccepted('01')}")
        print(f"for 1  accepted status is {fa.checkAccepted('1')}")
        print(f"for '' accepted status is {fa.checkAccepted('')}")
    else:
        print("The automata is not deterministic.")

    print(" ")
    fa.displayThings()
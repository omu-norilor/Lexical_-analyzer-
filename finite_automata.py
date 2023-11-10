from transition import Transition
from helpers import readFileToList, readUserInput
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
        self.states = lines[0].split(" ")
        self.alphabet = lines[1].split(" ")
        self.initialState = lines[2]
        self.finalStates = lines[3].split(" ")
        for i in range(4, len(lines)):
            tokens = lines[i].split(" ")
            fromState = tokens[0]
            toState = tokens[-1]
            symbols = tokens[1:-1]
            self.transitions.append(Transition(fromState, toState, symbols))

    def isDeterministic(self):
        for state in self.states:
            for  symbol in self.alphabet:
                if (len(self.getTransitionsFromStateAndSymbol(state, symbol)) > 1):
                    return False
        return True

    def getTransitionsFromStateAndSymbol(self,state,symbol): 
        result = []
        for transition in self.transitions:
            if transition.getFromState()==state and symbol in transition.getSymbols():
                result.append(transition)
        return result

    def getStates(self):
        return self.states

    def getAlphabet(self):
        return self.alphabet

    def getFinalStates(self):
        return self.finalStates

    def getTransitions(self): 
        return self.transitions

    def getInitialState(self):
        return self.initialState
    
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

    def printInfo(self):
        print(f"States: {self.getStates()}")
        print(f"Alphabet: {self.getAlphabet()}")
        print(f"Transitions: ")
        for transition in self.getTransitions(): print(transition)
        print(f"Initial state: {self.getInitialState()}")
        print(f"Final states: {self.getFinalStates()}")
        print(" ")

if __name__ == "__main__":
    fa = FiniteAutomata("./rules/fa_dummy.in")

    fa.printInfo()

    if fa.isDeterministic():
        print("The automata is deterministic.")
        print(f"for 0  accepted status is {fa.checkAccepted('0')}")
        print(f"for 01 accepted status is {fa.checkAccepted('01')}")
        print(f"for 1  accepted status is {fa.checkAccepted('1')}")
        print(f"for '' accepted status is {fa.checkAccepted('')}")
    else:
        print("The automata is not deterministic.")

    
class Transition():

    def __init__(self,fromState, toState, symbol):
        self.fromState = fromState
        self.toState = toState
        self.symbol = symbol

    def getFromState(self):
        return self.fromState

    def setFromState(self, fromState):
        self.fromState = fromState

    def getToState(self):
        return self.toState

    def setToState(self, toState):
        self.toState = toState

    def getSymbol(self):
        return self.symbol

    def setSymbol(self, symbol):
        self.symbol = symbol

    def __str__(self):
        return "d(" + self.fromState + ", " + self.symbol + ") = " + self.toState
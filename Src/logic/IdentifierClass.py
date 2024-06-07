class Identifier:

    def __init__(self):
        self.name = None
        self.fileName = None
        self.lineNo = None
        self.tokenType = None
        self.value = None
        self.varOrReturnType = None

    def printId(self):
        print(
            f"The name is : {self.name}, The file name is : {self.fileName}, The line number is : {self.lineNo}, "
            f"The token type is : {self.tokenType}, The value is : {self.value}, "
            f"var or return type : {self.varOrReturnType}")
        print("*******************************************************************************************************")


class AllFileTokens:
    def __init__(self):
        self.allTokens = []

    def addId(self, identifier):
        self.allTokens.append(identifier)

    def getList(self):
        return self.allTokens.copy()

    def printList(self):
        for identifier in self.allTokens:
            if identifier.name is not None and identifier.fileName is not None and identifier.lineNo is not None:
                identifier.printId()

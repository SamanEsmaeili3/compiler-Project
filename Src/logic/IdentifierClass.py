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
            f"The token type is : {self.tokenType}, The value is : {self.value}, var or return type : {self.varOrReturnType}")
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
            identifier.printId()

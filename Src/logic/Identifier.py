class Identifier:

    def __init__(self):
        self.name = ""
        self.fileName = None
        self.lineNo = None
        self.tokenType = None
        self.value = None
        self.varOrReturnType = None
        self.editedName = None

    def printId(self):
        print(
            f"The name is : {self.name}, The file name is : {self.fileName}, The line number is : {self.lineNo}, "
            f"The token type is : {self.tokenType}, The value is : {self.value}, "
            f"var or return type : {self.varOrReturnType}, edited Name is : {self.editedName}")
        print("*******************************************************************************************************")

    def setEditedName(self, name):
        self.editedName = name

    def getAtr(self):
        return self.name, self.tokenType, self.fileName

    def __eq__(self, other):
        if self.name == other.name and self.value == other.value and self.type == other.type and self.fileName == other.fileName:
            return True
        else:
            return False

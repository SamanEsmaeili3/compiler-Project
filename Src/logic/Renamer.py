from Src.logic.JavaParserListener import JavaParserListener
from JavaParser import *
from Src.logic.Executer import *
from Src.logic.Identifier import *


class Renamer(JavaParserListener):
    def __init__(self, currentFile, executer):
        self.executer = executer
        self.currentFile = currentFile
        self.out = []
        self.dicOfTypes = {
            7: [7, 51, 104, 25, 111, 82, 41],
            11: [11, 104, 82, 51],
            20: [20, 98, 99],
            38: [38, 104, 99, 98],
            13: [13, 99, 104],
            15: [15, 51, 82],
            35: [35, 98, 20],
            31: [31, 104]
        }

    def enterIdentifier(self, ctx: JavaParser.IdentifierContext):
        tokenType = ctx.parentCtx.getRuleIndex()
        for identifier in self.executer.identifierList.identifiers:
            self.changeIdentifier(ctx, identifier, tokenType)

    def enterTypeIdentifier(self, ctx: JavaParser.TypeIdentifierContext):
        tokenType = ctx.getRuleIndex()
        for identifier in self.executer.identifierList.identifiers:
            self.changeIdentifier(ctx, identifier, tokenType)

    def changeIdentifier(self, ctx, identifier: Identifier, tokenType):
        name = ctx.getText()
        token = ctx.start

        # print("---------------------------------------------")
        # print(identifier.printId())
        if identifier.name == name:
            if tokenType in self.dicOfTypes[identifier.tokenType]:
                if name not in self.executer.ignoreClasses:
                    token.text = identifier.editedName

    def visitTerminal(self, node):
        token = node.symbol
        if token is not None:
            self.out.append(token.text)
        return super().visitTerminal(node)

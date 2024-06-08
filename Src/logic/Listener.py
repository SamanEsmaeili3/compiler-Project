from Src.logic import IdentifierList
from Src.logic.JavaParserListener import JavaParserListener
from JavaParser import *
import Identifier


class Listener(JavaParserListener):

    def __init__(self, currentFile, executer):
        self.out = []
        self.identifier = Identifier.Identifier()
        self.identifiers = IdentifierList.IdentifierList()
        self.executer = executer
        self.currentFile = currentFile
        self.vars = []
        self.methods = []
        self.classes = []
        self.enumDeclaration = []
        self.enumConstant = []
        self.interfaceDeclaration = []
        self.constantDeclarator = []
        self.interfaceCommonBodyDeclaration = []
        self.types = []
        self.values = []

    def enterIdentifier(self, ctx: JavaParser.IdentifierContext):
        # ctxNum = ctx.parentCtx.getRuleIndex()  #thiese three lines used for debuging
        # ctxName = ctx.getChild(0).getText()
        # ctx_P = ctx.parentCtx.parentCtx.getRuleIndex()
        # ctxToken = ctx.start

        if ctx.parentCtx.getRuleIndex() == 11:
            self.enumDeclaration.append(ctx.getChild(0).getText())
            self.identifier.name = ctx.getChild(0).getText()
            self.identifier.fileName = self.currentFile
            self.identifier.lineNo = ctx.start.line
            self.identifier.tokenType = 11

        elif ctx.parentCtx.getRuleIndex() == 13:
            self.enumConstant.append(ctx.getChild(0).getText())
            self.identifier.name = ctx.getChild(0).getText()
            self.identifier.fileName = self.currentFile
            self.identifier.lineNo = ctx.start.line
            self.identifier.tokenType = 13

        elif ctx.parentCtx.getRuleIndex() == 15:
            self.interfaceDeclaration.append(ctx.getChild(0).getText())
            self.identifier.name = ctx.getChild(0).getText()
            self.identifier.fileName = self.currentFile
            self.identifier.lineNo = ctx.start.line
            self.identifier.tokenType = 15

        elif ctx.parentCtx.getRuleIndex() == 31:
            self.constantDeclarator.append(ctx.getChild(0).getText())
            self.identifier.name = ctx.getChild(0).getText()
            self.identifier.fileName = self.currentFile
            self.identifier.lineNo = ctx.start.line
            self.identifier.tokenType = 31

        elif ctx.parentCtx.getRuleIndex() == 35:
            self.interfaceCommonBodyDeclaration.append(ctx.getChild(0).getText())
            self.identifier.name = ctx.getChild(0).getText()
            self.identifier.fileName = self.currentFile
            self.identifier.lineNo = ctx.start.line
            self.identifier.tokenType = 35

        elif ctx.parentCtx.getRuleIndex() == 7:
            self.classes.append(ctx.getChild(0).getText())
            self.identifier.name = ctx.getChild(0).getText()
            self.identifier.fileName = self.currentFile
            self.identifier.lineNo = ctx.start.line
            self.identifier.tokenType = 7
            self.identifier.varOrReturnType = self.identifier.name
            self.identifier.value = "null"

        elif ctx.parentCtx.getRuleIndex() == 38:
            self.vars.append(ctx.getChild(0).getText())
            self.identifier.name = ctx.getChild(0).getText()
            self.identifier.fileName = self.currentFile
            self.identifier.lineNo = ctx.start.line
            self.identifier.tokenType = 38

        elif ctx.parentCtx.getRuleIndex() == 20:
            self.methods.append(ctx.getChild(0).getText())
            self.identifier.name = ctx.getChild(0).getText()
            self.identifier.fileName = self.currentFile
            self.identifier.lineNo = ctx.start.line
            self.identifier.tokenType = 20

        # elif ctx.parentCtx.getRuleIndex() == 25:   //Constructor method
        #     self.methods.append(ctx.getChild(0).getText())
        #     self.identifier.name = ctx.getChild(0).getText()
        #     self.identifier.fileName = self.currentFile
        #     self.identifier.lineNo = ctx.start.line
        #     self.identifier.tokenType = 20
        #     self.identifier.varOrReturnType = self.identifier.name

        if ctx.parentCtx.getRuleIndex() in [7, 11, 20, 13, 15, 35, 31, 38]:
            self.identifier.setEditedName(createNewName(self.identifier.name))
            self.addToList()
        # if ctx.parentCtx.parentCtx.getRuleIndex() == 47:
        #     self.identifier.setEditedName(createNewName(self.identifier.name))
        #     self.addToList()  #method argument Rule index

    def enterVariableInitializer(self, ctx: JavaParser.ElementValueContext):
        self.identifier.value = ctx.getChild(0).getText()
        self.values.append(ctx.getChild(0).getText())
        self.identifier.setEditedName(createNewName(self.identifier.name))
        self.addToList()

    def enterTypeType(self, ctx: JavaParser.LocalVariableDeclarationContext):
        # print(3)
        # print(ctx.getRuleIndex())
        # print("TYPE IS: ")
        # print(ctx.getText())
        tup = ctx.getText()
        self.identifier.varOrReturnType = ctx.getText()
        self.types.append(ctx.getText())

    def enterMethodDeclaration(self, ctx: JavaParser.MethodDeclarationContext):
        # print(4)
        self.identifier.varOrReturnType = ctx.getChild(0).getText()
        self.identifier.value = "null"
        # print(ctx.getChild(0).getText())

    def exitCompilationUnit(self, ctx: JavaParser.CompilationUnitContext):
        # print(6)
        print("*************************************************")
        print("vars: ", self.vars)
        print("methods: ", self.methods)
        print("classes: ", self.classes)
        print("enumConstant", self.enumConstant)
        print("enumDeclaration: ", self.enumDeclaration)
        print("constantDeclarator: ", self.constantDeclarator)
        print("interfaceDeclaration: ", self.interfaceDeclaration)
        print("interfaceCommonBodyDeclaration: ", self.interfaceCommonBodyDeclaration)
        print("Values: ", self.values)
        print("types: ", self.types)
        print("*************************************************")

        # self.identifiers.printList()

    def identifierList(self):
        return self.identifiers

    def addToList(self):
        self.identifiers.addId(self.identifier)
        self.identifier = Identifier.Identifier()


def createNewName(name):
    n = str(name)
    return f'New_{n}'

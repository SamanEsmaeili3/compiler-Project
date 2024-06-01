from Src.logic.JavaParserListener import JavaParserListener
from JavaParser import *
import IdentifierClass


class Listener(JavaParserListener):

    def __init__(self, currentFile, executer):
        self.out = []
        self.identifier = IdentifierClass.Identifier()
        self.AllFileTokens = IdentifierClass.AllFileTokens()
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

        # print(ctx.getText(), ctx.parentCtx.getRuleIndex())
        # if var --> add var to self.vars
        # ...
        print(1)
        print(ctx.getChild(0).getText())
        if ctx.parentCtx.getRuleIndex() == 11:
            self.enumDeclaration.append(ctx.getChild(0).getText())
            self.identifier.name = ctx.getChild(0).getText()
            self.identifier.fileName = self.currentFile
            self.identifier.lineNo = ctx.start.line
            self.identifier.tokenType = 11

        if ctx.parentCtx.getRuleIndex() == 13:
            self.enumConstant.append(ctx.getChild(0).getText())
            self.identifier.name = ctx.getChild(0).getText()
            self.identifier.fileName = self.currentFile
            self.identifier.lineNo = ctx.start.line
            self.identifier.tokenType = 13

        if ctx.parentCtx.getRuleIndex() == 15:
            self.interfaceDeclaration.append(ctx.getChild(0).getText())
            self.identifier.name = ctx.getChild(0).getText()
            self.identifier.fileName = self.currentFile
            self.identifier.lineNo = ctx.start.line
            self.identifier.tokenType = 15

        if ctx.parentCtx.getRuleIndex() == 31:
            self.constantDeclarator.append(ctx.getChild(0).getText())
            self.identifier.name = ctx.getChild(0).getText()
            self.identifier.fileName = self.currentFile
            self.identifier.lineNo = ctx.start.line
            self.identifier.tokenType = 31

        if ctx.parentCtx.getRuleIndex() == 35:
            self.interfaceCommonBodyDeclaration.append(ctx.getChild(0).getText())
            self.identifier.name = ctx.getChild(0).getText()
            self.identifier.fileName = self.currentFile
            self.identifier.lineNo = ctx.start.line
            self.identifier.tokenType = 35

        if ctx.parentCtx.getRuleIndex() == 7:
            self.classes.append(ctx.getChild(0).getText())
            self.identifier.name = ctx.getChild(0).getText()
            self.identifier.fileName = self.currentFile
            self.identifier.lineNo = ctx.start.line
            self.identifier.tokenType = 7
            self.identifier.varOrReturnType = self.identifier.name
            self.identifier.value = "null"

        if ctx.parentCtx.getRuleIndex() == 38:
            self.vars.append(ctx.getChild(0).getText())
            self.identifier.fileName = self.currentFile
            self.identifier.name = ctx.getChild(0).getText()
            self.identifier.fileName = self.currentFile
            self.identifier.lineNo = ctx.start.line
            self.identifier.tokenType = 38

        if ctx.parentCtx.getRuleIndex() == 20:
            self.methods.append(ctx.getChild(0).getText())
            self.identifier.name = ctx.getChild(0).getText()
            self.identifier.fileName = self.currentFile
            self.identifier.lineNo = ctx.start.line
            self.identifier.tokenType = 20
            # if self.identifier.value == "null" or self.identifier.varOrReturnType == "void":
            # self.AllFileTokens.addId(self.identifier)
            # self.identifier = IdentifierClass.Identifier()

        # print(ctx.getText(), ctx.start.line)
        # print(ctx.IDENTIFIER().getSymbol().line)

        # print(f"Line number is : {ctx.IDENTIFIER().getSymbol().line}")
        # self.identifier.lineNo = ctx.IDENTIFIER().getSymbol().line
        # print("------------------------------------------------------------")
        # self.identifier.printId()

        # print(ctx.getChild(0), " rule index: ", ctx.parentCtx.getRuleIndex())

    def enterVariableDeclarator(self, ctx: JavaParser.VariableDeclaratorContext):
        print(1.9)
        # print(ctx.getChild(2).getText())

        # self.identifier.value = ctx.getChild(2).getText()

    def enterVariableInitializer(self, ctx: JavaParser.ElementValueContext):
        print(f"(", ctx.getChild(0).getText(), ")")
        print(ctx.getRuleIndex())
        print(2)
        self.identifier.value = ctx.getChild(0).getText()
        self.values.append(ctx.getChild(0).getText())
        self.AllFileTokens.addId(self.identifier)
        self.identifier = IdentifierClass.Identifier()
        print("------------------------------------------------------------")
        # self.identifier.printId()
        # self.AllFileTokens.addId(self.identifier)
        # self.identifier = IdentifierClass.Identifier()
        # if self.identifier.tokenType == 20:
        # if self.identifier.value == "null" or self.identifier.varOrReturnType == "void":
        # self.AllFileTokens.addId(self.identifier)
        # self.identifier = IdentifierClass.Identifier()

    def enterTypeType(self, ctx: JavaParser.LocalVariableDeclarationContext):
        print(3)
        # print("TYPE IS: ")
        # print(ctx.getText())
        self.identifier.varOrReturnType = ctx.getText()
        self.types.append(ctx.getText())
        # self.identifier.fileName = self.currentFile

    def enterMethodDeclaration(self, ctx: JavaParser.MethodDeclarationContext):
        print(4)
        self.identifier.varOrReturnType = ctx.getChild(0).getText()
        self.identifier.value = "null"
        # print(ctx.getChild(0).getText())

    def exitIdentifier(self, ctx: JavaParser.IdentifierContext):
        print(5)
        print("{", ctx.parentCtx.getRuleIndex(), "}")
        if (ctx.parentCtx.getRuleIndex() != 31) and (ctx.parentCtx.getRuleIndex() != 38):
            self.AllFileTokens.addId(self.identifier)
            self.identifier = IdentifierClass.Identifier()
        print("----------------------------------------------")

    def exitCompilationUnit(self, ctx: JavaParser.CompilationUnitContext):
        print(6)
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
        self.AllFileTokens.printList()

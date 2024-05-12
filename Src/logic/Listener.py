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

    def enterIdentifier(self, ctx: JavaParser.IdentifierContext):

        # print(ctx.getText(), ctx.parentCtx.getRuleIndex())
        # if var --> add var to self.vars
        # ...

        if ctx.parentCtx.getRuleIndex() == 11:
            self.enumDeclaration.append(ctx.getChild(0).getText())
            self.identifier.fileName = self.currentFile
            self.identifier.lineNo = ctx.start.line
            self.identifier.tokenType = 11
            self.identifier.name = ctx.getChild(0).getText()

        elif ctx.parentCtx.getRuleIndex() == 13:
            self.enumConstant.append(ctx.getChild(0).getText())
            self.identifier.fileName = self.currentFile
            self.identifier.lineNo = ctx.start.line
            self.identifier.tokenType = 13
            self.identifier.name = ctx.getChild(0).getText()

        elif ctx.parentCtx.getRuleIndex() == 15:
            self.interfaceDeclaration.append(ctx.getChild(0).getText())
            self.identifier.fileName = self.currentFile
            self.identifier.lineNo = ctx.start.line
            self.identifier.tokenType = 15
            self.identifier.name = ctx.getChild(0).getText()

        elif ctx.parentCtx.getRuleIndex() == 31:
            self.constantDeclarator.append(ctx.getChild(0).getText())
            self.identifier.fileName = self.currentFile
            self.identifier.lineNo = ctx.start.line
            self.identifier.tokenType = 31
            self.identifier.name = ctx.getChild(0).getText()

        elif ctx.parentCtx.getRuleIndex() == 35:
            self.interfaceCommonBodyDeclaration.append(ctx.getChild(0).getText())
            self.identifier.fileName = self.currentFile
            self.identifier.lineNo = ctx.start.line
            self.identifier.tokenType = 35
            self.identifier.name = ctx.getChild(0).getText()

        elif ctx.parentCtx.getRuleIndex() == 7:
            self.classes.append(ctx.getChild(0).getText())
            self.identifier.fileName = self.currentFile
            self.identifier.lineNo = ctx.start.line
            self.identifier.tokenType = 7
            self.identifier.name = ctx.getChild(0).getText()
            self.identifier.varOrReturnType = self.identifier.name
            self.AllFileTokens.addId(self.identifier)
            self.identifier = IdentifierClass.Identifier()

        elif ctx.parentCtx.getRuleIndex() == 38:
            self.identifier.fileName = self.currentFile
            self.vars.append(ctx.getChild(0).getText())
            self.identifier.lineNo = ctx.start.line
            self.identifier.tokenType = 38
            self.identifier.name = ctx.getChild(0).getText()

        elif ctx.parentCtx.getRuleIndex() == 20:
            self.identifier.fileName = self.currentFile
            self.methods.append(ctx.getChild(0).getText())
            self.identifier.lineNo = ctx.start.line
            self.identifier.tokenType = 20
            self.identifier.name = ctx.getChild(0).getText()
            if self.identifier.varOrReturnType is None:
                self.identifier.varOrReturnType = "void"
            if self.identifier.value is None:
                self.identifier.value = "null"
            # if self.identifier.value == "null" or self.identifier.varOrReturnType == "void":
            # self.AllFileTokens.addId(self.identifier)
            # self.identifier = IdentifierClass.Identifier()

        # print(ctx.getText(), ctx.start.line)
        # print(ctx.IDENTIFIER().getSymbol().line)

        print(f"Line number is : {ctx.IDENTIFIER().getSymbol().line}")
        self.identifier.lineNo = ctx.IDENTIFIER().getSymbol().line
        print("------------------------------------------------------------")
        self.identifier.printId()

        print(ctx.getChild(0), " rule index: ", ctx.parentCtx.getRuleIndex())

    def enterVariableInitializer(self, ctx: JavaParser.ElementValueContext):
        print(ctx.getChild(0).getText())
        self.identifier.value = ctx.getChild(0).getText()
        print("------------------------------------------------------------")
        self.identifier.printId()
        self.AllFileTokens.addId(self.identifier)
        self.identifier = IdentifierClass.Identifier()
        if self.identifier.tokenType == 20:
            if self.identifier.value == "null" or self.identifier.varOrReturnType == "void":
                self.AllFileTokens.addId(self.identifier)
                self.identifier = IdentifierClass.Identifier()

    def enterTypeType(self, ctx: JavaParser.LocalVariableDeclarationContext):
        print(ctx.getText())
        self.identifier.varOrReturnType = ctx.getText()
        self.identifier.fileName = self.currentFile

    def enterMethodDeclaration(self, ctx: JavaParser.MethodDeclarationContext):
        print(ctx.getChild(0).getText())

    def exitCompilationUnit(self, ctx: JavaParser.CompilationUnitContext):
        print("*************************************************")
        print("vars: ", self.vars)
        print("methods: ", self.methods)
        print("classes: ", self.classes)
        print("enumConstant", self.enumConstant)
        print("enumDeclaration: ", self.enumDeclaration)
        print("constantDeclarator: ", self.constantDeclarator)
        print("interfaceDeclaration: ", self.interfaceDeclaration)
        print("interfaceCommonBodyDeclaration: ", self.interfaceCommonBodyDeclaration)
        print("*************************************************")
        # self.AllFileTokens.printList()

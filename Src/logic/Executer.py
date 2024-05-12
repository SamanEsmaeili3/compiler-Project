import os

from Listener import *
from Src.logic.JavaLexer import JavaLexer


class Executer:
    def __init__(self, files):
        self.fileNames, self.filePaths = files
        self.extractor = None
        self.renamer = None
        self.fileCopies = []

    def readJavaFile(self, filepath: str):
        context = None
        readingJavaFile = filepath
        try:
            context = open(readingJavaFile, "r")
        except IOError:
            print("Something went wronged reading the file")
        return context.read()

    def executeFiles(self):
        self.makeTable()

    def makeTable(self):
        for i in range(len(self.filePaths)):

            input_text = self.readJavaFile(os.path.join(self.filePaths[i], self.fileNames[i]))
            input_stream = InputStream(input_text)
            lexer = JavaLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = JavaParser(stream)
            tree = parser.compilationUnit()  # Parse the entire compilation unit
            self.extractor = Listener(self.filePaths[i], self)
            walker = ParseTreeWalker()
            walker.walk(self.extractor, tree)
            fileCopy = ' '.join(self.extractor.out)
            self.fileCopies.append(fileCopy)

    def makeOutput(self, i, final_output_with_replaced_classes):
        javaFileName = f'New_{self.fileNames[i]}'
        writePath = self.filePaths[i].replace('input', 'output')
        if not os.path.exists(writePath):
            os.makedirs(writePath)
        with open(os.path.join(writePath, javaFileName), "w") as java_file:
            print(os.path.join(writePath, javaFileName))
            java_file.write(final_output_with_replaced_classes)

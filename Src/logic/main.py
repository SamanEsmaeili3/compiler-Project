from os import walk
from Executer import *


def main():
    executor = Executer(getFilePaths())
    executor.executeFiles()


def getFilePaths():
    names = []
    filepaths = []

    final_path = os.path.join(os.path.dirname(__file__), '..', 'JavaFiles', 'input', 'main')
    w = walk(final_path)
    for (dirpath, dirnames, filenames) in w:
        for filename in filenames:
            if filename.endswith(".java"):
                names.append(filename)
                filepaths.append(dirpath)
    return names, filepaths


if __name__ == "__main__":
    main()

from typing import Any

NUMBER = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
NEWLINE = '\n'
DOT = '.'
SPACE = ' '

class Parser:
    def __init__(self,filepath):
        self.__filePath = filepath
    
    def openFile(self) -> list[str]:
        with open(self.__filePath, 'r') as file:
            contents = file.readlines()
        return contents

    def parseInteger(num: list[str]) -> int:
        integer = 0
        degree = 0
        index = len(num) - 1
        for i in range(len(num)):
            integer = integer + (int(num[index]) * (10 ** degree))
            degree = degree + 1
            index = index - 1
        return integer
    
    def parseFraction(frac: list[str]) -> float:
        fraction = 0
        for i in range(len(frac)):
            degree = i + 1
            fraction = fraction + (int(frac[i]) * (10 ** (-degree)))
        return fraction

    def parseFile(self) -> Any:
        contents = self.openFile()
        listContents = list(contents)
        listInt = []
        listFrac = []
        resultMatrix = []

        for i in range(len(listContents)):
            j = 0
            EOL = False
            STOP = False
            FRAC = False
            rowMatrix = []
            while(j < len(listContents[i]) and (not EOL)):
                STOP = False
                numInt = 0
                numFrac = 0
                number = 0
                while ((not STOP) and (not EOL)):
                    if (listContents[i][j] in NUMBER):
                        if (not FRAC):
                            listInt.append(listContents[i][j])
                        else:
                            listFrac.append(listContents[i][j])
                    elif (listContents[i][j] is SPACE):
                        FRAC = False
                        STOP = True
                    elif (listContents[i][j] is DOT):
                        FRAC = True
                    elif (listContents[i][j] is NEWLINE):
                        STOP = True
                        EOL = True
                    else:
                        raise Exception("InvalidInputException")

                    if ((i == len(listContents)-1) and (j == len(listContents[i])-1)):
                        STOP = True

                    j = j + 1

                if STOP:
                    numInt = Parser.parseInteger(listInt)
                    numFrac = Parser.parseFraction(listFrac)
                    number = numInt + numFrac
                    rowMatrix.append(number)
                    listInt.clear()
                    listFrac.clear()

            resultMatrix.append(rowMatrix)
        return resultMatrix
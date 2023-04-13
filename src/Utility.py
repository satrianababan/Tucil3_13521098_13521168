def read_file(filename):
    file = filename.read().splitlines()
    banyak = int(file[0])
    matriks = []
    koordinat = []
    matriksToFloat = [[0 for i in range(banyak)] for j in range(banyak)]
    CoorToFloat = [[0 for i in range(2)] for j in range(banyak)]
    for i in range(banyak):
        line = file[i+2]
        matriks.append(line)
        koor = file[i+2+banyak]
        koordinat.append(koor)
        matriksToFloat[i] = [float(x) for x in matriks[i].split()]
        CoorToFloat[i] = [float(x) for x in koordinat[i].split()]
        if(isSquareMatrix(matriksToFloat) and isSymmetricMatrix(matriksToFloat) and isNumberEqualsMatrix(matriksToFloat)):
            return file,matriksToFloat,CoorToFloat
        else:
            raise Exception

def isSquareMatrix(matrix:list[list[float]]) -> bool:
    square = True
    rowCount = len(matrix)
    columnCount = len(matrix[0])
    if(rowCount != columnCount):
        square = False
    else:
        i = 0
        while(i < len(matrix) and square):
            if (len(matrix[i]) != columnCount):
                square = False
            i = i + 1
    return square

def isNumberEqualsMatrix(number:int,matrix:list[list[int]]) -> bool:
    if(number == len(matrix)):
        return True
    else:
        return False
    
def isSymmetricMatrix(matrix:list[list[float]]) -> bool:
    symmetric = True
    i = 0
    while (i < len(matrix) and symmetric):
        j = 0
        while(j < len(matrix[i]) and symmetric):
            if(matrix[i][j] != matrix[j][i]):
                symmetric = False
            j = j + 1
        i = i + 1
    return symmetric
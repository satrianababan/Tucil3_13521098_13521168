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
    return file,matriksToFloat,CoorToFloat

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
    return square

def isNumberEqualsMatrix(number:int,matrix:list[list[int]]) -> bool:
    if(number == len(matrix)):
        return True
    else:
        return False
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
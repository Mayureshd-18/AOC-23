with open("input_1.txt") as f:
    # Read the lines
    data = f.read()
    lines = data.splitlines()

    mat = []
    for line in lines:
        mat.append(list(line))

    print(*mat, sep="\n")

    #Expand rows

    rows = []

    for i in range(len(mat)):
        if '#' not in mat[i]:
            rows.append(i)

    t = 0
    for i in rows:
        mat.insert(i+1+t, ['.']*len(mat[0]))
        t+=1


    print()
    print(*mat, sep="\n")

    #Expand cols
    mat = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

    cols = []

    for i in range(len(mat)):
        if '#' not in mat[i]:
            cols.append(i)

    print(cols)
    t = 0
    for i in cols:
        mat.insert(i+1+t, ['.']*len(mat[0]))
        t+=1

    mat = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

    print()
    print(*mat, sep="\n")


    #Find coords for all the galaxies
    coords = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == '#':
                coords.append([i,j])


    print(coords)

    res = 0

    #Find the manhattan distance between all
    for i in range(len(coords)):
        for j in range(i+1, len(coords)):
            res+= (abs(coords[i][0] - coords[j][0]) + abs(coords[i][1] - coords[j][1]))

    print(res)




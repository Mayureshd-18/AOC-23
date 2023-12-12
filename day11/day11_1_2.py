
#Without manipulating the physical universe
with open("input_1.txt") as f:
    # Read the lines
    data = f.read()
    lines = data.splitlines()

    mat = []
    for line in lines:
        mat.append(list(line))

    print(*mat, sep="\n")

    rows = []
    for i in range(len(mat)):
        if '#' not in mat[i]:
            rows.append(i)
    print(rows)

    mat = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
    cols = []
    for i in range(len(mat)):
        if '#' not in mat[i]:
            cols.append(i)
    mat = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
    print(cols)

    coords = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == '#':
                coords.append([i, j])

    print(coords)


    def count_elements_in_range(arr, start_range, end_range):
        start = min(start_range, end_range)
        end = max(start_range, end_range)
        return sum(start < num < end for num in arr)


    res = 0

    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            res += ((abs(coords[i][0] - coords[j][0]) + count_elements_in_range(rows, coords[i][0],
                                                                                coords[j][0])) + (
                                abs(coords[i][1] - coords[j][1]) + count_elements_in_range(cols, coords[i][1],
                                                                                           coords[j][1])))
    print(res)




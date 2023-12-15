import rotate_matrix

def rotate(matrix):
    temp_matrix = []
    column = len(matrix) - 1
    for column in range(len(matrix)):
        temp = []
        for row in range(len(matrix) - 1, -1, -1):
            temp.append(matrix[row][column])
        temp_matrix.append(temp)

    print(*temp_matrix, sep="\n")
    # for i in range(len(matrix)):
    #     for j in range(len(matrix)):
    #         matrix[i][j] = temp_matrix[i][j]
    return matrix

with open("input_1.txt") as f:
    data = f.read()
    lines = data.splitlines()

    # lines = rotate(lines)
    print(*lines, sep="\n")


    for _ in range (1000000000):

        for r in range(4):
            if r==0:
                lines = rotate_matrix.clockwise(lines)
            else:
                lines = rotate_matrix.anti_clockwise(lines)


            # print(*lines, sep="\n")
            # print("\n")

            for l in range(len(lines)):
                ctr = 0
                line = lines[l]
                temp = []
                for i in range(len(line)):
                    if line[i] == 'O':
                        temp.insert(ctr, line[i])
                        ctr+=1

                    elif line[i] == '#':
                        ctr = i
                        temp.insert(ctr, line[i])
                        ctr+=1
                    else:
                        temp.insert(ctr, line[i])

                lines[l] = list(temp)

            # print(*lines, sep="\n")
            # print("\n")
        for i in range(2):
            lines = rotate_matrix.anti_clockwise(lines)

    # print(*lines, sep="\n")
    # print("\n")

    #
    res = 0
    for i in lines:
        for j in range(len(i)):
            if i[j] == 'O':
                res+= 10 - j

    print(res)





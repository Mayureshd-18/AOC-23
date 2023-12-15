with open("input_1.txt") as f:
    data = f.read()
    lines = data.splitlines()

    lines = [[lines[j][i] for j in range(len(lines))] for i in range(len(lines[0]))]

    print(*lines, sep="\n")

    res = 0

    for line in lines:
        temp = 0
        ctr = 100
        flag = False
        for i in range(len(line)):
            # print(line[i], line[i] == 'O')
            if line[i] == 'O':
                temp+= ctr
                ctr-=1
            elif line[i] == '#':
                ctr = 100 - i - 1
        print(temp)
        res+= temp
    print(res)
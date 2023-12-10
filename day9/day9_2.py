with open("input_1.txt") as f:
    # Read the lines
    data = f.read()
    lines = data.splitlines()


    res = 0

    for line in lines:
        data = []
        data.append(list(map(int, line.split())))
        # print(data)

        while any(element != 0 for element in data[-1]):
            temp = [data[-1][i+1] - data[-1][i] for i in range(len(data[-1])-1)]
            data.append(temp)

        # print(data)

        #Insert the difference at the start
        for j in range(len(data)-2, -1, -1):
            data[j].insert(0,data[j][0] - data[j+1][0])

        print(data)

        #In this we need the first element not the last
        res+= data[0][0]

    print(res)

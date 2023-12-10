with open("input_1.txt") as f:
    # Read the lines
    data = f.read()
    lines = data.splitlines()

    #var to store the answer
    res = 0

    for line in lines:

        data = [list(map(int, line.split()))]
        # print(data)

        #While not all the elements are 0, continue calculating the differences
        #and append them to the data
        while any(element != 0 for element in data[-1]):
            temp = [data[-1][i+1] - data[-1][i] for i in range(len(data[-1])-1)]
            data.append(temp)

        # print(data)

        #Iterate from the second last element in reverse order and append the sum
        #of the current last element and the last element of the next list i.e. the difference
        for j in range(len(data)-2, -1, -1):
            data[j].append(data[j+1][-1] + data[j][-1])

        print(data)

        #Add the first element to the var
        res+= data[0][-1]

    print(res)

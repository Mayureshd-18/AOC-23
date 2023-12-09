import math
with open("input_1.txt") as f:

    #Read the lines
    data = f.read()
    lines = data.splitlines()

    mapper = {}
    #First line is the sequence
    seq = lines[0]

    #After the first line and a new line we have the map
    for line in lines[2:]:
        src, dest = line.split("=")
        src = src.strip()
        dest = dest.strip().split(",")
        dest[0] = dest[0].replace("(", "")
        dest[1] = dest[1].replace(")", "").strip()

        #Store the source and possible destinations in a dict
        mapper[src] = dest

    print(mapper)

    #In part 2 find out all the nodes ending with 'A'
    start_nodes = [i for i in mapper if i[-1] == 'A']
    print(start_nodes)

    res = 0
    ctr = 0
    n = len(seq)

    #List to store the turns required for every node to reach destination
    indis = []

    #Calculate the turns required for each node
    for i in range(len(start_nodes)):
        while not start_nodes[i].endswith('Z'):
            start_nodes[i] = mapper[start_nodes[i]][1] if seq[ctr] == 'R' else mapper[start_nodes[i]][0]
            ctr = (ctr + 1)%n
            res+=1
        indis.append(res)
        ctr = 0
        res = 0

    # print(indis)

    #Finally find the LCM of all the individual turns.
    #NOTE: Python 3.9+ supports *.
    print(math.lcm(*indis))




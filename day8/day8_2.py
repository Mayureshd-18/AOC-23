import math
with open("input_1.txt") as f:
    data = f.read()
    lines = data.splitlines()

    mapper = {}

    seq = lines[0]
    for line in lines[2:]:
        src, dest = line.split("=")
        src = src.strip()
        dest = dest.strip().split(",")
        dest[0] = dest[0].replace("(", "")
        dest[1] = dest[1].replace(")", "").strip()

        mapper[src] = dest

    print(mapper)

    start_nodes = [i for i in mapper if i[-1] == 'A']
    print(start_nodes)

    res = 0
    ctr = 0
    n = len(seq)

    indis = []

    for i in range(len(start_nodes)):
        while not start_nodes[i].endswith('Z'):
            start_nodes[i] = mapper[start_nodes[i]][1] if seq[ctr] == 'R' else mapper[start_nodes[i]][0]
            ctr = (ctr + 1)%n
            res+=1
        indis.append(res)
        ctr = 0
        res = 0

    # print(indis)
    print(math.lcm(*indis))




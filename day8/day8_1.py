with open("input_1.txt") as f:
    # Read the lines
    data = f.read()
    lines = data.splitlines()


    mapper = {}

    # First line is the sequence
    seq = lines[0]

    # After the first line and a new line we have the map
    for line in lines[2:]:
        src, dest = line.split("=")
        src = src.strip()
        dest = dest.strip().split(",")
        dest[0] = dest[0].replace("(", "")
        dest[1] = dest[1].replace(")", "").strip()

        # Store the source and possible destinations in a dict
        mapper[src] = dest

    print(mapper)

    #The source is the node 'AAA' and the destination is node 'ZZZ'
    crt = 'AAA'

    #To store the number of steps
    res = 0
    #To cycle through the sequence
    ctr = 0
    n = len(seq)

    #Continue finding the next step until we reach destination and simultaneously increment the steps needed and cycle through the sequence
    while crt!= 'ZZZ':
        crt = mapper[crt][1] if seq[ctr] == 'R' else mapper[crt][0]
        ctr = (ctr + 1)%n
        res+=1

    print(res)




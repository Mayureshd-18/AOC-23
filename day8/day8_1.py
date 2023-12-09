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

    crt = 'AAA'

    res = 0
    ctr = 0
    n = len(seq)

    while crt!= 'ZZZ':
        crt = mapper[crt][1] if seq[ctr] == 'R' else mapper[crt][0]
        ctr = (ctr + 1)%n
        res+=1

    print(res)




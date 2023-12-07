with open("input_1.txt") as f:
    data = f.read()
    lines = data.splitlines()

    res = 1

    _,times = lines[0].split(":")
    t = int("".join(times.strip().split()))

    _, dists = lines[1].split(":")
    record = int("".join(dists.strip().split()))

    ctr=0
    dist_travelled = None

    for j in range(t+1):
        dist_travelled = j * (t-j)
        if dist_travelled > record:
            ctr+=1

    print(ctr)





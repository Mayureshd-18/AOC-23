with open("input_1.txt") as f:
    data = f.read()
    lines = data.splitlines()

    res = 1

    _,times = lines[0].split(":")
    times = list(map(int, times.strip().split()))
    _, dists = lines[1].split(":")
    records = list(map(int, dists.strip().split()))

    print(times, records)

    for i in range(len(times)):
        t = times[i]
        ctr = 0
        dist_travelled = None

        for j in range(t+1):
            dist_travelled = j * (t-j)
            if dist_travelled > records[i]:
                ctr+=1

        # print(ctr)
        res *= ctr

    print(res)





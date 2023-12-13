with open("input_1.txt") as f:
    # Read the lines
    data = f.read()
    lines = data.splitlines()

    ans = 0
    for line in lines:
        possible = [line.split()[0]]
        for i in range(len(line.split()[0])):
            new_possible = []
            for p in possible:
                if p[i] == "?":
                    new_possible.append(p[:i] + "." + p[i + 1:])
                    new_possible.append(p[:i] + "#" + p[i + 1:])
                else:
                    new_possible.append(p)
            possible = new_possible
        for p in possible:
            counts = []
            count = 0
            for c in p:
                if c == "#":
                    count += 1
                if c == "." and count > 0:
                    counts.append(count)
                    count = 0
            if count > 0:
                counts.append(count)
            ans += counts == list(map(int, line.split()[1].split(",")))

    print(ans)
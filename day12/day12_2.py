with open("input_1.txt") as f:
    # Read the lines
    data = f.read()
    lines = data.splitlines()

    ans = 0
    for line in lines:

        possible_ = line.split()[0]

        possible = possible_

        for _ in range(4):
            possible += '?'
            possible+= possible_

        possible = list(possible)
        print(f'possible is {possible}')

        match = list(map(int, line.split()[1].split(","))) * 5
        print(f'match is {match}')

        # print(possible)
        n = len(possible)

        for i in range(len(possible)):
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
            ans += counts == match

    print(ans)
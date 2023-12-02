
res = 0
with open("input_1.txt") as f:
    data = f.read()
    lines = data.splitlines()

    for i in lines:
        max_red, max_green, max_blue = -float('inf'), -float('inf'), -float('inf')

        gameid, games = i.split(":")
        _,id_ = gameid.split()

        subgames = games.split(";")
        for j in subgames:
            cubes = j.split(",")
            # print(cubes)
            for k in cubes:
                n, c = k.split()
                if c=="red":
                    max_red = max(max_red, int(n))
                elif c=="green":
                    max_green = max(max_green, int(n))
                else:
                    max_blue = max(max_blue, int(n))
        power = (max_red*max_green*max_blue)
        res+= power

print(res)





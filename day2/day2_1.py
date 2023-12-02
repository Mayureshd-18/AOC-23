rl, gl, bl = 12, 13, 14
res = 0
with open("input1.txt") as f:
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
        if max_red<=rl and max_blue<=bl and max_green<=gl:
            print(id_)
            res+= int(id_)

print(res)





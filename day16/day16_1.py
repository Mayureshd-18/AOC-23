import sys
sys.setrecursionlimit(999999999)

with open("input_1.txt") as f:
    data = f.read()
    lines = data.splitlines()
    m = len(lines[0])
    n = len(lines)

    ctr = 0
    dirns = []

    for line in range(n):
        lines[line] = list(lines[line])

    print(*lines, sep="\n", end="\n\n")


    def make_beam(point, dirn):
        global ctr
        while 0 <= point[0] <=n-1 and 0<=point[1]<=m-1:


            if dirn == 1:
                if lines[point[0]][point[1]] == '.':
                    lines[point[0]][point[1]] = '#'

                if lines[point[0]][point[1]] == '|':
                    make_beam([point[0]-1, point[1]], -2)
                    make_beam([point[0]+1, point[1]], +2)
                    break

                if lines[point[0]][point[1]] == '\\':
                    # dirn = 2
                    # point[1] -=1
                    make_beam([point[0]+1, point[1]], 2)
                    break

                if lines[point[0]][point[1]] == '/':
                    # dirn = -2
                    # point[1] -=1
                    make_beam([point[0]-1, point[1]], -2)
                    break
                point[1]+=1


            if dirn == 2:
                if lines[point[0]][point[1]] == '.':
                    lines[point[0]][point[1]] = '#'

                if lines[point[0]][point[1]] == '-':
                    make_beam([point[0], point[1]-1], -1)
                    make_beam([point[0], point[1]+1], +1)
                    break

                if lines[point[0]][point[1]] == '\\':
                    # dirn = 1
                    # point[0] -= 1
                    make_beam([point[0], point[1]+1], 1)
                    break

                if lines[point[0]][point[1]] == '/':
                    # dirn = -1
                    # point[0] -= 1
                    make_beam([point[0], point[1]-1], -1)
                    break

                point[0]+=1


            if dirn == -1:
                if lines[point[0]][point[1]] == '.':
                    lines[point[0]][point[1]] = '#'

                if lines[point[0]][point[1]] == '|':
                    make_beam([point[0]-1, point[1]], -2)
                    make_beam([point[0]+1, point[1]], +2)
                    break

                if lines[point[0]][point[1]] == '\\':
                    # dirn = 2
                    # point[1] -=1
                    make_beam([point[0]-1, point[1]], -2)
                    break

                if lines[point[0]][point[1]] == '/':
                    # dirn = -2
                    # point[1] -=1
                    make_beam([point[0]+1, point[1]], 2)
                    break

                point[1] -=1


            if dirn == -2:
                if lines[point[0]][point[1]] == '.':
                    lines[point[0]][point[1]] = '#'

                if lines[point[0]][point[1]] == '-':
                    make_beam([point[0], point[1]-1], -1)
                    make_beam([point[0], point[1]+1], +1)
                    break

                if lines[point[0]][point[1]] == '\\':
                    # dirn = 1
                    # point[0] -= 1
                    make_beam([point[0], point[1]-1], -1)
                    break

                if lines[point[0]][point[1]] == '/':
                    # dirn = -1
                    # point[0] -= 1
                    make_beam([point[0], point[1]+1], 1)
                    break

                point[0] -=1




            # print()



    make_beam([0,0], 1)
    print(*lines, sep="\n", end="\n\n")







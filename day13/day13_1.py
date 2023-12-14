def check_vertical(pattern):
    l = len(pattern[0])
    for n in range(1,l):
        min_len = min(n, l-n)
    #     flag = True
    #     # print(n)
    #     for p in pattern:
    #         left =  p[:n][-min_len:]
    #         right = p[n:n+min_len][::-1]
    #         # print(f'{left} || {right}')
    #         if left!=right:
    #             flag = False
    #             break
    #     if flag:
    #         # print(f"Mirror found at {n} ")
    #         return n
    #     # print()
    # # print("Mirror not found")
        if all(
                p[:n][-min_len:] == p[n:n + min_len][::-1]
                for p in pattern
        ):
            return n
    return 0


def check_horizontal(X):
    pattern = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
    return check_vertical(pattern)

with open("input_1.txt") as f:
    data = f.read()
    lines = data.splitlines()

    patterns = []
    temp = []

    for line in lines:
        if line!="":
            temp.append(line)
        else:
            patterns.append(temp)
            temp = []
    if temp:
        patterns.append(temp)

    for i in patterns:
        for j in range(len(i)):
            i[j] = list(i[j])
    print(patterns)


    res = sum(check_vertical(i) + check_horizontal(i)*100 for i in patterns)
    print(res)




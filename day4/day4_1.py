ans = 0
with open("input_1.txt") as f:
    data = f.read()
    lines = data.splitlines()

    for line in lines:
        card, rem = line.split(":")
        rem = rem.strip()
        winners,holdings = rem.split("|")
        winners = winners.strip().split()
        holdings = holdings.strip().split()
        # print(winners, holdings)

        res = [value for value in winners if value in holdings]
        print(res)
        if res:
            ans+= 2**(len(res) - 1)

print(ans)




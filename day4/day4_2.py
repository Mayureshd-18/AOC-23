ans = 0
with open("input_1.txt") as f:
    data = f.read()
    lines = data.splitlines()

    cards_freq= {i:1 for i in range(1,len(lines)+1)}


    for line in lines:
        card, rem = line.split(":")
        _,card_no = card.split()
        card_no = int(card_no)
        rem = rem.strip()
        winners,holdings = rem.split("|")
        winners = winners.strip().split()
        holdings = holdings.strip().split()
        # print(winners, holdings)

        res = [value for value in winners if value in holdings]
        # print(res)

        for _ in range(cards_freq[card_no]):
            for d in range(card_no+1, len(res) + card_no+1):
                cards_freq[d]+=1

    print(sum(cards_freq.values()))

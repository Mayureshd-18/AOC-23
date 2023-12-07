from collections import Counter


precedence = ['A', 'K', 'Q', ]

mapper = {
    'A' : 'Z',
    'K' : 'Y',
    'Q' : 'X',
    'J' : 'W',
    'T' : 'V',
    '9' : 'U',
    '8' : 'T',
    '7' : 'S',
    '6' : 'R',
    '5' : 'Q',
    '4' : 'P',
    '3' : 'O',
    '2' : 'N',
    '1' : 'M'
}

with open("input_1.txt") as f:
    data = f.read()
    lines = data.splitlines()


    def determine_type(hand:str)-> int:
        ctr = Counter(hand)
        vals = list(ctr.values())

        #Five of a kind
        if 5 in vals:
            return 1

        #Four of a kind
        elif 4 in vals:
            return 2


        elif 3 in vals:
            #full house
            if 2 in vals:
                return 3

            #Three of a kind
            else:
                return 4

        # Two pair
        elif vals.count(2) == 2:
            return 5

        #One pair
        elif 2 in vals:
            return 6

        #High card
        else:
            return 7




    data = {}
    strengths = {}

    for line in lines:

        #Read the hand and the bid
        hand, bid = line.split()

        #Map the hand with another alphabet to determine the rank easily
        hand = list(hand)
        for i in range(len(hand)):
            hand[i] = mapper[hand[i]]
        hand = "".join(hand)

        data[hand] = int(bid)

        type_ = determine_type(hand)
        # print(hand, type_)

        #For every hand determine the type. For every type store the hands int a dict.
        if type_ not in strengths:
            strengths[type_] = [hand]
        else:
            strengths[type_].append(hand)


    #Sort the types
    myKeys = list(strengths.keys())
    myKeys.sort()
    strengths = {i: strengths[i] for i in myKeys}

    res = 0

    #Sort the hands having the same type
    for key, values in strengths.items():
        values.sort(reverse= True)

    print(strengths)
    print(data)

    #Determie the total number of hands
    t_ranks = len(list(data.keys()))

    #Multiply the sorted hands with respective bid
    for key, vals in strengths.items():
        for j in vals:
            res += data[j] * t_ranks
            t_ranks-=1

    print(res)




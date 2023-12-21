def algo(s:str) -> int:
    crt_value = 0
    for i in s:
        crt_value+= ord(i)
        crt_value*=17
        crt_value%=256

    return crt_value


with open("input_1.txt") as f:
    data = f.read()
    lines = data.splitlines()


    ans =0
    boxes = {}

    for line in lines:
        vals = line.split(",")
        for strs in vals:
            if '-' in strs:
                label = strs[:-1]
                val = algo(label)
                if val in boxes:
                    for lens in boxes[val]:
                        if label== lens[0]:
                            boxes[val].remove(lens)
                            if len(boxes[val]) == 0:
                                del boxes[val]
                            break
            else:
                label, focal_len = strs.split("=")
                val = algo(label)
                if val in boxes:
                    flag = False
                    for i in range(len(boxes[val])):
                        if boxes[val][i][0] == label:
                            boxes[val][i] = [label, focal_len]
                            flag = True
                            break
                    if not flag:
                        boxes[val].append([label,focal_len])
                else:
                    boxes[val] = [[label, focal_len]]

            print(boxes)

    for box in boxes:
        for lens in boxes[box]:
            val = (box+1) * (boxes[box].index(lens)+1) * int(lens[1])
            print(lens,val)
            ans+= val

    print(ans)




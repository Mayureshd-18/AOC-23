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
    for line in lines:
        vals = line.split(",")
        for strs in vals:
            print(strs,algo(strs))
            ans+=(algo(strs))

    print(ans)


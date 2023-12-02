mapping = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}
with open("input_2.txt") as f:
    data = f.read()
    for name, value in mapping.items():
        data = data.replace(name, value)

    lines = data.splitlines()

res = 0

for i in lines:
    temp = "".join(j for j in i if j.isdigit())
    res+= int(temp[0] + temp[-1])

print(res)
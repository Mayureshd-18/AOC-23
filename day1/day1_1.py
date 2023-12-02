file1 = open('input.txt', 'r')
Lines = file1.readlines()

res = 0

for i in Lines:
    temp = "".join(j for j in i if j.isdigit())
    res+= int(temp[0] + temp[-1])

print(res)

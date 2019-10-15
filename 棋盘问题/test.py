ls = [[], [], []]

order = 0
for i in range(3):
    for j in range(3):
        order += 1
        ls[i].append(order)

print(ls)
list = [68, 34, 934, 1, 45, 834, 54, 56, 57]

for i in range (len(list)-1):
    swapped = False
    for b in range (len(list) - 1):
        if list[b] > list[b + 1]:
            temp = list[b]
            list [b] = list [b + 1]
            list [b + 1] = temp
            swapped = True
    if swapped == False:
        break
print(list)

# l = [10, 13, 12, 11]
#
# l.sort()
#
# print(l)

# big O notation

# bubble sort
# insertion sort
# selection sort


######################
### bubble sort ###
## Complexity (worst case): O(n^2)
## Complexity (best case): O(n)

data = [42, 69, 13, 9, 17]

for i in range(len(data) - 1):
    for j in range(len(data) - i - 1):
        if data[j] > data[j + 1]:
            temp = data[j]
            data[j] = data[j + 1]
            data[j + 1] = temp


print(data)
# module: random
# function: randint

from random import randint

# nums = [randint(10, 99) for _ in range(10)]

# nums = []
#
# for _ in range(100):
#     nums.append(randint(10, 99))
#
# print(nums)
#
# target = int(input("Enter a number: "))

######### Linear search
## Complexity: O(n)

# idx = -1
#
# for i in range(len(nums)):
#     if nums[i] == target:
#         idx = i
#         break
#
# print(idx)

######### Double ended search
# i = 0
# j = len(nums) - 1
#
# idx = -1
#
# while i < j:
#     if nums[i] == target:
#         idx = i
#         break
#
#     if nums[j] == target:
#         idx = j
#         break
#
#     i += 1
#     j -= 1
#
#
# if idx != -1:
#     print("Element found:", idx)
# else:
#     print("Not found")


# int mid = low + (high - low) / 2;
################# Binary search

nums = [randint(0, 1_000_000) for _ in range(100000) ]

nums = set(nums)
nums = list(nums)

nums.sort()

print(nums)

target = int(input("Enter a number: "))

left = 0
right = len(nums) - 1

idx = -1

iterations = 0

while left < right:
    mid = left + (right - left) // 2

    if nums[mid] == target:
        idx = mid
        break
    elif nums[mid] > target:
        right = mid - 1
    else:
        left = mid + 1

    iterations += 1


print(idx)
print(f"Iterations: {iterations}")
# union(other_set) или | – возвращает объединение множеств.
# intersection(other_set) или & – возвращает пересечение множеств.
# difference(other_set) или - – возвращает разность множеств.
# symmetric_difference(other_set) или ^ – возвращает симметрическую разность (элементы, которые есть только в одном из множеств).
# update(other_set) или |= – добавляет элементы из other_set (изменяет текущее множество).
# intersection_update(other_set) или &= – оставляет только пересечение с other_set.
# difference_update(other_set) или -= – удаляет элементы, присутствующие в other_set.
# symmetric_difference_update(other_set) или ^= – оставляет только симметрическую разность.


# s = set()
s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}

# for item in s:
#     print(item)


## add, pop, remove, discard
# s1.add(6)
# s1.pop()
# s1.discard(69) # no error here
# if 3 in s1:
#     s1.remove(3)
#
# print(s1)


## union
# result = s1.union(s2)
#
# print(result)

## intersect

# result = s1.intersection(s2)
#
# print(result)

## difference

# result = s1.difference(s2)
#
# print(result)

## symmetric_difference
# result = s1.symmetric_difference(s2)
#
# print(result)

## update (union)

# s1.update(s2)
#
# print(s1)

## intersect_update

# s1.intersection_update(s2)
#
# print(s1)

## difference_update
# s1.difference_update(s2)
#
# print(s1)

## symmetric_difference_update
# s1.symmetric_difference_update(s2)
#
# print(s1)

## issubset (подмножество)
# set1 = {10, 20, 30}
# set2 = {10, 20, 30, 40, 50}
#
# res = set1.issubset(set2) #
#
# print(res)

## issuperset (надмножество)

# set1 = {10, 20, 30}
# set2 = {10, 20, 30, 40, 50}
#
# res = set2.issuperset(set1)
#
# print(res)

## isdisjoint

set1 = {1, 2, 3}
set2 = {4, 5, 6}

print(set1.isdisjoint(set2))


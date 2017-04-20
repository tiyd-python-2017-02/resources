from sys import argv
import random


def merge(l):
    if len(l) <= 1:
        return l
    left  = merge(l[:len(l)//2])
    right = merge(l[len(l)//2:])

    #now we've got 2 sorted lists....
    #how do I combine 2 sorted lists into 1 sorted list?
    new_l = []
    while left and right:
        if left[0] < right[0]:
            new_l.append(left.pop(0))
        else:
            new_l.append(right.pop(0))
    return new_l + left + right
    


def sort_me(l, which):
    if which == "merge":
        return merge(l)
    else:
        l.sort()
        return l



n = int(argv[1])
which = argv[2]
numbers = list(range(n+1))

random.shuffle(numbers)

print(numbers)

sorted_nums = sort_me(numbers, which)

print(sorted_nums)


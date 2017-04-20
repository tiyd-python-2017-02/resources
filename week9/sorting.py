from sys import argv
import random

def bubble(l):
    switch = True
    count = 0
    while switch:
        switch = False
        count += 1
        for i in range(len(l)-count):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                switch = True
    return l


def select(l):
    out = []
    while l:
        m = min(l)
        out.append(m)
        l.remove(m)
    return out

def insert(l):
    out = [l[0]]
    for index in range(1, len(l)):
        for place in range(len(out)):
            if out[place] > l[index]:
                out.insert(place, l[index])
                break
        else:
            out.append(l[index])
    return out

def merge(l):
    if len(l) <= 1:
        return l
    left  = merge(l[:len(l)//2])
    right = merge(l[len(l)//2:])
    out = []
    while left and right:
        if left[0] < right[0]:
            out.append(left.pop(0))
        else:
            out.append(right.pop(0))
    return out + left + right


def sort_me(l, which):
    if which == "bubble":
        return bubble(l)
    elif which == "insert":
        return insert(l)
    elif which == "select":
        return select(l)
    elif which == "merge":
        return merge(l)
    else:
        l.sort()
        return l



n = int(argv[1])
which = argv[2]
numbers = list(range(n+1))

random.shuffle(numbers)

#print(numbers)

sorted_nums = sort_me(numbers, which)

#print(sorted_nums)


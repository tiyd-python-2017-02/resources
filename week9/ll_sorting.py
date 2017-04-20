from sys import argv
import random
from LinkedList import LinkedList as LL

def bubble(l):
    pass

def select(l):
    pass

def insert(l):
    for i in range(len(l)):
        for j in range(i):
            if l[i] < l[j]:
                l.insert(l.pop(i), j)
        

def merge(l):
    pass

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
ll = LL()
for number in numbers:
    ll.append(number)

print(ll)

sorted_nums = sort_me(ll, which)

print(ll)


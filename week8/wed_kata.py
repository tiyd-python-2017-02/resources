def sum_pairs(ints, s):
    min_right_index = len(ints)

    for left_index in range(len(ints)):
        for right_index in range(left_index + 1, len(ints)):
            left = ints[left_index]
            right = ints[right_index]
            if left + right == s:
                if right_index < min_right_index:
                    out = [left, right]
                    min_right_index = right_index

                #do something.
                #now determine if this is the correct left and right...
                #if so, return... if not... keep going.

    return out


def sum_pairs(ints, s):
    for right_index in range(len(ints)):
        right = ints[right_index]
        left = s - right
        #if there is a left, this is my pair.
        try:
            ints.index(left, 0, right_index)
            return [left, right]
        except:
            #there is no matching left number
            pass


def sum_pairs(ints, s):
    #left_set will be used to keep track of everything to the left of 
    #right.
    left_set = set()
    for right_index in range(len(ints)):
        right = ints[right_index]
        left = s - right
        print(s, left, right, number_set)        
        if left in left_set:
            return [left, right]

        left_set.add(right)


def sum_pairs(ints, s):
    #left_set will be used to keep track of everything to the left of 
    #right.
    left_set = set()
    for right in ints:
        left = s - right
        print(s, left, right, number_set)        
        if left in left_set:
            return [left, right]
        left_set.add(right)


l1= [1, 4, 8, 7, 3, 15]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5]
l6= [4, -2, 3, 3, 4]
l7= [0, 2, 0]
l8= [5, 9, 13, -3]

print(l1)
sum_pairs(l1, 8) == [1, 7]
print(l2)
sum_pairs(l2, -6) == [0, -6]
print(l3)
sum_pairs(l3, -7) == None
#sum_pairs(l4, 2) == [1, 1]
#sum_pairs(l5, 10) == [3, 7]
#sum_pairs(l6, 8) == [4, 4]
#sum_pairs(l7, 0) == [0, 0]
#sum_pairs(l8, 10) == [13, -3]


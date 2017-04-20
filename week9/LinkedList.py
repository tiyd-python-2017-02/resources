#Ryan
#Will

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.start = None
        self.end = None
        self.size = 0

    def __str__(self):
        if not self.start:
            return ""
        curr = self.start
        string_list = ''
        while curr.next:
            string_list += str(curr.data) + ', '
            curr = curr.next
        string_list += str(curr.data)
        return string_list

    def __len__(self):
        return self.size
        #count = 1
        #if not self.start:
        #    return 0
        #curr = self.start
        #while curr.next:
        #    count += 1
        #    curr = curr.next
        #return count

    def append(self, what):
        new_node = Node(what)
        if(self.start):
            curr = self.start
            while curr.next:
                curr = curr.next
            curr.next = new_node
        else:
            # new empty linked list, add first node
            self.start = new_node
        self.size += 1
        self.end = new_node

    def insert(self, what, where):
        new_node = Node(what)
        if where > len(self):
            raise IndexError
        if where == len(self):
            self.append(what)
            return

        if where == 0:
            new_node.next = self.start
            self.start = new_node
           
        else:
            curr_location = 1
            curr = self.start
            while curr_location < where:
                curr = curr.next
                curr_location += 1
            new_node.next = curr.next
            curr.next = new_node
        self.size += 1

    def pop(self, where=0):
        if where >= len(self):
            raise IndexError
        
        if where == 0:
            data = self.start.data
            self.start = self.start.next
           
        else:
            curr_location = 1
            curr = self.start
            while curr_location < where:
                curr = curr.next
                curr_location += 1
            data = curr.next.data
            curr.next = curr.next.next
        self.size -= 1
        return data

    def __getitem__(self, where):
        if where >= len(self):
            raise IndexError
        if where == 0:
            return self.start.data
        curr_location = 1
        curr = self.start
        while curr_location < where:
            curr = curr.next
            curr_location += 1
        return curr.next.data

    def remove(self, what):
        self.pop(self.find(what))

    def find(self, what):
        if not self.start:
            return -1
        curr_location = 0
        curr = self.start
        while curr.next:
            if curr.data == what:
                return curr_location
            curr_location += 1
            curr = curr.next
        if curr.data == what:
            return curr_location
        return -1
        

    


if __name__ == "__main__":
    l2 = LinkedList()
    l2.append(1)
    l2.append(2)
    l2.append(3)
    l2.append(4)
    l2.append(5)
    print(l2.find(1))
    print(l2.find(2))
    print(l2.find(7))
    print(l2.find(5))
    l2.remove(3)
    print(l2)

    print(l2[0])
    print(l2[1])
    print(l2[len(l2)-1])

    ll = LinkedList()
    ll.append('brekky')
    print(ll)
    ll.append('beer')
    print(ll)
    ll.append('crush your enemies')
    print(ll)
    ll.append('don\'t let your dreams be dreams')
    print(ll)
    ll.insert('yum', 2)
    print(ll)
    ll.insert('beginning', 0)
    ll.insert('end', len(ll))
    print(ll)
    ll.insert('one', 1)
    print(ll)

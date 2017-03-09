class OddList:
    def __init__(self, some_list):
        self.odd_list = some_list

    def append(self, item):
        self.odd_list.append(item)

    def __contains__(self, prey):
        return prey in self.odd_list

    def insert(self, item, location):
        self.odd_list.insert(location, item)

    def __iter__(self):
        return iter(self.odd_list)

    def __getitem__(self, index):
        return self.odd_list[index]

    def __add__(self, other):
        return OddList(self.odd_list + other.odd_list)

    def __str__(self):
        return str(self.odd_list)

    def __eq__(self, other):
        return self.odd_list == other.odd_list

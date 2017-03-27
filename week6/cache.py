class Cache:
    def __init__(self):
        self.innards = {}

    def get(self, key):
        return self.innards.get(key)

    def set(self, key, value):
        self.innards[key] = value

    def clear(self):
        self.innards = {}

    def has_key(self, key):
        return key in self

    def __contains__(self, key):
        return key in self.innards

    def __iter__(self):
        return iter(self.innards.items())

    def __len__(self):
        return len(self.innards)

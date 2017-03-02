class Album:
    def __init__(self, name, stock, msrp, discount=0, catalog_discount=0):
        self.name = name
        self.stock = stock
        self.msrp = msrp
        self.discount = discount
        self.catalog_discount = catalog_discount

    def __str__(self):
        return "%s %s %s" % (self.name, self.stock, self.get_price())

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return self.name.__hash__()

    def __adjust_stock__(self, add, quantity):
        if add:
            self.stock += abs(quantity)
        else:
            self.stock -= abs(quantity)

    def get_price(self):
        partial = self.msrp - self.msrp * self.discount
        return partial - partial * self.catalog_discount

    def sell(self, how_many=1):
        self.__adjust_stock__(add=False, quantity=how_many)

    def buy(self, how_many=1):
        self.__adjust_stock__(add=True, quantity=how_many)

    def list_stock(self):
        return self.stock

    def set_discount(self, discount):
        self.discount = discount

    def set_catalog_discount(self, discount):
        self.catalog_discount = discount


class Artist:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return self.name.__hash__()


class Store:
    artists = {}
    albums = {}

    @classmethod
    def add(cls, album, artist):
        cls.artists.setdefault(artist, set()).add(album)
        cls.albums.setdefault(album, set()).add(artist)

    @classmethod
    def discount_catalog(cls, artist, discount):
        if artist not in cls.artists:
            return
        for album in cls.artists[artist]:
            print(album)
            album.set_catalog_discount(discount)

    @classmethod
    def list_inventory(cls):
        for artist, albums in cls.artists.items():
            for album in albums:
                print(artist, album)

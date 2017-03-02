from record_store import Album, Artist, Store
from menu import Menu

artists = set()


def add_inventory():
    pass


def sell_album():
    pass


def add_artist():
    name = input("What is the name of the artist? ")
    artists.add(Artist(name))


def discount_album():
    pass

m = Menu()
m.register("Add Artist", add_artist)
m.register("Add Inventory", add_inventory)
m.register("Sell Album(s)", sell_album)
m.register("Discount Album", discount_album)
m.register("Show Artists", lambda: print(*sorted(artists), sep="\n"))
m.register("Show Inventory", Store.list_inventory)
m.display()

import csv
from record_store import *

a = Artist("morphine")

with open("inventory.csv", "r") as f:
    dr = csv.DictReader(f)
    for row in dr:
        print(row)
        artist = Artist(row["artist"].strip())
        album = Album(row["album"].strip(), float(row["quantity"]), float(row["msrp"]))
        # if a == artist:
        #     print("yay")
        Store.add(album, artist)

Store.discount_catalog(a, .2)
Store.list_inventory()

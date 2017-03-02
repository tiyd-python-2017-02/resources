import csv

class StockDay:
    def __init__(self, name, **kwargs):
        self.name  = name
        self.date  = kwargs.get('Date')
        self.open  = float(kwargs.get('Open'))
        self.close = float(kwargs.get('Close'))
        self.high  = float(kwargs.get('High'))
        self.low   = float(kwargs.get('Low'))

    def change(self):
        return self.close - self.open

    def max_diff(self):
        return self.high - self.low

    def __repr__(self):
        return "{} {} {} {} {} {}".format(self.name, self.date, self.open, self.close, self.high, self.low)


def sort_on(sd):
    return sd.open - sd.close


def main():
    days = []
    with open("EOD-GOOG.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            sd = StockDay("GOOG", **row)
            #sd = StockDay("GOOG", Date=row['Date'], Open=row['Open'])
            days.append(sd)

    #print(*days, sep="\n")
    print(max([day for day in days], key=lambda sd: sd.open - sd.close))
    print(min([day for day in days], key=sort_on ))

if __name__ == "__main__":
    main()
        



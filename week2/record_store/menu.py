from collections import OrderedDict
class Menu:
    def __init__(self, quit_option=True):
        self.quit_option = quit_option
        self.options = OrderedDict()

    def register(self, name, function):
        self.options[name] = function

    def display(self):
        while True:
            for index, option in enumerate(self.options):
                print("{}){}".format(index,option))
            if self.quit_option:
                print("{}){}".format(index+1,"Quit"))

            choice = input("what would you like to do? ")
            for index, option in enumerate(self.options):
                if str(index) == choice:
                      self.options[option]()


def test():
    #run test functions for menu.
    pass

if __name__ == "__main__":
    test()

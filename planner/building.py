import datetime


class Building:
    def __init__(self, address, stories):
        self.designer = "Matt Reeds"
        self.owner = ""
        self.date_constructed = ""
        self.address = address
        self.stories = stories

    def construct(self):
        self.date_constructed = datetime.datetime.now().date()


    def purchase(self, name):
        self.owner = name


    def print_details(self):
        print(f"{self.address} was purchased by {self.owner} on {self.date_constructed} and has {self.stories} stories.")




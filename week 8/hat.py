import random

class Hat:
    houses = ["gry", "huf", "raw", "sly"]

    @classmethod
    def sort(cls, name):
        house = random.choice(cls.houses)
        print(name, "is in", house)




Hat.sort("harry")

class PartyAnimal:
    x = 0

    # constructor for class
    def __init__(self):
        print('I am Constructed')

    def party(self):
        self.x = self.x + 1 
        print("So far", self.x)

    # deconstructor for class
    def __del__(self):
        print('I am deconstructed ', self.x)


class PartyLover():
    x = 0
    name = ''

    def __init__(self, z):
        self.name = z
        print(self.name, "constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)


pa = PartyAnimal()
pa.party()
pa.party()

pa = 42
# pa = 42 will change the pa's value and make it an integer,
# which will lead to call deconstructor,
# which will delete already set values to pa
print('pa contains: ', pa)

s = PartyLover('Sally')
s.party()

j = PartyLover('Jim')
j.party()
j.party()

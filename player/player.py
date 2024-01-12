from player.person import Person

class Player(Person):
    def __init__(self, name):
        super().__init__(name, 1000)

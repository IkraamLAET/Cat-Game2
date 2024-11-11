class Cat:
    # the constructor will create a cat for us in code.
    # to create the cat we need given_name and given_colour.
    # self is the cat we are creating.
    def __init__(self,given_name,given_colour):
        self.name = given_name
        self.colour = given_colour
        self.age = 1
        self.energy = 50
        self.intelligence = 5
        self.weight = 5
    
    def train(self):
        print(f"{self.name} is training ...  -5 energy  +1 intelligence")
        self.energy -= 5
        self.intelligence += 1
        self.age += 0.1

    def feed(self):
        print(f"{self.name} is eating ...  +10 energy  +1 weight")
        self.energy += 10
        self.weight += 1
        self.age += 0.1

    def sleep(self):
        print(f"{self.name} is sleeping ...  +10 energy  ")
        self.energy += 10
        self.age += 0.1

    def play(self):
        print(f"{self.name} is playing ...  -5 energy  -1 weight")
        self.energy -= 5
        self.weight -= 1
        self.age -= 0.1

    def stats(self):
        print(f"\n {self.name}'s stats: \n Energy = {self.energy} \n Intelligence = {self.intelligence} \n Weight = {self.weight}")
    
    def too_high(self):
            print(f"\n{self.name}'s energy and weight are too high! try training/playing with it.")
    
    def old_cat(self):
        if self.age>=15:
            print(f"\n{self.name} became too old and died. Game over.")



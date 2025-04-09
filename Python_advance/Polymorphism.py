# One method behaves differently depending on the object (many forms).

class Bird:
    def sound(self):
        print("Bird sound")

class Sparrow(Bird):
    def sound(self):
        print("Chirp")

class Parrot(Bird):
    def sound(self):
        print("Squawk")

def make_sound(bird):
    bird.sound()

make_sound(Sparrow())
make_sound(Parrot())

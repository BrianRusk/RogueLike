# create a generic class to represent not just the player, but just about everything in our game world. Enemies, items, and whatever other foreign entities we can dream of will be part of this class, which we’ll call Entity

# the 'def move(' is a method for the Entity class. 

class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx, dy):
    # Move the entity by a given amount
        self.x += dx
        self.y += dy
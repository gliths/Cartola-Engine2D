import sdl2

class GameObject(sdl2.ext.Entity):
    """
        Objeto renderizado na cena/world
    """
    def __init__(self, world, sprite, position=(0,0),parent = "world"):
        
        self.sprite = sprite
        self.sprite.position = position
        self.attributes = {}

        if parent == "world":
            self.Parent = world
        else:
            self.Parent = parent

    def AddAttribute(self,AttributeName: str,AttributeValue):
        self.attributes[AttributeName] = AttributeValue


class Color4(sdl2.ext.Color):
    def __init__(self, r=255, g=255, b=255, a=255):
        super().__init__(r, g, b, a)
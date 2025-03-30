import sdl2
import sdl2.ext

class Color4(sdl2.ext.Color):
    def __init__(self, r=255, g=255, b=255, a=255):
        super().__init__(r, g, b, a)


    


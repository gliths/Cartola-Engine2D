import sdl2



class SoftwareRenderer(sdl2.ext.SoftwareSpriteRenderSystem):
    def __init__(self, window):
        super(SoftwareRenderer, self).__init__(window)
        self.BackgroundWindowColor = sdl2.ext.Color(8, 2, 26)

    def render(self, components):
        sdl2.ext.fill(self.surface, self.BackgroundWindowColor)
        super(SoftwareRenderer, self).render(components)
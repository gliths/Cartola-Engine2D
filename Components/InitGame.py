import sdl2
import sdl2.ext
import sys
from  CFW import *
from Components.Systems import *

class Game():

    def Update(self, func):
        def wrapper(*args, **kwargs):
            while self.running:
                func(*args, **kwargs)
        return wrapper

    def __init__(self,name: str,fullscreen: bool = True,WindowSize: Vector2 = Vector2(1920, 1020), BackgroundColor: Color4 = Color4(8,4,16)):
        """
        
        A classe que é o jogo, onde tem os metodos principais, como, update e start

        The class that is the game, where it has the main methods, such as update and start
        
        """

        sdl2.ext.init()

        #Iniciando a e mostrando Janela na tela
        window = sdl2.ext.Window(name, WindowSize.tuple(), flags=sdl2.SDL_WINDOW_RESIZABLE)
        window.show()

        if fullscreen:
            window.maximize()
        
        self.name = name
        self.running = True
        self.BackgroundColor = BackgroundColor

        self.world = sdl2.ext.World()
        self.renderer = sdl2.ext.Renderer(window)
        self.factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)


        #Criando Serviços
        SpriteRender = SoftwareRenderer(window)

        SpriteRender.BackgroundWindowColor = self.BackgroundColor

        #Adicionado os serviços ao World
        self.world.add_system(SpriteRender)

       
    def play(self):
         # Loop principal onde é verificado os eventos, como eventos do teclado ou de sair do programa 
        while self.running:
            events = sdl2.ext.get_events()
            for event in events:
                if event.type == sdl2.SDL_QUIT:
                    self.running = False
                    break
       
            sdl2.SDL_Delay(10)
            #processa os serviços do world
            self.world.process()

        sdl2.ext.quit()
        sys.exit()

    def quit():
        sdl2.ext.quit()

if __name__ == "__main__":
    game = Game("LOGO")
    game.play()

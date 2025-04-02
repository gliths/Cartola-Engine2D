import sdl2
import sdl2.ext
import math

#Sistemas
class SoftwareRenderer(sdl2.ext.SoftwareSpriteRenderSystem):
    def __init__(self, window):
        super(SoftwareRenderer, self).__init__(window)
        self.BackgroundWindowColor = sdl2.ext.Color(8, 2, 26)

    def render(self, components):
        sdl2.ext.fill(self.surface, self.BackgroundWindowColor)
        super(SoftwareRenderer, self).render(components)

#Componetes
class Color4(sdl2.ext.Color):
    def __init__(self, r=255, g=255, b=255, a=255):
        super().__init__(r, g, b, a)
class Vector2():
    def __init__(self, X,Y):
        
        self.x = X
        self.y = Y

    #Adição
    def __add__(self,other):
        return Vector2(self.x + other.x, self.y + other.y)  
    
    #subtração
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    
    #Multiplicação
    def __mul__(self, other):
        return Vector2(self.x * other.y,self.y * other.y)
    
    #Divisão
    def __truediv__(self, other):
        return Vector2(self.x / other.x, self.y / other.y)

    def __str__(self):
        return f"{self.x,self.y}"
    
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalized(self):
        mag = self.magnitude()
        return Vector2(self.x / mag, self.y / mag)
    
    def tuple(self):

        return (self.x,self.y)

#Objetos
class GameObject(sdl2.ext.Entity):
    """
        Objeto renderizado na cena/world
    """
    def __init__(self, world, position=(0,0),parent = "world",sprite = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE).from_color(Color4(255,255,255), Vector2(0,0).tuple())):
        
        self.sprite = sprite
        self.sprite.position = position
        self.attributes = {}

        if parent == "world":
            self.Parent = world
        else:
            self.Parent = parent

    def AddAttribute(self,AttributeName: str,AttributeValue):
        self.attributes[AttributeName] = AttributeValue

#Metodos/funções
def ResizeSprite(factory,sprite, new_width, new_height):
    
    # Cria uma nova superfície com o tamanho desejado
    resized_surface = sdl2.SDL_CreateRGBSurface(
        0, new_width, new_height, 32,  # 32 bits por pixel (8 por canal: RGBA)
        0x00FF0000,  # Máscara para o canal vermelho
        0x0000FF00,  # Máscara para o canal verde
        0x000000FF,  # Máscara para o canal azul
        0xFF000000   # Máscara para o canal alfa
    )
    

    sdl2.SDL_SetSurfaceBlendMode(resized_surface,sdl2.SDL_BLENDMODE_BLEND)

    # Redimensiona a superfície original para a nova superfície
    sdl2.SDL_BlitScaled(sprite.surface, None, resized_surface, None)
    
    # Retorna um novo sprite com a superfície redimensionada
    return factory.from_surface(resized_surface)
def Delay(delayTime):
        sdl2.SDL_Delay(delayTime)

#Init Game

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

        icon = sdl2.SDL_LoadBMP(b"icon.bmp")

        if icon:
            # Define o ícone da janela
            sdl2.SDL_SetWindowIcon(window, icon)
            # Libera a memória do ícone após definir
            sdl2.SDL_FreeSurface(icon)
        

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

    def quit():
        sdl2.ext.quit()

if __name__ == "__main__":
    game = Game("LOGO")
    game.play()
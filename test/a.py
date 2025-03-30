import sdl2
import sdl2.ext

# Defina a classe GameObject
class GameObject(sdl2.ext.Entity):
    """
    Objeto renderizado na cena/world
    """
    def __init__(self, world, sprite, position=(0, 0), parent="world"):
        self.sprite = sprite
        self.sprite.position = position
        self.attributes = {}

        if parent == "world":
            self.Parent = world
        else:
            self.Parent = parent

    def AddAttribute(self, AttributeName: str, AttributeValue):
        self.attributes[AttributeName] = AttributeValue

# Inicializa o SDL2
sdl2.ext.init()

# Cria uma janela e um renderizador
window = sdl2.ext.Window("Dois Objetos com o Mesmo Sprite", size=(800, 600))
window.show()

renderer = sdl2.ext.Renderer(window)

# Cria um mundo (world) para gerenciar entidades
world = sdl2.ext.World()

# Carrega o sprite (substitua pelo caminho da sua imagem)
factory = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE, renderer=renderer)
sprite = factory.from_color(sdl2.ext.Color(200,100,200), (200,200))

# Cria dois objetos usando o mesmo sprite, mas com posições diferentes
obj1 = GameObject(world, sprite, position=(100, 100))
obj2 = GameObject(world, sprite, position=(300, 200))


# Loop principal
running = True
while running:
    for event in sdl2.ext.get_events():
        if event.type == sdl2.SDL_QUIT:
            running = False
            break

    # Limpa a tela
    renderer.clear(0)

    # Atualiza e renderiza todos os objetos no mundo
    world.process()

    # Atualiza a tela
    renderer.present()

    # Espera um pouco para não sobrecarregar o processador
    sdl2.SDL_Delay(10)

# Finaliza o SDL2
sdl2.ext.quit()
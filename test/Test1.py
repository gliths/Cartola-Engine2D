import sys
import sdl2
import sdl2.ext

RESOURCES = sdl2.ext.Resources(__file__, "resources")

# Inicializa a SDL
sdl2.ext.init()

# Cria uma janela com o tamanho 800x600
window = sdl2.ext.Window("Cartola Engine", size=(800, 600), flags=sdl2.SDL_WINDOW_RESIZABLE)

# Mostra a janela
window.maximize()
window.show()

factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
sprite = factory.from_image(RESOURCES.get_path("cartola.png"))


sprite.position = 50,10
sprite.position = 150, 70
spriterenderer = factory.create_sprite_render_system(window)
spriterenderer.render(sprite)


processor = sdl2.ext.TestEventProcessor()
processor.run(window)

sdl2.ext.quit()
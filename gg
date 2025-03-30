import sys
import sdl2
import sdl2.ext

class ResponsiveApp:
    def __init__(self):
        sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO)

        # Criar uma janela redimensionável
        self.window = sdl2.SDL_CreateWindow(
            b"Janela Responsiva com PySDL2",
            sdl2.SDL_WINDOWPOS_CENTERED,
            sdl2.SDL_WINDOWPOS_CENTERED,
            800, 600,  # Tamanho inicial
            sdl2.SDL_WINDOW_RESIZABLE  # Permitir redimensionamento
        )

        # Criar um renderizador para desenhar na tela
        self.renderer = sdl2.SDL_CreateRenderer(self.window, -1, sdl2.SDL_RENDERER_ACCELERATED)
        
        self.running = True
        self.width, self.height = 800, 600  # Inicializa o tamanho da janela
        self.init_width, self.init_height = 800, 600
        self.run()

    def handle_events(self):
        """ Captura eventos da janela. """
        events = sdl2.SDL_Event()
        while sdl2.SDL_PollEvent(events):
            if events.type == sdl2.SDL_QUIT:
                self.running = False
            elif events.type == sdl2.SDL_WINDOWEVENT:
                if events.window.event == sdl2.SDL_WINDOWEVENT_RESIZED:
                    self.on_resize(events.window.data1, events.window.data2)

    def on_resize(self, width, height):
        """ Atualiza o tamanho da janela quando redimensionada. """
        self.width, self.height = width, height
        print(f"Nova resolução: {width}x{height}")

    def draw(self):
        """ Renderiza os elementos na tela. """
        sdl2.SDL_SetRenderDrawColor(self.renderer, 0, 0, 80, 255)  # Fundo preto
        sdl2.SDL_RenderClear(self.renderer)

        # Definir a cor vermelha para o retângulo
        sdl2.SDL_SetRenderDrawColor(self.renderer, 255, 255, 0, 255)

        # Criar um retângulo vermelho que se ajusta à janela
        rect = sdl2.SDL_Rect(int(self.width * 0.25), int(self.height * 0.25),
                             int(400), int(400))
        
        
        
        sdl2.SDL_RenderFillRect(self.renderer, rect)

        # Atualizar a tela
        sdl2.SDL_RenderPresent(self.renderer)

    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            sdl2.SDL_Delay(16)  # Aproximadamente 60 FPS

        # Encerrar SDL
        sdl2.SDL_DestroyRenderer(self.renderer)
        sdl2.SDL_DestroyWindow(self.window)
        sdl2.SDL_Quit()
        sys.exit()

if __name__ == "__main__":
    ResponsiveApp()

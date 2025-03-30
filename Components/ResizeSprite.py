import sdl2

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
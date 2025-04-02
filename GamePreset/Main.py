from Components import *
from threading import *

game = Game("Game")

def MultThread(func):
    def wrapper():
        Thread(target=func).start()
    return wrapper

if __name__  == "__main__":

    def __init__():
        factory = game.factory
        BlockSpr = factory.from_color(Color4(200,100,200), Vector2(200,200).tuple())
        GameObject(game.world,Vector2(20,20).tuple(),BlockSpr)

        game.play()

    __init__()

    
    


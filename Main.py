from CFW import *
import sys


game = Game("Borrachinha")




def Paralelo(func):
    def wrapper():
        Thread(target=func).start()
    return wrapper
    


@Paralelo
def ain():
    a = 0
    while True:
        print(a)
        a = a + 1

ain()

if __name__  == "__main__":

    def __init__():
        factory = game.factory
        BlockSpr = factory.from_color(Color4(200,100,200), Vector2(200,200).tuple())
        GameObject(game.world,BlockSpr,Vector2(20,20).tuple(),game.world)

        game.play()

    __init__()

    
    


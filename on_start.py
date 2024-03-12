import bge
from bge import logic

def main():

    cont = logic.getCurrentController()
    scene = logic.getCurrentScene()

    end = cont.sensors["Near-End"]
    constant_end = cont.sensors["End-Constant"]

    gameStart = cont.actuators["gameStart"]

    Camera = scene.objects["Camera"]
    Limit = scene.objects["Limit"]

    if Camera.position.y < -3.4:
        Camera.position.y += 0.046

    if end.positive:
        # Used for single updates related to the camera, please remove feature later
        pass
    
    if constant_end.positive:
        cont.activate(gameStart)
        
main()
import bge
from bge import logic


def main():

    cont = logic.getCurrentController()
    scene = logic.getCurrentScene()
    own = cont.owner

    tracking = cont.actuators["Track"]

    fish_look = cont.actuators["Fish_Look"]
    fish_trace = cont.actuators["Fish_Trace"]

    Player = scene.objects["Player_Hitbox"]

    #for maxLimit in range(-20, 1, 1):
    #    if maxLimit == 4:
    #      break
    #    tracking.max = abs(maxLimit) 
    #    cont.activate(tracking)
    if own.position.z < 2.7:
      Player.position.z += 20
      cont.deactivate(fish_trace)
      cont.activate(fish_look)

    if own.position.z >= 2.61:
      tracking.velocity += 0.2
      Player.position.z = 2.7
      cont.deactivate(fish_look)
      cont.activate(fish_trace)


    cont.activate(tracking)


main()

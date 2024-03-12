import bge
from random import uniform


def main():

    cont = bge.logic.getCurrentController()
    own = cont.owner

    fish_listen = cont.sensors["spawnFishRelay"]
    fisheSpawn = cont.actuators["spawnFishe"]

    if fish_listen.positive:
        minX = own.position.x - 3
        maxX = own.position.x + 3
        own.position.x = uniform(minX, maxX)
        minY = own.position.y - 3
        maxY = own.position.y + 3
        own.position.y = uniform(minY, maxY)
        own.position.z = 0
        cont.activate(fisheSpawn)
    else:
        pass

main()

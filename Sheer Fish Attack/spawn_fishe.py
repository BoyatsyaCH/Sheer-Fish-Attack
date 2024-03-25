import bge
from random import randint
from random import uniform

def main():

    cont = bge.logic.getCurrentController()
    scene = bge.logic.getCurrentScene()
    own = cont.owner

    fish_listen = cont.sensors["spawnFishRelay"]
    fish_counter = cont.sensors["Fish-Kill"]

    round = cont.actuators['Round']
    fisheSpawn = cont.actuators["spawnFishe"]
    fisheRound2 = cont.actuators["FishRound2"]
    fisheRound3 = cont.actuators["FishRound3"]

    Player = scene.objects["Player_Armature"]

    if fish_counter.positive:
        round.value = str(int(round.value) + 1)


    if fish_listen.positive:
        choice = randint(0, 1)
        if int(round.value) == 0:
            Player["Round"] = 0
            minX = own.position.x - 5
            maxX = own.position.x + 5
            own.position.x = uniform(minX, maxX)
            minY = own.position.y - 5
            maxY = own.position.y + 5
            own.position.y = uniform(minY, maxY)
            own.position.z = 0
            cont.activate(fisheSpawn)
            

        if int(round.value) > 0 and choice == 0:
            print("Fishe round 2")
            Player["Kills"] = 0
            Player["Round"] = 2
            cont.activate(fisheRound2)

        if int(round.value) > 0 and choice == 1:
            print("Fishe round 3")
            Player["Kills"] = 0
            Player["Round"] = 3
            cont.activate(fisheRound3)
    else:
        pass

main()

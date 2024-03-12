import bge
from bge import logic

def main():

    cont = logic.getCurrentController()
    scene = logic.getCurrentScene()
    own = cont.owner

    grenade_listen = cont.sensors['Grenade-Listen']
    bullet_listen = cont.sensors['Bullet-Listen']

    spawnGrenade = cont.actuators['grenadeSpawn']
    spawnBullet = cont.actuators['bulletSpawn']

    Pointer = scene.objects["spawner_Pointer"]

    if grenade_listen.positive:
        distance = own.getDistanceTo(Pointer)
        velocity = pow(abs(distance), 1.08)
        spawnGrenade.linearVelocity = (0, velocity, 0)
        cont.activate(spawnGrenade)

    if bullet_listen.positive:
        #distance = own.getDistanceTo(Pointer)
        #velocity = pow(abs(distance), 1.08)
        #spawnBullet.linearVelocity = (0, velocity, 0)
        cont.activate(spawnBullet)

    else:
        pass

main()

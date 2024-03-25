import bge
from bge import logic

def main():

    cont = logic.getCurrentController()
    own = cont.owner

    equip_grenade = cont.sensors["Equip_Grenade"]
    equip_gun = cont.sensors["Equip_Gun"]
    bullet_listen = cont.sensors["Bullet_Listen"]
    player_death = cont.sensors["Player_Death"]

    relay = cont.actuators["Relay"]

    grenade_anim = cont.actuators["Equip_Grenade"]
    gun_anim = cont.actuators["Equip_Gun"]
    shot_anim = cont.actuators["Gun_Shot"]
    death_anim = cont.actuators["Death_Animation"]

    #Gun = scene.objects["Gun"].meshes[0]

    if equip_grenade.positive:
        relay.subject = "Grenade_Mesh"
        cont.activate(relay)
        cont.activate(grenade_anim)

    if equip_gun.positive:
        #replace.mesh = (Gun)
        relay.subject = "Gun_Mesh"
        cont.activate(relay)
        cont.activate(gun_anim)

    if bullet_listen.positive:
        cont.activate(shot_anim)

    if player_death.positive:
        cont.activate(death_anim)
    else:
        pass

main()

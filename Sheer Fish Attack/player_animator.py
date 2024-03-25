# !!! DISCLAIMER !!!
# Maybe the true aberration was the code I made along the way

import bge
from bge import logic

def main():

    cont = logic.getCurrentController()
    scene = logic.getCurrentScene()
    own = cont.owner

    ### Sensors ###
    player_listen = cont.sensors["Pl-Start-Listen"]
    gameplay_ready = cont.sensors["Game-Ready"]
    left_click = cont.sensors["Left-Click"]
    rotate_sensor = cont.sensors["Rotate-Self"]
    throw_animation = cont.sensors["ThrowGrenade"]
    change_to_gun = cont.sensors["Change_To_Gun"]
    to_gun_idle = cont.sensors["To_Gun_Idle"]
    fish_shot = cont.sensors["Fish-Killed"]
    death_listen = cont.sensors["LTFish"]
    restart_ready = cont.sensors["Restart-Ready"]


    ### Animations ###
    FishingIdle = cont.actuators["Fishing_Idle"]
    PlayerStart = cont.actuators["Player_Start"]
    PlayerIdle = cont.actuators["Player_Idle"]
    PlayerRotation = cont.actuators["Player_Rotation"]
    PlayerThrow = cont.actuators["Player_Throw"]
    GunOut = cont.actuators["Gun_Out"]
    GunIdle = cont.actuators["Gun_Idle"]
    GunShot = cont.actuators["Gun_Shot"]
    Death = cont.actuators["Player_Ded"]
    ### Actuators ###
    equip_grenade_relay = cont.actuators["Equip_Grenade_Relay"]
    tracker = cont.actuators["Tracker"]
    throw_relay = cont.actuators["Throw_Grenade"]
    equip_gun_relay = cont.actuators["Equip_Gun_Relay"]
    spawnBullet = cont.actuators["spawnBullet"]
    restart = cont.actuators["Restart"]
    fish_killed_relay = cont.actuators["FishKillRelay"]
    circle_cursor = cont.actuators["Cursor"]
    
    ### Objects ###
    Loop_Controller = scene.objects["Loop_Controller"]
    Torus = scene.objects["Torus"]


    if player_listen.positive == False:
        cont.activate(FishingIdle)
        cont.deactivate(tracker)

    if player_listen.positive and Loop_Controller.position.z == 20 and Loop_Controller.position.x == -21:
        cont.deactivate(FishingIdle)
        cont.activate(PlayerStart)
        Loop_Controller.position.z = 0

    if PlayerStart.frame >= 259 and PlayerStart.frame <= 261:
        cont.activate(equip_grenade_relay)

    if gameplay_ready.positive and Loop_Controller.position.x == -21:
        cont.deactivate(PlayerStart)
        cont.activate(PlayerIdle)
        Loop_Controller.position.z = 1
        

    if Loop_Controller.position.z == 1:
        #print("MORE BLOOD MUST BE SHED")
        Torus.setVisible(True)
        cont.activate(tracker)
        if rotate_sensor.positive and Loop_Controller.position.x == -21:
            cont.activate(PlayerRotation)

            # add an "and fisheliminated.positive" to control the ending state of the loop controller even further 
        if change_to_gun.positive:
            Loop_Controller.position.x = -20
            if Loop_Controller.position.y == 21:
                cont.activate(GunOut)

            if to_gun_idle.positive:
                if GunOut.frame >= 19 or GunOut.frame <= 21:
                    cont.activate(equip_gun_relay)
                    Loop_Controller.position.y = 20

        if Loop_Controller.position.y == 20:
            cont.deactivate(GunOut)
            cont.activate(GunIdle)


        if left_click.positive:
            if Loop_Controller.position.x == -21:
                cont.activate(PlayerThrow)
            if Loop_Controller.position.x == -20:
                cont.activate(GunShot)
                cont.activate(spawnBullet)

        if throw_animation.positive:
            cont.activate(throw_relay)


    if fish_shot.positive:
        cont.activate(fish_killed_relay)
        own["Kills"] += 1
        print(str(own["Kills"]))
        if own["Kills"] == 1 and own["Round"] == 0:
            Loop_Controller.position.x = -21
            Loop_Controller.position.y = 21
            Loop_Controller.position.z = 1
            cont.activate(equip_grenade_relay)
            cont.activate(PlayerIdle)
            cont.activate(circle_cursor)
        if own["Kills"] == 3 and own["Round"] == 2:
            Loop_Controller.position.x = -21
            Loop_Controller.position.y = 21
            Loop_Controller.position.z = 1
            cont.activate(equip_grenade_relay)
            cont.activate(PlayerIdle)
            cont.activate(circle_cursor)
        if own["Kills"] == 4 and own["Round"] == 3:
            Loop_Controller.position.x = -21
            Loop_Controller.position.y = 21
            Loop_Controller.position.z = 1
            cont.activate(equip_grenade_relay)
            cont.activate(PlayerIdle)
            cont.activate(circle_cursor)

    if death_listen.positive:
        cont.activate(Death)
        Loop_Controller.position.z = 20
        print("death_listen is positive")
        cont.deactivate(GunIdle)
        tracker.time = 4800
        cont.deactivate(tracker)
        Torus.setVisible(False)

    if restart_ready.positive:
        cont.activate(restart)

    else:
        pass

main()

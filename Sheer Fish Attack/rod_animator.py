import bge


def main():

    cont = bge.logic.getCurrentController()
    own = cont.owner

    rod_listen = cont.sensors['Rod-Start-Listen']
    rod_splash = cont.sensors["Rod-Splash"]

    rodIdle = cont.actuators['Rod_Idle']
    rodThrow = cont.actuators['Rod_Throw']
    rodSplash = cont.actuators["Splash"]
    splashSFX = cont.actuators["Splash_SFX"]
    #rodStatic = cont.actuators['Rod_Static']

    #Self = scene.objects["Rod_Armature"]


    if rod_listen.positive != True:
        cont.activate(rodIdle)

    if rod_listen.positive and own.position.z > -3:
        cont.deactivate(rodIdle)
        cont.activate(rodThrow)

    if rod_splash.positive:
        cont.activate(rodSplash)
        cont.activate(splashSFX)

    else:
        pass

main()

import bge
from bge import logic

def main():

    cont = logic.getCurrentController()
    scene = logic.getCurrentScene()
    own = cont.owner

    gun_change = cont.sensors["Equip_Gun"]
    grenade_change = cont.sensors["Equip_Grenade"]

    replace = cont.actuators["Replace"]
    
    if grenade_change.positive:
        if own["gunPart"] == 1:
            Grenade = scene.objects["Grenade_Prop"].meshes[0]
            replace.mesh = (Grenade)
            cont.activate(replace)
        if own["gunPart"] == 2:
            SmolEmpty = scene.objects["Smol"].meshes[0]
            replace.mesh = (SmolEmpty)
            cont.activate(replace)
        if own["gunPart"] == 3:
            SmolEmpty = scene.objects["Smol"].meshes[0]
            replace.mesh = (SmolEmpty)
            cont.activate(replace)

    if gun_change.positive:
        print("Gun change positive")
        if own["gunPart"] == 1:
            Gun = scene.objects["Gun_Part.001"].meshes[0]
            replace.mesh = (Gun)
            cont.activate(replace)
        if own["gunPart"] == 2:
            Gun = scene.objects["Gun_Part.002"].meshes[0]
            replace.mesh = (Gun)
            cont.activate(replace)
        if own["gunPart"] == 3:
            Gun = scene.objects["Gun_Part.003"].meshes[0]
            replace.mesh = (Gun)
            cont.activate(replace)
    else:
        pass

main()

import bge
from bge import logic
from bge import render

# Busca en el script de la plantilla como anadir opciones en la barra de propiedades al estilo SerializeField de Unity, que se veia arrecho wn
# ^ Esto requiere que refactorices tu codigo para que funcione como un componente de Python.
# ^^ De paso requiere importar OrderedDict de collections.
render.showMouse(0)

def main():

    cont = logic.getCurrentController()
    scene = logic.getCurrentScene()
    own = cont.owner

    mouse = cont.sensors["Mouse-Over"]
    left_click = cont.sensors["Left-Click"]
    throw_synced = cont.sensors['Throw']
    crosshair = cont.sensors["Crosshair"]
    circlepoint = cont.sensors["Circlepoint"]

    spawnGrenade = cont.actuators["spawnGrenade"]
    pointerRelayX = cont.actuators["pointerPositionX"]
    pointerRelayY = cont.actuators["pointerPositionY"]
    Change_Cursor = cont.actuators["Change_Cursor"]

    Pointer = scene.objects["spawner_Pointer"]
    #Torus_Cursor = scene.objects["Torus"].meshes[0]
    #Cross_Cursor = scene.objects["Crosshair"].meshes[0]


    if mouse.positive:
        own.worldPosition.x = mouse.hitPosition.x
        own.worldPosition.y = mouse.hitPosition.y
        own.applyRotation((0, 0, 0.04), True)
        if left_click.positive:
            Pointer.worldPosition.x = mouse.hitPosition.x
            pointerRelayX.body = str(Pointer.worldPosition.x)
            cont.activate(pointerRelayX)

            Pointer.worldPosition.y = mouse.hitPosition.y
            pointerRelayY.body = str(Pointer.worldPosition.y)
            cont.activate(pointerRelayY)
            
    if throw_synced.positive:
        cont.activate(spawnGrenade)

    if crosshair.positive:
        Change_Cursor.mesh = scene.objects["Crosshair"].meshes[0]
        cont.activate(Change_Cursor)

    if circlepoint.positive:
        Change_Cursor.mesh = scene.objects["Circlepoint"].meshes[0]
        cont.activate(Change_Cursor)

main()

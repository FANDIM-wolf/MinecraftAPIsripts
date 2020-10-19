#to show player in home or no ?
#18.10.20
from mcpi.minecraft import Minecraft
mc = Minecraft.create()


#coordinas for home
buildX = 10
buildY =  68
buildZ = 50

#size of home
width = 19
height = 23
length = 25

#get position of player
pos =mc.player.getTilePos()
x=pos.x
y=pos.y
z=pos.z
#check player in home
inside  = buildX < x <buildX+width 
if inside == True:
    mc.postToChat("You are in Home.")
else:
    mc.postToChat("You are not  in Home "+"  "+str(x)+":"+str(y)+":"+str(z))
    #mc.player.setPos(-86,69,-86)


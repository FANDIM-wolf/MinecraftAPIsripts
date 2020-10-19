#this script builds block wall
#18.10.2020
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos=mc.player.getPos()#it finds player position out
x=pos.x
y=pos.y
z=pos.z
width=10
height=5
length=6
blockType=4

air=0
mc.setBlocks(x,y,z,x+width,y+height,z+length,blockType)



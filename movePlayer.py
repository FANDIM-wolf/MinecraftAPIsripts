#we move player  in this program
from  mcpi.minecraft import Minecraft

mc = Minecraft.create()

#get position of player
position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z

blockType = 10
mc.setBlock(x,y,z,blockType)
#mc.player.setTilePos(x,y,z) , function  set postition for Player


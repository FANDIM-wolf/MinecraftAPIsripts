#to show player coordinats
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos() #get position
x=pos.x
y=pos.y
z=pos.z
playerPosition =str(x)+":"+str(y)+":"+str(x)
mc.postToChat(playerPosition)
mc.postToChat(playerPosition)
mc.postToChat(playerPosition)
mc.postToChat(playerPosition)
mc.postToChat(playerPosition)
mc.postToChat(playerPosition)

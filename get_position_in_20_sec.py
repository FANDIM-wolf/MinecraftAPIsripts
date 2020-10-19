#output position of player in 25 seconds
import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos1 = mc.player.getTilePos()
x1=pos1.x
y1=pos1.y
z1=pos1.z
#wait for 25 seconds
time.sleep(25)
#get position again
pos2 =mc.player.getTilePos()
x2 = pos2.x
y2 = pos2.y
z2 = pos2.z

#calculate
xDistance = x2 - x1
yDistance = y2 - y1
zDistance = z2 - z1

#put result to one variable
post = (str(xDistance)+":"+str(yDistance)+":"+str(zDistance))

#output result
mc.postToChat(post)

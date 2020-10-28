#set watermealon 
from mcpi.minecraft import Minecraft
import  time 

mc= Minecraft.create()
time.sleep(10)

hits = mc.events.pollBlockHits()
block = 103 #watermealon

x,y,z=hits.x,hits.y,hits.z

mc.setBlock(x,y,z,block)



import mcpi.minecraft as minecraft
import time
import math


mc = minecraft.Minecraft.create()

answer = input("Start crater bomb in 10 sec ?: ")

if answer == "yes":
    #code to exploude the bomb  
    pos = mc.player.getPos()
    time.sleep(10)
    mc.setBlocks(pos.x+1,pos.y+6,pos.z+1 , pos.x-1,pos.y-1,pos.z-1,0)#zero in end ,this means air
    mc.postToChat("Boom!MutherFucker! ")
else:
    mc.postToChat("Order was canceld")

from  mcpi.minecraft import Minecraft
import time 
mc = Minecraft.create()

#coordinats for player

x = 10,1
y = 110,2
z = 12,1

#function to change player position
time.sleep(10)
mc.player.setPos(x,y,z)

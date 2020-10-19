#inpput number of block and set it 
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
try:
    x = 20
    y = 70
    z = 30
    blockType=int(input("Enter type of Block :"))
    ms.setBlock(x,y,z,blockType)
except:
    mc.postToChat("It is not number! Try do it again")
    

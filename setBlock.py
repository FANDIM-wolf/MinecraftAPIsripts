from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x=6
y=70

z=23
#103 - block watermelon
blockType=100
#set block  at difine position
mc.player.setPos(x,y,z)
mc.setBlock(x,y,z, blockType)

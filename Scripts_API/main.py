#minecraft divine edithion 
#1.0
import mcpi.minecraft as minecraft
import time

#------------------------------------------------------------

# function to show result , how many coins you have
def show_result(mc,number):
    mc.postToChat("Result:"+str(number))
    

# -----------------------------------------------------------

def main():
    mc = minecraft.Minecraft.create()#connect to world 
    
    #blocks
    
    

    
    #first bonfire , to get first bonus
    first_bonfire=mc.player.getTilePos()
    first_bonfire.x = -78
    first_bonfire.y =  38
    first_bonfire.z =  2
    #second bonfire , to get second bonus
    second_bonfire=mc.player.getTilePos()
    second_bonfire.x = -12
    second_bonfire.y = 42
    second_bonfire.z = 42

    #third bonfire , to get third bonus
    third_bonfire=mc.player.getTilePos()
    third_bonfire.x = -155
    third_bonfire.y = 44
    third_bonfire.z = 9
    
    #where we start 22,85,-33
     #where we finish game -1,89,-34

    #finsih_part  , end of first part
    finish_part=mc.player.getTilePos()
    finish_part.x = -53
    finish_part.y = 49
    finish_part.z = 50

    #second finish point , where you can check your bonus coins
    finish_part2=mc.player.getTilePos()
    finish_part2.x = -196
    finish_part2.y = 41
    finish_part2.z = 35
    

    
    # finish position 
    finish1 = mc.player.getTilePos()
    finish1.x = -1
    finish1.y = 89
    finish1.z = -34
    # finish button position 
    finish2 = mc.player.getTilePos()
    finish2.x = -41
    finish2.y = 55
    finish2.z = -32
    
    # coins for achivments , and  I use 1 and 0 instead true and false ,
    # cause translator can't define the variable 
    coin_bonus=0
    get_bonus_coin_1 = 1
    get_bonus_coin_2 = 1
    get_bonus_coin_3 = 1

    

    while True:
        
        pos=mc.player.getTilePos()
        if pos == finish1 or pos == finish2:
            mc.player.setTilePos(22,85,-33)#teleport to start point

            
        elif pos == first_bonfire and get_bonus_coin_1==1 :
            
        	mc.postToChat("Bonfire is fired!")
        	coin_bonus=coin_bonus+1
        	get_bonus_coin_1 = 0
        	mc.postToChat("Go to next point")
                #if we got coin in first time  we cant do it later
                    
        	mc.postToChat("Bonus coins:"+str(coin_bonus))
        elif pos == finish_part:
            show_result(mc,coin_bonus)
            
            
        elif pos == second_bonfire and get_bonus_coin_2==1:
            mc.postToChat("Bonfire is fired!")
            coin_bonus=coin_bonus+1
            get_bonus_coin_2 = 0
            bonus2=mc.player.getTilePos()
            bonus2.x=-14
            bonus2.y=42
            bonus2.z=42
            mc.setBlock(bonus2,103)
            mc.postToChat("Go to next point")
            
            #if we got coin in first time  we cant do it later
                    
            mc.postToChat("Bonus coins:"+str(coin_bonus))
        elif pos == third_bonfire and get_bonus_coin_3==1:
            mc.postToChat("Bonfire is fired!")
            coin_bonus=coin_bonus+1
            get_bonus_coin_3 = 0
            mc.postToChat("Go to next point")
            mc.postToChat("Bonus coins:"+str(coin_bonus))
            
        elif pos ==finish_part2:
            show_result(mc,coin_bonus)
        else:
            mc.postToChat("Go ahead! Bro")
            post = mc.player.getTilePos()
            mc.postToChat(post)
        
        

        time.sleep(1)


if __name__ == '__main__':
    main()


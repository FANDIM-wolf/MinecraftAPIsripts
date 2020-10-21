import mcpi.minecraft as minecraft
import time
import math

#maximal distation in the server

red_zone = 20

# get distance  between two points
def distance_between_2points(p1, p2):
    xd = p1.x - p2.x
    yd = p1.y - p2.y
    zd = p1.z - p2.z
    return math.sqrt((xd * xd) + (yd * yd) + (zd * zd))


# ----------------------------------------------------------

# current position
def print_player_position(mc, isDublicateToConsole=False):
    pos = mc.player.getTilePos()
    x = pos.x,
    y = pos.y,
    z = pos.z

    mc.posToChat("current pos: " + str(x) + str(y) + str(z))


# -----------------------------------------------------------

def main():
    mc = minecraft.Minecraft.create()

    start_point = mc.player.getTilePos()
    # distance between two points
    

    while True:
        cur_pos = mc.player.getTilePos()
        distance = distance_between_2points(start_point, cur_pos)
        if distance >= red_zone:
            mc.player.setTilePos(start_point)
            mc.postToChat("You tried to break borders of the Server ")
        else:
            mc.postToChat(distance)

        time.sleep(5)


if __name__ == '__main__':
    main()

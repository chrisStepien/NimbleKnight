#LAYERS
# Background
# Layer 1 - background of building
# Layer 2 - interactables and cosmetics
# Layer 3 - collidables with player

#LEGEND
#
# P = Player
# F = Floor
# R = Roof
# C = Cracked wall
# D = Death block
# L = Lava
# S = Stair
# W = Wall
# T = Trap
#23 rows
#Needs lots of tweaks and letter changes


#level_map_0
    #layer at the back - on top of background
#level_map_1
    #layer that adds cosmetics to the level
#level_map_2
    #layer for collidable surfaces

level_map = [
'                                                               ',
'               RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR',
'              R                                                ',
'             R                                                 ',
'RRRRRRRRRRRRR                                                  ',
'D                                                              ',
'D 123                                                          ',
'D 4 5                    F                                     ',
'D 6 7 P                  F                                     ',
'FFFFFFFFFFFFS            F                                     ',
'             S           F                                     ',
'              S          F                                     ',
'               FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF',
'                                                               ',
'                                                               ',
'                                                               ',
'                                                               ',
'                                                               ',
'                                                               ',
'                                                               ',
'                                                               ',
'                                                               ',
'                                                               ']                                                                                                                                                                                                                                                           


level_map_1 = []


level_map_2 = []


tile_size = 32
print(len(level_map[0]))
screen_width = 852
screen_height = 480 





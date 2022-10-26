#level_map = []

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

#Needs lots of tweaks and letter changes

level_map = [
'RRRRRRRRRRRRRRRRRRR            RRRRRRD',
'D                  R          R      D',    
'D                   R        R       D',
'D                    R      R     SFFFD',
'D  P                  R    R     SD',
'DFFFFFFFFFFFFFFS       RRRR     SD',
'               DS               WD',
'                DS              WD ',
'                 DS     FF      WD ',
'                  DC            WD    ',
'                  DW            WD  ',
'                  DW          FFWD      ',
'                  DW            WD',
'                 DC             RRRRRRRRRRRRRRRRRRRRR      WRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRW',
'         DRRRRRRRC                                   R     W                                                                     W',
'         D                                            R    W                                                                     W',
'         D                                             R   W                                                                     W',
'         D      SFFFLLLLLFLLLLLLFFF FFF FFF FFFS        R  W                                                                     W',
'         DFFFFFF                   T   T   T    S        R W                                                                     W',
'                                                 S        RW                                                                     W',
'                                                  S       RR                                                                     W',
'                                                   S                                                                             W                 WRRRRRRRRRRRRRRRRRRRRWTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTRRRRRRRTTTTTTTRRRRRRRTTTTTTTRRRRRRRRRRRRRRRRRR',
'                                                    S                                                                            W                 W       TTT    TTT                                                                                        W',
'                                                     S                                                                           W                 W                                                                                                         W',
'                                                      S                                                                          W               TTT                                                                                                         W',            
'                                                       S                                                                         RRRRRRRRRRRRRRRR                       FFFFF     FFFFF     FFFFF     FFFFF     FFFFFFFFFFFFFFTTTTTTTFFFFFFFTTTTTTTFFFFFFFF  W',
'                                                        SFFF                                                                                           FFF       FFF    W   W     W   W     W   W     W   W     W                                         W TW',
'                                                           W                                                                                                            W   WLLLLLW   WLLLLLW   WLLLLLW   WLLLLLW                                         W TW',
'                                                           W                                                                                     SFF                    W                                                                                 W TW',
'                                                           W                                                                                    S  W                    W    RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRW TW',
'                                                           W                                                                     FFFFFFFFFFFFFFF   WLLLLLLLLLLLLLLLLLLLLW    W                                                                               W',
'                                                           W                                                                     W                                           W                                                                               W',
'                                                           W                                                                     W                                           W                                        FF                                     W',
'                                                           W                                                                   FFW                                           W    FFFLLLLLLLFFFFFFFFFFFFFFFFFFFFLLLLLLLLLLLLLLLLLLLFFFFFFFFFFFFFFFFFFFFTTFFTTW',
'                                                           W                                                                     W                                           W    W',
'                                                           W                                                                     W                                           W    W',
'                                                           W                                                                     W                                           W    WTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR                                                                                                        ',
'                                                           W                                                                     W                                           W                                                                                                                    W',
'                                                           WTTTTTTTTFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFTTTTTTTTW                                           W                                                                                                                    W',
'                                                                                                                                                                             W                                                                                                                    W',
'                                                                                                                                                                             W                                                                                                                    W',
'                                                                                                                                                                             W                                                                                                        SFFFFFFFFFFFW',
'                                                                                                                                                                             WTTTFFF                                                                         FFFFFFFFFFFFFFFFF      FF',
'                                                                                                                                                                                   FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF                T      T',
'                                                                                                                                                                                                                                                                             T      T',
'                                                                                                                                                                                                                                                                             T      T',
'                                                                                                                                                                                                                                                                             T      T',
'                                                                                                                                                                                                                                                                             T      T',
'                                                                                                                                                                                                                                                                             T      T',     
'                                                                                                                                                                                                                                                                             T      T',
'                                                                                                                                                                                                                                                                             T      T',
'                                                                                                                                                                                                                                                                             T      T',
'                                                                                                                                                                                                                                                                             T      T',
'                                                                                                                                                                                                                                                                             T      T',
'                                                                                                                                                                                                                                                                             T      T',
'                                                                                                                                                                                                                                                                             T      T',
'                                                                                                                                                                                                                                                               RRRRRRRRRRRRRRT      TRRRRRRRRRRRRRR',
'                                                                                                                                                                                                                                                               W                                  W',
'                                                                                                                                                                                                                                                               W                                  W',
'                                                                                                                                                                                                                                                               W                                  W',
'                                                                                                                                                                                                                                                               W                                  W',
'                                                                                                                                                                                                                                                               W                                  W',
'                                                                                                                                                                                                                                                               W               FFFF               W',
'                                                                                                                                                                                                                                                               W                                  W',
'                                                                                                                                                                                                                                                               W                                  W',
'                                                                                                                                                                                                                                                               FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF']















tile_size = 32
screen_width = 800
screen_height = 600 

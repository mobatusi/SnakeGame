# Snake Game!

import pygame, sys, time, random

check_errors = pygame.init()

if check_errors[1] > 0:
    print("(!) Had {0} initializing errors, "
          "existing ...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) PyGame successfully initialized!")
"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and ELLE_VUOTTO.
"""
########################################################################
# done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################
import rosegraphics as rg

########################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
steve = rg.SimpleTurtle('square')
steve.pen = rg.Pen('Pink',15)
steve.speed = 20
for k in range (150):
    steve.left(80)
    steve.forward(k)
    steve.speed = 20*k

mike = rg.SimpleTurtle('triangle')
mike.pen = rg.Pen('Dark Blue',10)
mike.speed = 40
mike.go_to(rg.Point(10,0))
for k in range (150) :
    mike.right(80)
    mike.backward(k)
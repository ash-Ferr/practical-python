# bounce.py
#
# Exercise 1.5
#  A rubber ball is dropped from a height of 100 meters
#    and each time it hits the ground, it bounces back up to 3/5 the
#    height it fell. Write a program bounce.py that
#    prints a table showing the height of the first 10 bounces.
max_height=100
current_height=max_height
elasticity=3/5
for iter in range(10) :
    current_height=current_height*elasticity
    print('bounce number: #',iter,'  Height: ',round(current_height,4))

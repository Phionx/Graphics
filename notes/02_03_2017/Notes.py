#!/usr/bin/env python

from sys import argv

print "Generating Image\n"
file = open('image.ppm', 'w+')
file.truncate()
file.write("P3 500 500 255\n")
for i in range(0, 250):
    for j in range (0, 250):
        file.write("255 " + str(i) + " " + str(j) + " ")
    file.write("\n")

print "done!"


'''
Notes
Aim: 

'''

# -*- coding: utf-8 -*-
#Advent of Code- Day 1
#Part 1

captcha = open("day1.txt").read()

to_add = ''

for i in range(0,len(captcha)-2):
    if captcha[i] == captcha[i+1]:
        #to_add.append(captcha[i])
        to_add = to_add + captcha[i]
        
#check last and first number
if(captcha[len(captcha)-1] == captcha[0]):
    to_add = to_add + captcha[len(captcha)-1]        
    
#sum all entries in to_add
to_add_int = list(map(int, to_add))
print(sum(to_add_int))

#Part 2
half = len(captcha)//2
to_add = ''

for i in range(len(captcha)):
#    if(i + half > len(captcha)-1):
#        i2 = i + half - len(captcha)
#    else:
#        i2 = i + half
    
    if captcha[i] == captcha[(i + half) % len(captcha)]:
        to_add = to_add + captcha[i]

to_add_int = list(map(int, to_add))
print(sum(to_add_int))

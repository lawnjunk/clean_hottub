#!/usr/bin/python

import random

coin_goal = 100
health_points = 69
turn = 0
choise = False

grime = ["rat droppings", "cheto", "cigarret butt", "wrapper", "dried coffe", "beer", "mold", "barf", "dust", "condom", "dipin sausce", "makeup goo", "stik n poke needle", "14 day old food", "3 day old food", " 47 day old food" , "magical unknown substance", "scabies close", "rat shit", "barbeq spray", "fridge goo", "tub func", "sink gnar", "toenail clippings", "black mold", "rat", "behind the toilet", "open the fridge", "jars of peepee", "beer full of cigorett butts", "alexs nnnnasty socks", "turd", "tobbaco dip spit cup", "gitter messs", "bananna peel", "melted choclate bar", "taking out the trash", "trash back leeking the nasty lickquid" ]

rooms = ["yard", "living room", "ashia's room", "julias room", "kitchen", "kitchen nook", "laundry room" , "basment stairs", "sams room" , "basement room"]

breakTime = ["beer", "ciggaret", "redbuul", "fries", "cips", "calimocho", "4loco", "mickeys"]

watcha = ["slimefeld", "porn film", "utube family therapy", "make a craigs list post about dirrty dirrty daddys", "C.H.U.D."]

homies = ["pizza steef", "the narc", "curupt munk", "yarn", "a chud", "madude", "dorky", "alex", "joulia", "sam", "adan", "kyle", "kim", "davie"]

print "what up slug"
print "we gotta clean dis house"
name = raw_input("what is uur name sluggy? ")


def randomElement(arrayInput):
	rand_element_number = int(round(random.random() * (len(arrayInput)-1)))
	return arrayInput[rand_element_number]

def dooDamage(chance):
	global health_points
	if (random.random() < chance):
		rand_damage = int(random.random() * 15)
		health_points = health_points - rand_damage
		return True
	else:
		return False

def choosedYes():
	global choise
	ch = raw_input()
	if ch == "y":
		choise = True
	elif ch == "n":
		choise = False
	else:
		print "you must choose y or n"
		choosedYes()
	
print "" 

while health_points > 0:
	health_points = health_points -1
	turn = turn + 1
	random_room = randomElement(rooms)
	print "you have %s health points" % health_points
	print "turn %s: you have entered the %s" % (turn, random_room)
	random_shit =  randomElement(grime)
	print "you encountered a %s" % random_shit
	print "do uu want to cleen the %s" % random_shit
	choosedYes()
	if choise:
		didDamage = dooDamage(0.2)
		if not didDamage:
			print "great work %s you have cleaned up all the %s" % (name, random_shit)
		else:
			print "OUCh, that sucked cleaning the %s hurt you" % random_shit
			print "your health is now %d" % health_points
	else:
		if random.random() > 0.5:
			randomBreak = randomElement(watcha)
			randomHome = randomElement(homies)
			print "aright %s you get to take a break with %s and %s)" % (name, randomHome, randomBreak) 
			healthGain = int((random.random() * 15 ) + 10)
			"you gained %d health points" % healthGain
			health_points = health_points + healthGain
		else:
			print "the %s was to powerfull you should have cleaned it it took off 15 healthpoints" % random_shit
			health_points = health_points - 15

	print ""
	print "HP: %s" % health_points
	wait_to_continuse = raw_input("press <return> to continue")
	print ""		


print "%s died on turn %d" % (name, turn)

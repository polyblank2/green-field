#Filename Stat Gen

import random
from os import listdir
import os
#input_var = input("Input a filename: ")

def unitgenerator (input_str):
	#print(input_str)
	stats={}
	stats['name']=input_str

	random.seed(input_str)
	total = random.randint(100,130)
	#Total =

	weighted_choices = [('mage', 30), ('cleric', 20), ('warrior', 10), ('pirate', 40), ('assassin',5),('king',1)]
	prof = [val for val, cnt in weighted_choices for i in range(cnt)]
	stats['profession'] = random.choice(prof)

	weighted_choices = [('golem', 1), ('human', 100), ('orc', 80), ('elf', 40),('diety',1)]
	spec = [val for val, cnt in weighted_choices for i in range(cnt)]
	stats['species'] = random.choice(spec)

	#HP		Random
	hp = random.randint(10,20)
	total -= hp
	#print("hp"+str(hp))
	stats['hp']=hp

	#Attack
	att = random.randint(10,20)
	total -=att
	#print("attack"+str(att))
	stats['attack']=att

	#Defense
	defense = random.randint(10,20)
	total -=defense
	#print("defense"+str(defense))
	stats['defense']=defense

	#Agility
	agility = random.randint(10,20)
	total -=agility
	#print("agility"+str(agility))
	stats['agility']=agility

	#Intelligence
	intel = random.randint(10,20)
	total -=intel
	#print("intel"+str(intel))
	stats['intel']=intel

	#Range
	attrange = random.randint(10,20)
	total -=attrange
	#print("Attack Range"+str(attrange))
	stats['attackrange']=attrange

	#print("total:"+str(total))
	stats['total']=total
	print(stats)

myfiles = os.listdir(os.curdir)  #files and directories

for file in myfiles:
	unitgenerator(file)

'''
unitgenerator("temp.exe")
unitgenerator("Brian")
unitgenerator("Odin")
unitgenerator("goat")
unitgenerator("sheep")
unitgenerator("tank")
unitgenerator("man")
'''

#Ability_1
#Ability_2
#Ability_3
#Ability_4



#Mark Boady and Matthew Burlick
#Drexel University 2018
#CS 172

from hamster import *
import random

#This function has two monsters fight and returns the winner
def monster_battle(m1, m2):

	#first reset everyone's health!
	#####TODO######
	m1.resetHealth()
	m2.resetHealth()
	#next print out who is battling
	print("Starting Battle Between")
	print(m1.getName()+": "+m1.getDescription())
	print(m2.getName()+": "+m2.getDescription())
	
	
	#Whose turn is it?
	attacker = None
	defender = None
	
	#Select Randomly whether m1 or m2 is the initial attacker
	#to other is the initial definder
	######TODO######
	coin = random.randint(1, 10)
	if 1 <= coin <= 5:
		attacker = m1
		defender = m2
	else:
		attacker = m2
		defender = m1
	
	print(attacker.getName()+" goes first.")
	#Loop until either 1 is unconscious or timeout
	while m1.getHealth() > 0 and m2.getHealth() > 0:
		#Determine what move the monster makes
		#Probabilities:
		#	60% chance of standard attack
		#	20% chance of defense move
		#	20% chance of special attack move

		#Pick a number between 1 and 100
		move = random.randint(1, 100)
		#It will be nice for output to record the damage done
		before_health = defender.getHealth()
		
		#for each of these options, apply the appropriate attack and 
		#print out who did what attack on whom
		if( move >=1 and move <= 60):
			#Attacker uses basic attack on defender
			######TODO######
			attacker.basicAttack(defender)
			print(attacker.getName(), 'used', attacker.basicName(), 'on', defender.getName())

		elif move>=61 and move <= 80:
			#Defend!
			######TODO######
			attacker.defenseAttack(defender)
			print(attacker.getName(), 'used', attacker.defenseName(), 'on', defender.getName())
		else:
			#Special Attack!
			######TODO######
			attacker.specialAttack(defender)
			print(attacker.getName(), 'used', attacker.specialName(), 'on', defender.getName())
		#Swap attacker and defender
		######TODO######
		if attacker == m2:
			defender = m2
			attacker = m1
		else:
			defender = m1
			attacker = m2
		#Print the names and healths after this round
		######TODO######
		print(m1.getName(), 'at', m1.getHealth(), 'health')
		print(m2.getName(), 'at', m2.getHealth(), 'health')
	#Return who won
	######TODO######
	if m1.getHealth() <= 0:
		return m2
	else:
		return m1
#----------------------------------------------------


if __name__ == "__main__":
	#Every battle should be different, so we need to
	#start the random number generator somewhere "random".
	#With no input Python will set the seed

	first = Naruto("Naruto Uzumaki")
	second = TenTails("Ten Tails Madara")
	third = Dio("Dio Brando")
	fourth = Guy("Eight Gates Released Formation")
	
	winner = monster_battle(first, second)
	print(winner.getName(), 'is victorious!')
	winner2 = monster_battle(third, fourth)
	print(winner2.getName(), 'is victorious!')
	finalWinner = monster_battle(winner, winner2)
	print(finalWinner.getName(), 'is the tournament champion!')
	
	#Print out who won
	####TODO####
	
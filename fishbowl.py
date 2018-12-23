import os
import time
import random
from colorama import Fore
from iteration_utilities import duplicates

class Fish(object):
	def __init__(self, bowl_size, n_teams):
		self.bowl_size = bowl_size
		self.n_teams = n_teams
		self.color_codes = [Fore.RED, Fore.BLUE, Fore.GREEN, Fore.MAGENTA, Fore.CYAN, Fore.YELLOW]
		self.color_names = ["red", "blue", "green", "magenta", "cyan", "yellow"]
		self.maxv = 5
		self.location = [random.randint(1, bowl_size-1), random.randint(1, bowl_size-1)]
		self.direction = [random.randint(-self.maxv, self.maxv), random.randint(self.maxv, self.maxv)]
		self.color_code = self.color_codes[random.randint(0, n_teams)]
		self.color = self.color_names[self.color_codes.index(self.color_code)]

	def touching_wall(self):
		return any([x <= 1 or x >= self.bowl_size-1 for x in self.location])

	def bounce(self):
		self.direction = [random.randint(0, self.maxv) if x <=1
						  else random.randint(-self.maxv, 0) for x in self.direction]

	def move(self):
		self.location = [min(self.bowl_size-1, max(1, x+y)) for x,y in zip(self.location, self.direction)]

class Fishbowl(object):
	def __init__(self, nteams, nfishes, size):
		self.nteams = nteams
		if self.nteams > 5:
			exit("Maximum number of teams is 5")
		self.nfishes = nfishes
		if self.nfishes > 100:
			exit("Maximum number of players per team is 100")
		self.size = size
		if self.size > 50:
			exit("Maximum fishbowl size is 50")
		# create random start for all fishes
		self.fishes = [Fish(self.size, self.nteams) for _ in range(self.nfishes * self.nteams)]

	def draw(self):
		bowl = []
		# create fishbowl
		for q in range(self.size + 1):
			for t in range(self.size + 1):
				bowl.append(" ")
				if q == 0 or q == self.size or t == 0 or t == self.size:
					bowl.append(Fore.WHITE + "+")
				elif [q, t] in [fish.location for fish in self.fishes]:
					bowl.append([fish.color_code for fish in self.fishes if fish.location == [q, t]][0] + "€")
				else:
					bowl.append(" ")
			bowl.append("\n")
		# plot fishbowl
		os.system("cls")
		print("".join(bowl))
		bowl.clear()
		time.sleep(0.05)

	def remove_dead(self):
		self.fishes = [fish for fish in self.fishes
					   if fish.location not in duplicates([fish.location for fish in self.fishes])]

	def animate(self):
		while len(set([fish.color for fish in self.fishes])) > 1:
			# compute new direction of fishes
			for fish in self.fishes:
				if fish.touching_wall():
					fish.bounce()
				fish.move()
			# check for collisions between fishes
			self.remove_dead()
			# draw fishbowl
			self.draw()
		if not self.fishes:
			print("It's a draw!")
		else:
			print("Team {} wins!".format(*list(set([fish.color for fish in self.fishes]))))

if __name__=="__main__":

	bowl = Fishbowl(nfishes = 20, nteams = 4, size= 30)
	bowl.animate()
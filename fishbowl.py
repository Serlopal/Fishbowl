import os
import time
import random
from colorama import Fore
from iteration_utilities import duplicates

print(Fore.RED + 'some red text')

def draw_fishbowl(nteams, nfishes, l):
	# create random start for all fishes
	fishes = [[random.randint(1,l), random.randint(1,l)] for _ in range(nfishes*nteams)]
	team_colors = [Fore.RED, Fore.BLUE, Fore.GREEN, Fore.MAGENTA, Fore.CYAN, Fore.YELLOW]
	team_colors_names = ["red", "blue", "green", "magenta", "cyan", "yellow"]

	if nteams > len(team_colors):
		exit("Maximum number of teams is {}".format(len(team_colors)))
	if nfishes > 100:
		exit("Maximum number of players per team is 100")
	if l > 50:
		exit("Maximum fishbowl size is 50")

	colors = [c for team in [[color]*nfishes for color in team_colors[0:nteams]] for c in team]
	vectors = [[random.choice([1, -1])*random.randint(1, 3)]*2 for _ in range(nfishes*nteams)]
	bowl = []

	while len(set(colors)) > 1:
		# compute new direction of fishes
		for i in range(len(fishes)):
			if fishes[i][0] <= 0:
				vectors[i][0] = 1 * random.randint(1, 3)
			elif fishes[i][0] >= l:
				vectors[i][0] = -1 * random.randint(1, 3)

			if fishes[i][1] <= 0:
				vectors[i][1] = 1 * random.randint(1, 3)
			elif fishes[i][1] >= l:
				vectors[i][1] = -1 * random.randint(1, 3)

			fishes[i][0] += vectors[i][0]
			fishes[i][1] += vectors[i][1]

		# check for collisions
		idxs = [w for w, fish in enumerate(fishes) if fish not in duplicates(fishes)]
		fishes = [fishes[idx] for idx in idxs]
		colors = [colors[idx] for idx in idxs]
		vectors = [vectors[idx] for idx in idxs]

		# create fishbowl
		for q in range(l+1):
			for t in range(l+1):
				bowl.append(" ")
				if q == 0 or q == l or t == 0 or t ==l:
					bowl.append(Fore.WHITE + "+")
				elif [q, t] in fishes:
					bowl.append(colors[fishes.index([q,t])] + "€")
				else:
					bowl.append(" ")
			bowl.append("\n")

		# plot fishbowl
		os.system("cls")
		print("".join(bowl))
		bowl.clear()

		time.sleep(0.05)
	if not colors:
		print("It's a draw!")
	else:
		# print("Team {} wins!".format(team_colors_names[team_colors.index(colors[0])]))
		print("Team {} wins!".format([team_colors_names[team_colors.index(colors[i])] for i in range(len(colors))]))

if __name__=="__main__":

	draw_fishbowl(nfishes = 5, nteams = 3, l = 10)

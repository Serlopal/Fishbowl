import os
import time
import random
clear = "\n" * 100
def draw_fishbowl(num_fishes, l):

	# create random start for all fishes
	fishes = [[random.randint(1,l), random.randint(1,l)] for _ in range(num_fishes)]
	vectors = [[1, 1] for _ in range(num_fishes)]
	bowl = []

	while True:
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

		# create fishbowl
		for q in range(l+1):
			for t in range(l+1):
				bowl.append(" ")
				if q == 0 or q == l or t == 0 or t ==l:
					bowl.append("+")
				elif [q, t] in fishes:
					bowl.append("€")
				else:
					bowl.append(" ")
			bowl.append("\n")

		# plot fishbowl
		os.system("cls")
		print("".join(bowl))
		bowl.clear()
		time.sleep(0.05)



if __name__=="__main__":

	print(draw_fishbowl(num_fishes = 50	, l = 30))

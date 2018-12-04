import argparse
from time import sleep
from words import verbs, nouns
from random import choice as random_choice

def parse_args( ):
	parser = argparse.ArgumentParser(description='Gives you a random hacker phrase')
	parser.add_argument("-c", "--count", type=int, default=1, required=False, 
					    help="amount of phrases to show (default=1), negative number for infinite")
	parser.add_argument("-t", "--time-delay", type=float, default=1, required=False, help="amount of time between each phrase")

	return parser.parse_args( )

def main( ):
	args = parse_args( )
	args = vars(args)
	upto = [args["count"] if args["count"]>=0 else 5][0]
	for i in range(upto):
		print("{} the {}".format(random_choice(verbs), random_choice(nouns)))
		[sleep(args["time_delay"]) for j in [1] if i!=args["count"]-1]
		if args["count"] < 0: upto+=1

if __name__=="__main__":
	try:
		main( )
	except KeyboardInterrupt:
		print("Exitting the program...")
		exit(0)
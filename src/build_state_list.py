import csv


def build_state_list():

	state_list = []
	with open("states.csv","r") as csvfile:
		
		csvreader = csv.reader(csvfile,delimiter=",")

		#skip header
		next(csvreader)

		for row in csvreader:
			print row[1]
			state_list.append(row[1])

	return state_list

def build_state_lookup():

	state_lookup = {}
	
	with open("states.csv","r") as csvfile:
		
		csvreader = csv.reader(csvfile,delimiter=",")

		#skip header
		next(csvreader)

		for row in csvreader:
			state_lookup[row[1]] = row[0]

	return state_lookup

	
def main():

	state_list = build_state_list()

	state_lookup = build_state_lookup()


	print len(state_list)

	for state in state_list:
		print(state + "," + state_lookup[state])


if __name__ == "__main__":

	main()



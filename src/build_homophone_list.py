
def build_homophone_list():

	with open("homophones-1.01.txt", "r") as f:
		rows = f.readlines()

	counter = 0
	start = 0
	for row in rows:
		if "----------------" in row:
			start = counter+1
		counter +=1


	homophone_list = []	
	for i in range(start, len(rows)):
		for j in rows[i].strip().split(','):
			homophone_list.append(j)

	return homophone_list



def main():

	l = build_homophone_list()

	if "xander" in l:
		print "true"
	else:
		print "false"

if __name__ == "__main__":

	main()

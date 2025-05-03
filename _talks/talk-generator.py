import csv
import os

with open('../../OCW2025-registration.csv', newline='',encoding="utf8") as csvfile:
	f = csv.DictReader(csvfile)
	for row in f:
		#firstname, lastname, affiliation, stage, title
		if row['talk'] == 'Yes' and row['title'] != '':
			path_to_file = "talk-{0}-{1}.md".format(row['firstname'],row['lastname'])
			if not os.path.exists(path_to_file):
				g = open(path_to_file,"w")
				g.writelines("--- \n")
				g.writelines("name: {0} \n".format(row['title']))
				g.writelines("speakers: \n - {0} {1}  \ncategories:\n - Contributed\n".format(row['firstname'],row['lastname']))
				g.writelines("--- \n \n")
				#g.writelines("{0}".format(row['abstract']))
				g.close()
			else:
				pass
		elif row['talk'] == 'Undecided':
				pass
			#g.writelines("**Title**: *{0}*\n \n".format("TBA"))
			#g.writelines(" **Abstract**:\n \n {0}".format(row['abstract']))
		else:
			pass
		
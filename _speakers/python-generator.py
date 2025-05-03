import csv
import os

with open('../../OCW2025-registration.csv', newline='',encoding="utf8") as csvfile:
	f = csv.DictReader(csvfile)
	for row in f:
		#firstname, lastname, affiliation, stage, title
		path_to_file = "{0} {1}.md".format(row['firstname'],row['lastname'])
		if not os.path.exists(path_to_file):
			g = open(path_to_file,"w")
			g.writelines("--- \n")
			g.writelines("name: {0} {1}  \n".format(row['firstname'],row['lastname']))
			g.writelines("first_name: {0} \n".format(row['firstname']))
			g.writelines("last_name: {0} ({1}) \n".format(row['lastname'],row['affiliation']))
			g.writelines("hide: true \n")
			g.writelines("--- \n \n ")
			#if row['talk'] == 'Yes':
			#	g.writelines("**Title**: *{0}*\n \n".format(row['title']))
			#	g.writelines(" **Abstract**:\n \n ")
			#elif row['talk'] == 'Undecided':
			#	g.writelines("**Title**: *{0}*\n \n".format("TBA"))
				#g.writelines(" **Abstract**:\n \n {0}".format(row['abstract']))
			#else:
			#	pass
			g.close()


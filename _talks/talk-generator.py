import csv
with open('registration.csv', newline='',encoding="latin-1") as csvfile:
	f = csv.DictReader(csvfile)
	for row in f:
		#firstname, lastname, affiliation, stage, title
		if row['talk'] == 'Yes' and row['title'] != '':
			g = open("talk-{0}-{1}.md".format(row['firstname'],row['lastname']),"w+")
			g.writelines("--- \n")
			g.writelines("name: {0} \n".format(row['title']))
			g.writelines("speakers: \n - {0} {1}  \n".format(row['firstname'],row['lastname']))
			g.writelines("--- \n \n")
			g.close()
		elif row['talk'] == 'Undecided':
			pass
			#g.writelines("**Title**: *{0}*\n \n".format("TBA"))
			#g.writelines(" **Abstract**:\n \n {0}".format(row['abstract']))
		else:
			pass
		
import csv
with open('registration.csv', newline='',encoding="utf8") as csvfile:
	f = csv.DictReader(csvfile)
	for row in f:
		#firstname, lastname, affiliation, stage, title
		g = open("{0} {1}.md".format(row['firstname'],row['lastname']),"w+")
		g.writelines("--- \n")
		g.writelines("name: {0} {1} ({2}) \n".format(row['firstname'],row['lastname'],row['affiliation']))
		g.writelines("first_name: {0} \n".format(row['firstname']))
		g.writelines("last_name: {0} \n".format(row['lastname']))
		g.writelines("--- \n \n ")
		if row['talk'] == 'Yes':
			g.writelines("**Title**: *{0}*\n \n".format(row['title']))
			g.writelines(" **Abstract**:\n \n ")
		elif row['talk'] == 'Undecided':
			g.writelines("**Title**: *{0}*\n \n".format("TBA"))
			#g.writelines(" **Abstract**:\n \n {0}".format(row['abstract']))
		else:
			pass
		g.close()


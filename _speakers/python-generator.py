import csv
with open('registration-2.csv', newline='',encoding="latin-1") as csvfile:
	f = csv.DictReader(csvfile)
	for row in f:
		#firstname, lastname, affiliation, stage, title
		g = open("{0} {1}.md".format(row['firstname'],row['lastname']),"w+")
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


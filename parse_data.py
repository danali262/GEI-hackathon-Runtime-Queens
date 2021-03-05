import csv

with open ('/home/danali/Downloads/dataset.csv', 'r') as csv_file:
	reader = csv.reader(csv_file, delimiter=",")
	#row = list(reader)
	header = next(reader)
	#print(header)

	us_count = 0
	male_count = 0
	female_count = 0
	
	for row in reader:
		if row[3] == 'United States':
			print(row[56])
			us_count += 1
			if row[56] == 'Female':
				female_count += 1
			elif row[56] == 'Male':
				male_count += 1
print(us_count)
print("number of female employees in the US:", female_count)
print("number of male employees in the US:", male_count)
	

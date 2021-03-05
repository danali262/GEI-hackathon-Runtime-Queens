import csv

with open ('/home/himak/Downloads/dataset.csv', 'r') as csv_file:
	reader = csv.reader(csv_file, delimiter=",")
	#row = list(reader)
	header = next(reader)
	#print(header)

	us_count = 0
	male_count = 0
	female_count = 0
	
	for row in reader:
		if row[3] == 'United States':
			us_count += 1
			if row[56] == 'Female':
				female_count += 1
			elif row[56] == 'Male':
				male_count += 1
	
print(us_count)
print(female_count)
	

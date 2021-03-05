import csv

input_file = '/home/danali/Downloads/dataset.csv'
output_file = 'dataset_clean.csv'
cols_to_remove = [1, 2, 4, 7, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 48, 49, 50, 51, 52, 53, 54, 55]

cols_to_remove = sorted(cols_to_remove, reverse=True)   #reverse so we remove from end first
row_count = 0 #current amount of rows processed

with open (input_file, "r") as csv_file:
	reader = csv.reader(csv_file, delimiter=",")
	with open(output_file, "w", newline='') as result:
		writer = csv.writer(result, delimiter=",")
		for row in reader:
			row_count += 1
			print('\r{0}'.format(row_count), end='') #print rows processed
			for col_index in cols_to_remove:
				del row[col_index]
			writer.writerow(row)

	

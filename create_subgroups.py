import csv

input_file = 'dataset_clean.csv'

male_count = 0
female_count = 0
transgender_count = 0
nonbinary_count = 0
NA_count = 0

with open(input_file, newline='') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        if row[11] == 'Male':
            male_count += 1
        elif row[11] == 'Female':
            female_count += 1
        elif row[11] == 'Transgender':
            transgender_count += 1
        elif row[11] == 'NA':
            NA_count += 1
        else:
            nonbinary_count += 1
total = male_count + female_count + transgender_count + nonbinary_count

print(total)
print("Male percentage")
print(male_count/total)
print("Female percentage")
print(female_count/total)
print("Transgender percentage")
print(transgender_count/total)
print("Nonbinary percentage")
print(nonbinary_count/total)
# print("Percentage of NA")
# print(NA_count/total)
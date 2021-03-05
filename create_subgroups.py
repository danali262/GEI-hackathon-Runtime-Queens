import csv

input_file = 'dataset_clean.csv'

male_count = 0
female_count = 0
transgender_count = 0
nonbinary_count = 0
NA_count_gender = 0

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
            NA_count_gender += 1
        else:
            nonbinary_count += 1
total_responded_gender = male_count + female_count + transgender_count + nonbinary_count

print("Amount of people responded")
print(total_responded_gender)
print("Male percentage")
print(male_count/total_responded_gender)
print("Female percentage")
print(female_count/total_responded_gender)
print("Transgender percentage")
print(transgender_count/total_responded_gender)
print("Nonbinary percentage")
print(nonbinary_count/total_responded_gender)
# print("Percentage of NA")
# print(NA_count_gender/total)

employed_parttime_count = 0
employed_fulltime_count = 0
NA_count_employment = 0

with open(input_file, newline='') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        if row[2] == 'Employed full-time':
            employed_fulltime_count += 1
        elif row[2] == 'Employed part-time':
            employed_parttime_count += 1
        else:
            NA_count_employment += 1
total_responded_employment = employed_fulltime_count + employed_parttime_count

print("Amount of people responded")
print(total_responded_employment)
print("Full-time employment percentage")
print(employed_fulltime_count/total_responded_employment)
print("Part-time percentage")
print(employed_parttime_count/total_responded_employment)
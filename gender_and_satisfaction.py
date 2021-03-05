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

# print("Amount of people responded")
# print(total_responded_gender)
# print("Male percentage")
# print(male_count/total_responded_gender)
# print("Female percentage")
# print(female_count/total_responded_gender)
# print("Transgender percentage")
# print(transgender_count/total_responded_gender)
# print("Nonbinary percentage")
# print(nonbinary_count/total_responded_gender)

satisfied_male_count = 0
satisfied_female_count = 0
satisfied_transgender_count = 0
satisfied_nonbinary_count = 0
dissatisfied_male_count = 0
dissatisfied_female_count = 0
dissatisfied_transgender_count = 0
dissatisfied_nonbinary_count = 0
male_NA_count = 0
female_NA_count = 0
transgender_NA_count = 0
nonbinary_NA_count = 0

with open(input_file, newline='') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        if row[11] == 'Male' and (row[7] == 'Extremely satisfied' or row[7] == 'Moderately satisfied' or row[7] == 'Slightly satisfied'):
            satisfied_male_count += 1
        elif row[11] == 'Female' and (row[7] == 'Extremely satisfied' or row[7] == 'Moderately satisfied' or row[7] == 'Slightly satisfied'):
            satisfied_female_count += 1
        elif row[11] == 'Transgender' and (row[7] == 'Extremely satisfied' or row[7] == 'Moderately satisfied' or row[7] == 'Slightly satisfied'):
            satisfied_transgender_count += 1
        elif row[11] == 'Non-binary, genderqueer, or gender non-conforming' and (row[7] == 'Extremely satisfied' or row[7] == 'Moderately satisfied' or row[7] == 'Slightly satisfied'):
            satisfied_nonbinary_count += 1
        elif row[11] == 'Male' and (row[7] == 'Extremely dissatisfied' or row[7] == 'Moderately dissatisfied' or row[7] == 'Slightly dissatisfied'):
            dissatisfied_male_count += 1
        elif row[11] == 'Female' and (row[7] == 'Extremely dissatisfied' or row[7] == 'Moderately dissatisfied' or row[7] == 'Slightly dissatisfied'):
            dissatisfied_female_count += 1
        elif row[11] == 'Transgender' and (row[7] == 'Extremely dissatisfied' or row[7] == 'Moderately dissatisfied' or row[7] == 'Slightly dissatisfied'):
            dissatisfied_transgender_count += 1
        elif row[11] == 'Non-binary, genderqueer, or gender non-conforming' and (row[7] == 'Extremely dissatisfied' or row[7] == 'Moderately dissatisfied' or row[7] == 'Slightly dissatisfied'):
            dissatisfied_nonbinary_count += 1
        elif row[11] == 'Male' and row[7] == 'NA':
            male_NA_count += 1
        elif row[11] == 'Female' and row[7] == 'NA':
            female_NA_count += 1
        elif row[11] == 'Transgender' and row[7] == 'NA':
            transgender_NA_count += 1
        elif row[11] == 'Non-binary, genderqueer, or gender non-conforming' and row[7] == 'NA':
            nonbinary_NA_count += 1
total_gender_satisfaction = satisfied_male_count + satisfied_female_count + satisfied_transgender_count + satisfied_nonbinary_count + dissatisfied_male_count + dissatisfied_female_count + dissatisfied_transgender_count + dissatisfied_nonbinary_count

# print("Amount of sample")
# print(total_gender_satisfaction)
print("Satisfied males")
print(satisfied_male_count/male_count)
print("Satisfied females")
print(satisfied_female_count/female_count)
print("Satisfied transgenders")
print(satisfied_transgender_count/transgender_count)
print("Satisfied nonbinary, genderqueer, or gender non-conforming")
print(satisfied_nonbinary_count/nonbinary_count)
print("-----------------------------------------------------------------------")
print("Dissatisfied males")
print(dissatisfied_male_count/male_count)
print("Dissatisfied females")
print(dissatisfied_female_count/female_count)
print("Dissatisfied transgenders")
print(dissatisfied_transgender_count/transgender_count)
print("Dissatisfied nonbinary, genderqueer, or gender non-conforming")
print(dissatisfied_nonbinary_count/nonbinary_count)
print("-----------------------------------------------------------------------")
print("NA males")
print(male_NA_count/male_count)
print("NA females")
print(female_NA_count/female_count)
print("NA transgenders")
print(transgender_NA_count/transgender_count)
print("NA nonbinary, genderqueer, or gender non-conforming")
print(nonbinary_NA_count/nonbinary_count)
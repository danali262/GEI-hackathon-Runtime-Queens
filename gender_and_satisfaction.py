import csv

input_file = 'dataset_clean.csv'
output_file = 'gender_and_satisfaction.csv'

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

with open(output_file, "w", newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["", "Amount Satisfied", "Amount Dissatisfied", "Amount Neither Nor", "Amount NA"])
	writer.writerow(["Male", satisfied_male_count, dissatisfied_male_count, male_count - satisfied_male_count - dissatisfied_male_count - male_NA_count, male_NA_count])
	writer.writerow(["Female", satisfied_female_count, dissatisfied_female_count, female_count - satisfied_female_count - dissatisfied_female_count - female_NA_count, female_NA_count])
	writer.writerow(["Transgender", satisfied_transgender_count, dissatisfied_transgender_count, transgender_count - satisfied_transgender_count - dissatisfied_transgender_count - transgender_NA_count, transgender_NA_count])
	writer.writerow(["Non-binary, genderqueer or gender non-conforming", satisfied_nonbinary_count, dissatisfied_nonbinary_count, nonbinary_count - satisfied_nonbinary_count - dissatisfied_nonbinary_count - nonbinary_NA_count, nonbinary_NA_count])
	writer.writerow(["", "", "", "", ""])
	writer.writerow(["", "Percentage Satisfied", "Percentage Dissatisfied", "Percentage Neither Nor", "Percentage NA"])
	writer.writerow(["Male", satisfied_male_count/male_count, dissatisfied_male_count/male_count, (male_count - satisfied_male_count - dissatisfied_male_count - male_NA_count)/male_count, male_NA_count/male_count])
	writer.writerow(["Female", satisfied_female_count/female_count, dissatisfied_female_count/female_count, (female_count - satisfied_female_count - dissatisfied_female_count - female_NA_count)/female_count, female_NA_count/female_count])
	writer.writerow(["Transgender", satisfied_transgender_count/transgender_count, dissatisfied_transgender_count/transgender_count, (transgender_count - satisfied_transgender_count - dissatisfied_transgender_count - transgender_NA_count)/transgender_count, transgender_NA_count/transgender_count])
	writer.writerow(["Non-binary, genderqueer or gender non-conforming", satisfied_nonbinary_count/nonbinary_count, dissatisfied_nonbinary_count/nonbinary_count, (nonbinary_count - satisfied_nonbinary_count - dissatisfied_nonbinary_count - nonbinary_NA_count)/nonbinary_count, nonbinary_NA_count/nonbinary_count])
	writer.writerow(["", "", "", "", ""])
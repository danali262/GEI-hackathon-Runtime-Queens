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

hetero_count = 0
bisexual_count = 0
gaylesbian_count = 0
asexual_count = 0
morethanone_count = 0
NA_count_sexuality = 0

with open(input_file, newline='') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        if row[12] == 'Straight or heterosexual':
            hetero_count += 1
        elif row[12] == 'NA':
            NA_count_sexuality += 1
        elif row[12] == 'Bisexual or Queer':
            bisexual_count += 1
        elif row[12] == 'Gay or Lesbian':
            gaylesbian_count += 1
        elif row[12] == 'Asexual':
            asexual_count += 1
        else:
            morethanone_count += 1
total_responded_sexuality = hetero_count + bisexual_count + gaylesbian_count + asexual_count + morethanone_count

print("Amount of people responded")
print(total_responded_sexuality)
print("Straight or heterosexual percentage")
print(hetero_count/total_responded_sexuality)
print("Bisexual or Queer percentage")
print(bisexual_count/total_responded_sexuality)
print("Gay or Lesbian percentage")
print(gaylesbian_count/total_responded_sexuality)
print("Asexual percentage")
print(asexual_count/total_responded_sexuality)
print("Percentage of people with more than one sexualities")
print(morethanone_count/total_responded_sexuality)

extremely_satisfied_count = 0
moderately_satisfied_count = 0
slightly_satisfied_count = 0
neither_satisfied_nor_dissatisfied_count = 0
slightly_dissatisfied_count = 0
moderately_dissatisfied_count = 0
extremely_dissatisfied_count = 0
NA_count_satisfaction = 0

with open(input_file, newline='') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        if row[7] == 'Extremely satisfied':
            extremely_satisfied_count += 1
        if row[7] == 'Moderately satisfied':
            moderately_satisfied_count += 1
        if row[7] == 'Slightly satisfied':
            slightly_satisfied_count += 1
        if row[7] == 'Neither satisfied nor dissatisfied':
            neither_satisfied_nor_dissatisfied_count += 1
        if row[7] == 'Slightly dissatisfied':
            slightly_dissatisfied_count += 1
        elif row[7] == 'Moderately dissatisfied':
            moderately_dissatisfied_count += 1
        elif row[7] == 'Extremely dissatisfied':
            extremely_dissatisfied_count += 1
        else:
            NA_count_satisfaction += 1
total_responded_satisfaction = extremely_dissatisfied_count + extremely_satisfied_count + moderately_dissatisfied_count + moderately_satisfied_count + slightly_dissatisfied_count + slightly_satisfied_count + neither_satisfied_nor_dissatisfied_count

print("Amount of people responded")
print(total_responded_satisfaction)
print("Extremely satisfied percentage")
print(extremely_satisfied_count/total_responded_satisfaction)
print("Moderately satisfied percentage")
print(moderately_satisfied_count/total_responded_satisfaction)
print("Slightly satisfied percentage")
print(slightly_satisfied_count/total_responded_satisfaction)
print("Neither satisfied nor dissatisfied percentage")
print(neither_satisfied_nor_dissatisfied_count/total_responded_satisfaction)
print("Slightly dissatisfied percentage")
print(slightly_dissatisfied_count/total_responded_satisfaction)
print("Moderately dissatisfied percentage")
print(moderately_dissatisfied_count/total_responded_satisfaction)
print("Extremely dissatisfied percentage")
print(extremely_dissatisfied_count/total_responded_satisfaction)
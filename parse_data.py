import csv
import numpy as np
from sklearn.linear_model import LinearRegression

#class country:
#def __init__(self, namecountry, name, mcount, fcount, nacount, totalcount, ppp):
#	self.name 
#	self.mcount = name #male and female counted
#	self.fcount = fcount
#	self.nacount = nacount
#	self.totalcount = totalcount
#	self.ppp = ppp

def get_age(agestr):
	if agestr == '18 - 24 years old':
		return 1
	if agestr == '25 - 34 years old':
		return 2
	if agestr == '35 - 44 years old':
		return 3
	if agestr == '45 - 54 years old':
		return 4
	if agestr == '55 - 64 years old':
		return 5
	if agestr == '65 years or older':
		return 6
#___________________________________________


with open ('ppp.csv', 'r') as csv_file:
	reader = csv.reader(csv_file, delimiter=",")
	
	i = 0
	xfem = np.empty(10000)
	yfem = np.empty(10000)
	for row in reader:
		if row[11] == 'Female' and row[15] != 'NA' and row[15] != 'Under 18 years old':
			yfem.fill(row[17])
			xfem.fill(get_age(row[15]))
			#print(xfem[i], yfem[i])
			i += 1
	xfem = xfem.reshape((-1, 1))
	model = LinearRegression().fit(xfem, yfem)
	print(model.intercept_)
	print(model.coef_)

import csv
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
#class country:
#def __init__(self, namecountry, name, mcount, fcount, nacount, totalcount, ppp):
#	self.name 
#	self.mcount = name #male and female counted
#	self.fcount = fcount
#	self.nacount = nacount
#	self.totalcount = totalcount
#	self.ppp = ppp

#def get_age(agestr):
#	if agestr == '18 - 24 years old':
#		return 21
#	if agestr == '25 - 34 years old':
#		return 29.5
#	if agestr == '35 - 44 years old':
#		return 39.5
#	if agestr == '45 - 54 years old':
#		return 49.5
#	if agestr == '55 - 64 years old':
#		return 59.5
#	if agestr == '65 years or older':
#		return 70
#___________________________________________

def get_exp(expstr):
	if expstr == '0-2 years':
		return 1
	if expstr == '3-5 years':
		return 5
	if expstr == '6-8 years':
		return 7
	if expstr == '9-11 years':
		return 10
	if expstr == '12-14 years':
		return 13
	if expstr == '15-17 years':
		return 16
	if expstr == '18-20 years':
		return 19
	if expstr == '21-23 years':
		return 22
	if expstr == '24-26 years':
		return 25
	if expstr == '27-29 years':
		return 28
	else:
		return 0

def outlier(salary):
	if salary < '10' and salary > '0':
		return 0
	else:
		return 1

with open ('ppp.csv', 'r') as csv_file:
	reader = csv.reader(csv_file, delimiter=",")
	
	i = 0
	xfem = np.empty(100000)
	yfem = np.empty(100000)

	xman = np.empty(100000)
	yman = np.empty(100000)


	for row in reader:
		if row[11] == 'Female' and row[6] != 'NA' and row[6] != '30 or more years' and row[17] != 'NA' and outlier(row[17]) == 0:
			yfem[i] = row[17]
			xfem[i] = get_exp(row[6])
			print(xfem[i])
		if row[11] == 'Male' and row[6] != 'NA' and row[6] != '30 or more years':
			xman = row[17]
			yman = get_exp(row[6])
		i += 1

	#print(xfem[41])
	plt.scatter(xfem, yfem)
	plt.show()
	#plt.scatter(xman, yman)
	#plt.show()

	xfem = xfem.reshape((-1, 1))
	model = LinearRegression().fit(xfem, yfem)
	print(model.intercept_)
	print(model.coef_)

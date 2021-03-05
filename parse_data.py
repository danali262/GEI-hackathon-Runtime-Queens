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

def filter(salary, edu, country):
	#if edu == "Bachelor's degree (BA, BS, B.Eng., etc." and country == 'United States':
	#if country == 'United States':
		#return 0
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
		if row[11] == 'Female' and row[6] != 'NA' and row[6] != '30 or more years' and row[17] != 'NA' and filter(row[17], row[3], row[1]) == 0:
			yfem[i] = row[17]
			xfem[i] = get_exp(row[6])
			#print(
		if row[11] == 'Male' and row[6] != 'NA' and row[6] != '30 or more years' and row[17] != 'NA' and filter(row[17], row[3], row[1]) == 0:
			yman[i] = row[17]
			xman[i] = get_exp(row[6])
		#print(row[3])
		i += 1
	xfem = xfem.reshape((-1, 1))
	xman = xman.reshape((-1, 1))
	print(np.amax(yman))
	modelfem = LinearRegression().fit(xfem, yfem)
	modelman = LinearRegression().fit(xman, yman)

	fig = plt.figure()
	ax1 = fig.add_subplot(121)
	ax2 = fig.add_subplot(122)
	ax1.scatter(xfem,yfem, alpha=0.14)
	ax2.scatter(xman,yman, alpha=0.14)
	ax1.set_title('female')
	ax1.set_xlabel('x')
	ax1.set_ylabel('y')
	ax2.set_title('male')
	ax2.set_xlabel('x')
	ax2.set_ylabel('y')
	plt.show()	

	print(modelfem.intercept_, modelman.intercept_)
	print(modelfem.coef_, modelman.coef_)

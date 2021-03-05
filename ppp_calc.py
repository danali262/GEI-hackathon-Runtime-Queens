# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import csv
import matplotlib.pyplot as plt


with open('/home/ruben/Downloads/ppp.csv', 'w') as us_csv:
    with open('/home/ruben/Downloads/dataset.csv', 'r') as dataset:
        with open('/home/ruben/Downloads/oecd_ppp.csv', 'r') as ppp:
            read1 = list(csv.reader(dataset, delimiter=","))
            read2 = list(csv.reader(ppp, delimiter=","))

            difflist = [0]
            total = 0
            writer = csv.writer(us_csv)
            writer.writerow(['Respondent', 'Country', 'Employment', 'FormalEducation', 'DevType', 'YearsCoding', 'YearsCodingProf', 'JobSatisfaction', 'ConvertedSalaray', 'CurrencySymbol', 'EthicsChoise', 'Gender', 'SexualOrientation', 'EducationParents', 'RaceEthnicity', 'Age', 'Dependents', 'ppp / corrected salery'])
            for row in read1:
                if row[3] == 'Australia':
                    ppp_country = 54401.4
                elif row[3] == 'Austria':
                    ppp_country = 53902.949044976
                elif row[3] == 'Belgium':
                    ppp_country = 55590.1304610982
                elif row[3] == 'Canada':
                    ppp_country = 53198.172958054
                elif row[3] == 'Czech Republic':
                    ppp_country = 29280.7899702266
                elif row[3] == 'Denmark':
                    ppp_country = 57149.594305945
                elif row[3] == 'Finland':
                    ppp_country = 45697.556152853
                elif row[3] == 'France':
                    ppp_country = 46480.6153991188
                elif row[3] == 'Germany':
                    ppp_country = 53637.8016034603
                elif row[3] == 'Greece':
                    ppp_country = 27459.1258996487
                elif row[3] == 'Hungary':
                    ppp_country = 26223.196713398
                elif row[3] == 'Ireland':
                    ppp_country = 50490.4714068488
                elif row[3] == 'Italy':
                    ppp_country = 39189.365759204
                elif row[3] == 'Japan':
                    ppp_country = 38617.465494035
                elif row[3] == 'Republic of Korea':
                    ppp_country = 42284.789106855
                elif row[3] == 'Luxembourg':
                    ppp_country = 68680.5297308777
                elif row[3] == 'Netherlands':
                    ppp_country = 56552.2904256499
                elif row[3] == 'Norway':
                    ppp_country = 54027.4870519513
                elif row[3] == 'Poland':
                    ppp_country = 31969.5680309974
                elif row[3] == 'Portugal':
                    ppp_country = 26633.7171927498
                elif row[3] == 'Slovakia':
                    ppp_country = 25452.386629151
                elif row[3] == 'Spain':
                    ppp_country = 38757.5699607805
                elif row[3] == 'Sweden':
                    ppp_country = 46695.3498606658
                elif row[3] == 'Switzerland':
                    ppp_country = 66566.7263187086
                elif row[3] == 'United Kingdom':
                    ppp_country = 47226.0876596286
                elif row[3] == 'United States':
                    ppp_country = 65835.5776448653
                elif row[3] == 'Mexico':
                    ppp_country = 17594.4610524478
                elif row[3] == 'Israel':
                    ppp_country = 39403.1025725974
                elif row[3] == 'Slovenia':
                    ppp_country = 40219.6209682093
                elif row[3] == 'Estonia':
                    ppp_country = 30296.8772624036
                elif row[3] == 'Iceland':
                    ppp_country = 68005.7936836116
                elif row[3] == 'New Zealand':
                    ppp_country = 44030.7451831187
                elif row[3] == 'Chile':
                    ppp_country = 26915.8365049051
                elif row[3] == 'Latvia':
                    ppp_country = 28453.5867518221
                elif row[3] == 'Lithuania':
                    ppp_country = 28913.897758748
                else:
                    continue
                if row[26] != 'NA' and row[26] != '0':
                    salery = float(row[26])
                    if salery <= 2000000:
                        diff = (salery / ppp_country)
                        difflist.append(float(diff))
                        total += 1
                        writer.writerow([row[0], row[3], row[5], row[6], row[8], row[9], row[10], row[11], row[26], row[27], row[47], row[56], row[57], row[58], row[59], row[60], row[61], diff])



                       # print(salery)
                      #  print(diff)
                       # print(difflist)

difflist.sort()
print(total)
x = difflist
x2 = 1
y = range(total)
#plt.plot(difflist)
plt.plot(x)
plt.plot(x2)
#plt.subplot(x, 1)
plt.ylabel('difference in perc')
plt.show()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import numpy

def	print_centroid(bill, tip):
	mbill = 0
	mtip = 0

	x = 0
	while x < 6:
		mbill += bill[x]
		x += 1
	x = 0;
	while x < 6:
		mtip += tip[x]
		x += 1
	print("centroid:")
	print(mbill/6)
	print(mtip/6)
	return mbill/6, mtip/6
#______________________________________

def	sum_array(array):
	i = 0
	ret = 0
	while i < 6:
		ret += array[i]
		i += 1
	return ret
#______________________________________
bill = [34, 108, 64, 88, 99, 51]
tip = [5, 17, 11, 8, 14, 5]

mbill, mtip = print_centroid(bill, tip)
print("")
bidev = [0, 0, 0, 0, 0, 0] #Bill deviation
tidev = [0, 0, 0, 0, 0, 0] #Tip deviation
devpro = [0, 0, 0, 0, 0, 0] # Devation products
bdevsq = [0, 0, 0, 0, 0, 0] # Bill deviations squared

i = 0
while i < 6:
	bidev[i] = (bill[i] - mbill)
	tidev[i] = (tip[i] - mtip)
	devpro[i] = (bidev[i] * tidev[i])
	bdevsq[i] = (bidev[i] * bidev[i])
	i += 1
print(bidev)
print(tidev)
print("")
print(devpro)

sum_devpro = sum_array(devpro)
sum_bdevsq = sum_array(bdevsq)
print("sum devpro:", sum_devpro)
print("sum bdevsq:", sum_bdevsq)
print("")

b1 = sum_devpro/sum_bdevsq
print("b1 =", b1)
print("")
print("b0 =", mtip - (b1 * bidev))



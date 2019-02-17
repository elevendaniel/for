date = []
with open ('reviews.txt','r') as f:
	for line in f:
		date.append(line)
print(len(date))

print(date[0])
print('_____________')
print(date[1])

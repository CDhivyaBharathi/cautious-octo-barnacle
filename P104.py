import csv
from collections import Counter

# Finding the Mean
with open('104Project.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data = []
for i in range(len(file_data)):
    num = file_data[i][1]
    new_data.append(float(num))

n = len(new_data)
total = 0

for x in new_data:
    total += x

mean = total/n
print("Mean of the given data = "+ str(mean))



#Finding the median
new_data1.sort()
if n % 2 == 0:
    position1 = float(new_data[n//2])
    position2 = float(new_data[n//2+1])
    median = (position1+position2)/2
else:
    median = new_data[n/2]

print("The median of the given data set = "+str(median))



with open('104Project.csv', newline='') as f:
    reader = csv.reader(f)
    file_data2 = list(reader)

file_data2.pop(0)

new_data2=[]
for i in range(len(file_data2)):
	n_num = file_data2[i][1]
	new_data2.append(n_num)



#Calculating Mode
data = Counter(new_data2)
mode_data_for_range = {
                        "50-60": 0,
                        "60-70": 0,
                        "70-80": 0
                    }
for height, occurence in data.items():
    if 50 < float(height) < 60:
        mode_data_for_range["50-60"] += occurence
    elif 60 < float(height) < 70:
        mode_data_for_range["60-70"] += occurence
    elif 70 < float(height) < 80:
        mode_data_for_range["70-80"] += occurence

mode_range, mode_occurence = 0, 0
for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)
print(f"Mode is -> {mode:2f}")





import csv
from collections import Counter

# Finding the Mean
with open('104Project.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data = []
for i in range(len(file_data)):
    num = file_data[i][2]
    new_data.append(float(num))

n = len(new_data)
total = 0

for x in new_data:
    total += x

mean = total/n
print("Mean of the given data = "+ str(mean))



#Finding the median
new_data.sort()
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
	n_num = file_data2[i][2]
	new_data2.append(n_num)



#Calculating Mode
data = Counter(new_data2)
mode_data_for_range = {
                        "75-85": 0,
                        "85-95": 0,
                        "95-105": 0,
                        "105-115": 0,
                        "115-125": 0,
                        "125-135": 0,
                        "135-145": 0,
                        "145-155": 0,
                        "155-165": 0,
                        "165-175": 0
                    }
for height, occurence in data.items():
    if 75 < float(height) < 85:
        mode_data_for_range["75-85"] += occurence
    elif 85 < float(height) < 95:
        mode_data_for_range["85-95"] += occurence
    elif 95 < float(height) < 105:
        mode_data_for_range["95-105"] += occurence
    elif 105 < float(height) < 115:
        mode_data_for_range["105-115"] += occurence
    elif 115 < float(height) < 125:
        mode_data_for_range["115-125"] += occurence
    elif 125 < float(height) < 135:
        mode_data_for_range["125-135"] += occurence
    elif 135 < float(height) < 145:
        mode_data_for_range["135-145"] += occurence
    elif 145 < float(height) < 155:
        mode_data_for_range["145-155"] += occurence
    elif 155 < float(height) < 165:
        mode_data_for_range["155-165"] += occurence
    elif 165 < float(height) < 175:
        mode_data_for_range["165-175"] += occurence

mode_range, mode_occurence = 0, 0
for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)
print(f"Mode is -> {mode:2f}")









import random
import csv
import time

start_time = time.time()

first_phase = random.randint(0,1)
img_list = []

if first_phase == 0:
    csv_file = open('Reference.csv', 'r')
    img_index = 2
    csv_reader = csv.reader(csv_file)
    for i in csv_reader:
        img_list.append(i)
else:
    csv_file = open('Probe.csv', 'r')
    img_index = 3
    csv_reader = csv.reader(csv_file)
    for i in csv_reader:
        img_list.append(i)

#print(img_list[random.randint(0, len(img_list) - 1)][img_index])

ImageA_rand = 'images2/' + img_list[random.randint(0, len(img_list) - 1)][img_index]
#print(ImageA_rand)
#ImageA_rand = 'images2/' + ImageA_rand
print("--- %s seconds ---" % (time.time() - start_time))

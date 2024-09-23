import csv
import random


probe_file = open('Probe.csv', 'r')
probe_reader = csv.reader(probe_file)

img_list = []

for i in probe_reader:
    img_list.append(i)

tracker_file = open('ProbeMemory.csv', 'r')
tracker_reader = csv.reader(tracker_file)

tracker_list = []

cont = False
while True:
    rand_img = img_list[random.randint(0, len(img_list) - 1)]
    for i in tracker_reader:
        for j in i:
            tracker_list.append(j)
            #print(j)
            if j == rand_img[0]:
                cont = True
                break
    if not cont:
        break

tracker_file.close()

tracker_list.append(rand_img[0])
tracker_file_write = open('ProbeMemory.csv', 'w')
tracker_writer = csv.writer(tracker_file_write)
tracker_writer.writerow(tracker_list)

print(rand_img)

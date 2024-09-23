import random
import time
import csv

start_time = time.time()

probe_file = open('Probe.csv', 'r')
probe_reader = csv.reader(probe_file)

img_list = []

for i in probe_reader:
    img_list.append(i)

master_probe_img_list = []

num_list = random.sample(range(1, 36), 35)

for n in num_list:
    img_num_list = []
    for i in img_list:
        #print('%s, %s' % (n, i[0]))
        if int(i[0]) == int(n):
            img_num_list.append(i)
    chosen_img = img_num_list[random.randint(0, len(img_num_list) - 1)]
    img_list.remove(chosen_img)
    master_probe_img_list.append(chosen_img[3])

print(master_probe_img_list)
print(len(master_probe_img_list))

print("--- %s seconds ---" % (time.time() - start_time))

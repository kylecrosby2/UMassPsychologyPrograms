import csv
import random

numReps = 590
master_reference_list = []

hetero_file = open('HeteroInducer.csv', 'r')
hetero_reader = csv.reader(hetero_file)
hetero_img_list = []
for i in hetero_reader:
    hetero_img_list.append(i)


homo_file = open('HomoInducer.csv', 'r')
homo_reader = csv.reader(homo_file)
homo_img_list = []
for i in homo_reader:
    homo_img_list.append(i)

for i in range(numReps//2):
    master_reference_list.append(0)
for i in range(numReps//2):
    master_reference_list.append(1)

random.shuffle(master_reference_list)

print(master_reference_list)

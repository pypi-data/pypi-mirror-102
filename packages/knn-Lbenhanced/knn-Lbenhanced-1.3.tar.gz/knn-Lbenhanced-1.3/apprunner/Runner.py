import sys
import timeit
sys.path.append("/Users/morad/PycharmProjects/KNN-LB/KnnLb")
from FileReader import FileReader
from KnnLb import KnnLb
from datetime import date
import numpy as np
from Sequence_stats import SequenceStats
import time
import random
import joblib

name = ""
training_path = ""
testing_path = ""
window = 0
D = 0
V = 0
neighbors = 1
random.seed(1234)

if len(sys.argv) > 1:
    for i in range(2, len(sys.argv)):
        options = sys.argv[i].split("=")
        arg = options[0]
        value = options[1]
        if arg == "-name":
            name = value
        elif arg == "-train":
            training_path = value
        elif arg == "-test":
            testing_path = value
        elif arg == "-window":
            window = float(value)
        elif arg == "-n":
            neighbors = int(value)
        elif arg == "-v":
            V = float(value)

# Load data
train_file = FileReader.load_data(training_path)
test_file = FileReader.load_data(testing_path)

# Create datasets

train_data, train_labels = FileReader.parse_arff_data(train_file)
test_data, test_labels = FileReader.parse_arff_data(test_file)

sequence_stats_cache = SequenceStats(test_data)

train_data = np.array(train_data)
train_labels = np.array(train_labels)
test_data = np.array(test_data)
test_labels = np.array(test_labels)

m = KnnLb(n_neighbors=1, max_warping_window=10, window=1, V=20)
m.fit(train_data, train_labels)
start = timeit.default_timer()
stop = timeit.default_timer()

joblib.dump(m, 'knnlb_' + name + '_model.sav')

exit(0)

aciertos = 0
fallos = 0

accuracy = m.predict(test_data[0])
exec_time = (stop - start)
print("Accuracy: ", accuracy)


print("Time execution: ", exec_time)

f_path = '../outputs/' + name + '_KNN_LB_' + str(date.today()) + "_" + \
         str(time.localtime().tm_hour) + "-" + str(time.localtime().tm_min) + "-" + \
         str(time.localtime().tm_sec) + ".csv"
linea = name + ',' + str(window) + ',' + str(V) + ',' + str(neighbors) + ',' + str(round(accuracy, 5)) + ',' + str(
    round(exec_time, 5))
with open(f_path, 'w+') as file:
    file.writelines("name,window,V,Neighbors,accuracy,exec_time\n")
    file.write("%s\n" % linea)
file.close()

import matplotlib.pyplot as plt

exec_times = {}                             # Dictionary that will store execution times.
file = open("Results.txt","r")
for line in file:                           # Storing execution times from the file.
    lst = line.split()
    exec_times[int(lst[0])] = float(lst[2])

#plt.rcParams["figure.figsize"] = [7.50, 3.50]
#plt.rcParams["figure.autolayout"] = True

plt.plot(list(exec_times.keys()),list(exec_times.values()),marker="o") # Creating the graph with the help of matplotlib library.
plt.axis([1,100,0.0001,0.0008])    
plt.ylabel('time (seconds)')
plt.xlabel('Length of the List')
plt.title('Boyut-Zaman Grafiği')
plt.show()
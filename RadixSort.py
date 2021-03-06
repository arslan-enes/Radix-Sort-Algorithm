import math
import time
start_time = time.perf_counter()
file = open("100000.txt","r") # File name goes here
new_lines=[]

for line in file:
    new_lines.append(float(line))
    
file.close()
digits = [10000,1000,100,10,1,0.1,0.01,0.001]
for digit in digits[::-1]:
    new_lines.sort(key=lambda x : (x/digit)%10) # With the help of 'key' argument, sort method can sort by the provided value.
    # For example (195/10)%10 gives the tens digit and sort algorithm only sort by the tens digit.
    # Then it goes from least valueable digits to most.

    # With activation of this lines below, user can see the steps of the Radix Sort
    # print(new_lines) 
    # print("Sorted by " + str(digit))

print(new_lines)
print(time.perf_counter()-start_time)
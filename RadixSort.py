import math
file = open("100000likliste 4.txt","r") # File name goes here
new_lines=[]

for line in file:
    new_lines.append(float(line))
    
file.close()
digits = [10000,1000,100,10,1,0.1,0.01,0.001]
for digit in digits[::-1]:
    new_lines.sort(key=lambda x : (x/digit)%10)
    print(new_lines)
    print("Sorted by " + str(digit))
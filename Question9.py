N = int(input("enter number of students"))  # input from user
lb = []
print("enter the weights of {} students in lbs".format(N))
for i in range(N):
 lb.append(int(input()))
 kg = []
for i in range(N):
 value = "{:.2f}".format(lb[i]*0.45359237)  # converting lbs to kgs
 kg.append(float(value))
print(kg)
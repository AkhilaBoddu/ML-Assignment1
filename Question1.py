import statistics
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sorting the List of ages in order
ages.sort()
print(ages)
print("The minimum age in the list is %d" %min(ages))
print("The maximum age in the list is %d"%max(ages))
# Adding the min and max values of ages to the list
ages.append(min(ages))
ages.append(max(ages))
ages.sort()
print(ages)
print("The average of the ages is %d"%(sum(ages)/len(ages)))
print("The range of the ages in the list is %d"%(max(ages)-min(ages)))
print ("The median of the ages is %d"%(statistics.median(ages)))
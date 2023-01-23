it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print("THE LENGTH OF IT COMPANIES IS ",len(it_companies))  # length
it_companies.add('TCS')                      # adding to set it_companies
it_companies.update(['INFOSYS','COGNIZANT','WIPRO'])  # adding multiple it companies to set
print("THE IT COMPANIES ARE", it_companies)
it_companies.pop()      # remove one value from set
print("THE COMPANIES AFTER REMOVING RANDOM COMPANY",it_companies)
# The difference between remove and discard is that remove() method displays an error if the element is missing in a set , where as discard() method doesn't display anything if any element is missing
C=A.union(B)  # join a and b sets
print("A UNION B",C)
print("A INTERSECTION B",A.intersection(B))  # a intersection b
print("A SUBSET B?",A.issubset(B))  # a subset b?
print("A IS DISJOINT OF B?",A.isdisjoint(B))  # a disjoint b?
A.update(B)  # joining a with b
B.update(A)  # joining b with a
print("UPDATED A after joining with b",A)
print("UPDATED B after joining with a",B)
print("SYMMETRIC DIFFERENCE BETWEEN A AND B is :",A.symmetric_difference(B))  # symmetric difference
del A  # deleting all sets
del B
del it_companies
a=len(age)  # converting age list into set
b=set(age)
print("THE AGE AFTER CONVERTING INTO SET",b)
c=len(b)
print("the length of age is " ,a,"the length of age after becoming set is", c)
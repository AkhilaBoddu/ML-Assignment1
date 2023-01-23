Sentance='I am a teacher and I love to inspire and teach people'
#spliting the sentence by using the split function
list=Sentance.split()
print(list)
#finding the unique words in the sentance by using set function
teacher=set(list)
print(teacher)
print("The no of unique words in the sentence are %d"%(len(teacher)))

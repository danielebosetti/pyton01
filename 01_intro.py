import csv

csv_file=open("EN_bolt_strength.txt","r") 
csv_reader=csv.reader(csv_file, delimiter='\t')
# note, the csv_reader will read strings
# need to convert them to double-s

# convert string to double :
# https://stackoverflow.com/questions/482410/how-do-i-convert-a-string-to-a-double-in-python

# lists in python
# https://docs.python.org/3/tutorial/datastructures.html

# create an empty list (list of rows)
# note, this variable is called "matrix", but the object is actually a list (1-dimensional)
# anyway..
matrix=[]

for line in csv_reader:
  print("reading line from csv")
  # create an empty list (store the row numbers)
  row=[]
  for cell in line:
    print(cell+1)
    print(type(cell))
    number=float(cell)
    row.append(number)
  # append a row to the matrix
  matrix.append(row)

print(matrix)
print(matrix[0][0])
print(matrix[0][1])

csv_file.close()

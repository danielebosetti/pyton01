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






import json

#bolts strengths as per EN 1993-1-8 Table 3.1
file = open ("EN_bolt_strength.txt","r") 
EN_bolt_strenth_table=json.load(file)
file.close()

def fyb(boltClass):
    fyb=0
    for iClass in range(len(EN_bolt_strenth_table[0])-1):
        if boltClass == EN_bolt_strenth_table[0][iClass]:
            fyb=EN_bolt_strenth_table[1][iClass]
    return(fyb)

def fub(boltClass):
    fub=0
    for iClass in range(len(EN_bolt_strenth_table[0])):
        if boltClass == EN_bolt_strenth_table[0][iClass]:
            fub=EN_bolt_strenth_table[2][iClass]
    return(fub)


#materials safety factors as per EN 1993-1-8 §2.2 (2)
file = open ("EN_safety_factors_res.txt","r") 
EN_safety_factors_res_table=json.load(file)
file.close()

def SFm(safetyFactor):
    SFm=0
    for iFactor in range(len(EN_safety_factors_res_table[0])):
        if safetyFactor == EN_safety_factors_res_table[0][iFactor]:
            SFm=EN_safety_factors_res_table[1][iFactor]
    return(SFm)



#bolts unthreaded and threaded areas
file = open ("bolts_areas.txt","r") 
bolts_areas_table=json.load(file)
file.close()

def Agross(diameter):
    Agross=0
    for iDiameter in range(len(bolts_areas_table)):
        if diameter == bolts_areas_table[iDiameter][0]:
            Agross=bolts_areas_table[iDiameter][1]
    return(Agross)

def Athreaded(diameter):
    Athreaded=0
    for iDiameter in range(len(bolts_areas_table)):
        if diameter == bolts_areas_table[iDiameter][0]:
            Athreaded=bolts_areas_table[iDiameter][2]
    return(Athreaded)


# coefficient as per EN1993-1-8 Table 3.4
def alfaV(boltClass,shearPlane="thread"):
        alfaV=0
        if shearPlane=="thread":
            if boltClass==4.6 :
                  alfaV=0.6  
            if boltClass==5.6 :
                  alfaV=0.6  
            if boltClass==8.8 :
                  alfaV=0.6  
            if boltClass==4.8 :
                  alfaV=0.5  
            if boltClass==5.8 :
                  alfaV=0.5  
            if boltClass==6.8 :
                  alfaV=0.5  
            if boltClass==10.9 :
                  alfaV=0.5
        if shearPlane=="shank":
            alfaV=0.6
        return alfaV

        #bolt shear resistance per shear plane - EN1993-1-8 Table 3.4
def FvRd(diameter, boltClass, shearPlane="thread"):
    A = 0
    if shearPlane == "thread" :
        A = Athreaded(diameter)
    if shearPlane == "shank" :
        A = Agross(diameter)
    
    FvRd = alfaV(boltClass, shearPlane) * fub(boltClass) * A / SFm("gm2")
    return FvRd









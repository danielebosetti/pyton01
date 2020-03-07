from enum import Enum

# for debug: the module code is called once
print('initializing bolt-names')

# enum names must be valid variable names (so _4_6 instead of 4.6)
BoltNames = Enum('BoltName', '_4_6 _4_8 _5_6 _5_8 _6_8 _8_8 _10_9')

# define bolt-class as in eurocode[..] 3.1.1 General
class BoltClass:
  def __init__(self, name, label, yfb, yub):
    self.name=name
    self.label=label
    self.yfb=yfb
    self.yub=yub

  def toString(self):
    return 'BoltClass[{}]'.format(self.label)
  
  # string conversion, used in print()
  def __str__(self):
    return self.toString()
    
  # string conversion, used eg. when printing a list
  def __repr__(self):
    return self.toString()

boltClasses=[
  BoltClass(BoltNames._4_6, '4.6', 240, 400),
  BoltClass(BoltNames._4_8, '4.8', 320, 400),
  BoltClass(BoltNames._5_6, '5.6', 300, 500),
  BoltClass(BoltNames._5_8, '5.8', 400, 500),
  BoltClass(BoltNames._6_8, '6.8', 480, 600),
  BoltClass(BoltNames._8_8, '8.8', 640, 800),
  BoltClass(BoltNames._10_9, '10.9', 900, 1000)
]

# create an empty map
boltByLabel={}

# create an empty map
boltByName={}

# store all bolts by label
for bolt in boltClasses:
  boltByLabel[bolt.label]=bolt

for bolt in boltClasses:
  boltByName[bolt.name]=bolt

# return the bolt-class by label (eg. label='4.6')
def getBoltByLabel(label):
  return boltByLabel[label]

def getAlphaFor(boltClass):
  boltName=boltClass.name
  if boltName in [BoltNames._4_6, BoltNames._5_6, BoltNames._8_8]:
    return 0.6
  elif boltName in [BoltNames._4_8, BoltNames._5_8, BoltNames._6_8, BoltNames._10_9]:
    return 0.5
  else:
    errMsg='invalid boltName=[{}]'.format(boltName)
    raise ValueError(errMsg)
 
def shearResPerShearPlaneThreaded(boltClass, fUB, A, yM2):
  alphaV = getAlphaFor(boltType);
  return shearResPerShearPlane(alphaV, fUB, A, yM2)

def shearResPerShearPlaneUnthreaded(fUB, A, yM2):
  return shearResPerShearPlane(0.6, fUB, A, yM2)

def shearResPerShearPlane(alphaV, fUB, A, yM2):
  return ( alphaV * fUB * A ) / ( yM2 )

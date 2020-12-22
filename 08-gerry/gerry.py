##import the random library to help w vote randomness

import random

##variables
totalPopulation = 99
numRows = 3
numCols = 6
numOfDistrict = 6
myState=[[]]
popSums = [0] * (numOfDistrict+1)   
#note that this ^^ starts at 1 


#creates a cell containing attributes population, district # and vote
class genCell(object):   
    def __init__(self, population, district, vote):
        self.population = population
        self.district = district
        self.vote = vote

#creates population
def totalPop():
  global myState
  total = 0
  for i in range(numRows):
    for j in range(numCols):
      total = total + myState[i][j].population
  return total


    #prints state totals by iterating through 
    #prints district #, population and vote results
def displayMyState():
  global myState
  print("My State:")
  for i in range(numRows):
    print(i,end="\t")
    for j in range(numCols):
      print(myState[i][j].district, myState[i][j].population, myState[i][j].vote, end=",\t")
    print()


def standardDistrict():
  global prple_state
  districtCells = numRows * numCols / numOfDistrict
  distNum = 1
  numCells = 0

  for i in range(numRows):
    for j in range(numCols):
      myState[i][j].district = distNum
      numCells += 1
      if numCells >= districtCells:
        distNum = distNum + 1
        numCells = 0
        
def printPopSums():
    global popSums
    targetPop = totalPop() / numOfDistrict
    print()
    print("Target Population: ", int(targetPop))
    print()
    print("District Population")
    for i in range(1, numOfDistrict+1):
        print("\t",i,"\t\t",popSums[i])

#helper for testing to change variables
#def updateVars(distNum,addPop,addCells):
#    global myState
#    global numCells,popSum
#    myState[i][j].district = distNum
#    # popSum = addPop + myState[i][j].population
#    numCells = addCells + 1
#    return popSum + addPop
           
    
def makeDistricts():
  global myState
  global popSums, popSum, numCells
  targetPop = totalPop() / numOfDistrict
  districtCells = numRows * numCols / numOfDistrict
   # starts at 1, not 0
  popSum = 0
  numCells = 0
  distNum = 1
  over = False

  for i in range(numRows):
    for j in range(numCols):
      if ((over and
           popSum + myState[i][j].population >= targetPop)
           or (numCells >= districtCells +1)):
        over = False
        distNum = incDistSaveSums(distNum,popSum)
        myState[i][j].district = distNum
        popSum = myState[i][j].population
        numCells = 1
      else:
        myState[i][j].district = distNum
        popSum = popSum + myState[i][j].population
        numCells = numCells + 1
        if ((popSum >= targetPop)
             or (numCells >= districtCells +1)):
          over = True
          distNum = incDistSaveSums(distNum,popSum)
          popSum = 0
          numCells = 0
  # updates last sum for the last district
  popSums[numOfDistrict] = popSums[numOfDistrict] + popSum

#checks if number in district is less than number possible and saves sum 
def incDistSaveSums(distNum,popSum):
    global popSums
    popSums[distNum]=popSum
    if distNum < numOfDistrict:        
          distNum = distNum + 1
    return distNum 

#makes state w random population and random votes
def genState():
    global myState
    myState = [[ 
        genCell(random.randint(1,totalPopulation),  
        # random population
             1,  # district
             random.randint(0,1)) # randomly selects voter type
        for j in range(numCols) ] 
          for k in range(numRows) ]


genState()
makeDistricts()
printPopSums()
displayMyState()

from typing import List
# from sys import stdin
import sys
# next line redirect input from file as console input
# is required only with microsoft, then in unix systems
# you can delete or coment it.
sys.stdin = open("structures\segment_tree\input.txt", "r")

# next line redirect input from file as console input
# is required only with microsoft, then in unix systems
# you can delete or coment it.
sys.stdout = open('structures\segment_tree\output.txt', 'w')

class SegmentTree:

  def __init__(self,data:List[int]):
    segmentSize = 4*len(data)
    self.__segmentsMin = [0]*segmentSize # segment tree minimun values
    self.__segmentMax = [0]*segmentSize # segment tree maximun values
    self.__data = data
    self.__buildSegmentTree(1,0,len(data)-1)

  def left(self,position:int):
    return position<<1
  def right(self,position:int):
    return (position<<1)+1

  # Section 1: Main method build the segment(s) tree(s)
  # Build segment tree or in this case we are using a collection for each
  # posible segment tree (min and max values for some interval)
  def __buildSegmentTree(self,position:int,left:int,right:int):
    if(left==right):
      self.__segmentsMin[position] = left
      self.__segmentMax[position] = left
    else:
      leftSide = self.left(position)
      righSide = self.right(position)
      self.__buildSegmentTree(leftSide,left,(left+right)//2)
      self.__buildSegmentTree(righSide,((left+right)//2)+1,right)
      # this line include each value in its correc position inside
      # segment tree.
      self.__setValue(position, leftSide, righSide)


  #Section 2: populating data in segment tree(s)
  # set all segment trees with values for future queries
  def __setValue(self, position, leftSide, righSide):
    self.__setSegmentMin(position, leftSide, righSide)
    self.__setSegmentMax(position,leftSide,righSide)

  # set min value inside an interval for the minimun segment tree
  def __setSegmentMin(self, position, leftSide, righSide):
      p1 = self.__segmentsMin[leftSide]
      p2 = self.__segmentsMin[righSide]
      self.__segmentsMin[position] = p1 if self.__data[p1]<self.__data[p2] else p2

  # set min value inside an interval for the minimun segment tree
  def __setSegmentMax(self, position, leftSide, righSide):
      p1 = self.__segmentMax[leftSide]
      p2 = self.__segmentMax[righSide]
      self.__segmentMax[position] = p1 if self.__data[p1]>self.__data[p2] else p2

  # Section 3: query methods to get data from segment trees
  def getMaxValue(self, startInterval:int,endInterval:int)->int:
    indexMinValue =  self.__qrm(1,0,len(self.__data)-1,startInterval,endInterval,self.__segmentMax,False)
    return self.__data[indexMinValue]

  def getMinValue(self, startInterval:int,endInterval:int)->int:
    indexMaxValue =  self.__qrm(1,0,len(self.__data)-1,startInterval,endInterval,self.__segmentsMin)
    return self.__data[indexMaxValue]

  def __qrm(self,position:int, L:int,R:int,startInterval:int,endInterval:int, segmentTree:List[int],isMin=True)->int:
    if(startInterval>R or endInterval<L):return -1
    if(L>=startInterval and endInterval>=R):
      return segmentTree[position]

    leftSide = self.left(position)
    rightSide = self.right(position)

    p1 = self.__qrm(leftSide,L,(L+R)//2,startInterval,endInterval,segmentTree,isMin)
    p2 = self.__qrm(rightSide,((L+R)//2)+1,R,startInterval,endInterval,segmentTree,isMin)
    if(p1 == -1): return p2
    if(p2 == -1):return p1
    if(isMin):
      return p1 if self.__data[p1]<=self.__data[p2] else p2
    else:
      return p1 if self.__data[p1]>=self.__data[p2] else p2

def printMinQueryResult(segment:SegmentTree ,start:int,end:int):
  minTeplate = "The min value for [{},{}] is {}"
  minimumValue = segment.getMinValue(start,end)
  print(minTeplate.format(start,end,minimumValue))

def printMaxQueryResult(segment:SegmentTree ,start:int,end:int):
  maxTeplate = "The max value for [{},{}] is {}"
  maximumValue = segment.getMaxValue(start,end)
  print(maxTeplate.format(start,end,maximumValue))

if __name__ == '__main__':
    for line in sys.stdin:
      collection:List[int] = [int(element) for element in line.split(",")]
      print("\noriginal collection: {}\n".format(collection))
      size = len(collection)

      segment = SegmentTree(collection)

      ## asking aboutt min and max values between [start,end] intervals
      print("Asking about min values:")
      printMinQueryResult(segment,0,size-1)
      printMinQueryResult(segment,0,size//2)
      printMinQueryResult(segment,size//2,size-1)

      print("\nAsking about max values:")
      printMaxQueryResult(segment,0,size-1)
      printMaxQueryResult(segment,0,size//2)
      printMaxQueryResult(segment,size//2,size-1)
      print("___________________________________________________________________")
import string
import random

class color:
  #  PURPLE = '\033[95m'
  #  CYAN = '\033[96m'
  #  DARKCYAN = '\033[36m'
  #  BLUE = '\033[94m'
   GREEN = '\033[92m'
  #  YELLOW = '\033[93m'
  #  RED = '\033[91m'
  #  BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[00m'

def fileToArray(filePath):
  '''
  Return a file of words as list
  '''
  file = open(filePath, 'r')
  linesList = file.readlines()
  file.close()
  return linesList


def generateRandList(length):
  ''' 
  Generate random list of Uppercase chars with provided length
  '''
  randChars = []
  for _ in range(length):
    randChars.append(chr(random.randrange(65,91)))
  return randChars


def getRndIndex(usedIndexs,wordLength):
  '''
  Return unused index
  '''
  flag = True
  marks = 0
  index = 0
  while flag:
    rndIndex = random.randrange(0,len(charsList))
    for x in range(rndIndex , rndIndex + wordLength):
      if x not in usedIndexs:
        marks += 1
    if marks == wordLength:
      flag = False;
      index = rndIndex
  return index;


def getRndWord():
  rndWord = random.choice(wordsList)
  rndWord = str.strip(rndWord)
  print(" Word:", rndWord)
  return list(rndWord)


def injectRealWords():
  usedIndexs = []
  for _ in range(5):
    rndWord = getRndWord();
    index = getRndIndex(usedIndexs, len(rndWord))
    for i in range(len(rndWord)):
      charsList[(index + i)%len(charsList)] = rndWord[i]

def render():
  '''
    Render the characters as table
  '''
  for row in range(rows):
    subList = charsList[row * cols :row * cols + cols ]
    print (color.GREEN, "|", color.END, end="")
    for col in range(cols):
      print(color.UNDERLINE,
      subList[col]
      ,color.END,
      end = (color.GREEN+ "|"+ color.END))
    print ("")


rows = 20
cols = 20
wordsList = fileToArray('wordsList')
charsList = generateRandList(rows * cols)
injectRealWords()
render()
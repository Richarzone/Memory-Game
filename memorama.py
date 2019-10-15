import random
import pandas as pd
import numpy as np

#Creates table with numbers
def Tablero():
  global DFNum, tabNum
  
  tablero = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18]
  r1 = []
  r2 = []
  r3 = []
  r4 = []
  r5 = []
  r6 = []

  #Creates rows of the table with numbers
  random.shuffle(tablero)
  for i in range(0,6):
    r1.append(tablero[i])
  for i in range(6,12):
    r2.append(tablero[i])
  for i in range(12,18):
    r3.append(tablero[i])
  for i in range(18,24):
    r4.append(tablero[i])
  for i in range(24,30):
    r5.append(tablero[i])
  for i in range(30,36):
    r6.append(tablero[i])
    
  DFNum = pd.DataFrame([r1, r2, r3, r4, r5, r6], columns=['A', 'B', 'C', 'D', 'E', 'F'], index=['1|','2|','3|','4|','5|','6|'])
  tabNum = DFNum.to_numpy()
  print(DFNum)
  print()

def TableroOculto():
  global DFStar, tabStar, s1, s2, s3, s4, s5, s6

  stars = []
  star = " X"
  s1 = []
  s2 = []
  s3 = []
  s4 = []
  s5 = []
  s6 = []
  for i in range(0,6):
    for j in range(0,6):
      stars.append(star)
  #Creates rows of the table with numbers
  for i in range(0,6):
    s1.append(stars[i])
  for i in range(6,12):
    s2.append(stars[i])
  for i in range(12,18):
    s3.append(stars[i])
  for i in range(18,24):
    s4.append(stars[i])
  for i in range(24,30):
    s5.append(stars[i])
  for i in range(30,36):
    s6.append(stars[i])
  
  DFStar = pd.DataFrame([s1, s2, s3, s4, s5, s6], columns=['A', 'B', 'C', 'D', 'E', 'F'], index=['1|','2|','3|','4|','5|','6|'])
  tabStar = DFStar.to_numpy()
  print(DFStar)
  print()

#Sets the board
def startingTab(DFStar):
  global currentTab
  currentTab = DFStar
#Game starts
def listas(tabStar, tabNum):
  global numList, starList

  numList = tabNum.tolist()
  starList = tabStar.tolist()

counter = 0

def Turn1():
  global C1, R1, C12, R12, c1num, c12num
  print("Turno del jugador 1")
  print("Selecciona las coordenadas de las cartas que quieras destapar: ")
  print("Carta 1")
  C1 = input("Columna: ")
  R1 = int(input("Linea: "))
  print("Carta 2")
  C12 = input("Columna: ")
  R12 = int(input("Linea: "))
  

  #First coordenate
  c1low = C1.lower()
  for i in c1low:
    c1num = ord(i) - 96
  
  c1num = c1num - 1
  R1 = R1 - 1 

  #Second coordenate
  c12low = C12.lower()
  for i in c12low:
    c12num = ord(i) - 96

  c12num = c12num - 1
  R12 = R12 - 1 

  CurrentTable(starList, numList, tabNum, tabStar, R1, c1num, R12, c12num, currentTab, DFStar, counter)

def Turn2():
  global C2, R2, C22, R22, c2num, c22num, numList, starList
  print()
  print("Turno del jugador 2")
  print("Selecciona las coordenadas de las cartas que quieras destapar: ")
  print("Carta 1")
  C2 = input("Columna: ")
  R2 = int(input("Linea: "))
  print("Carta 2")
  C22 = input("Columna: ")
  R22 = int(input("Linea: "))

  #First coordenate
  c2low = C2.lower()
  for i in c2low:
    c2num = ord(i) - 96
  
  c2num = c2num - 1
  R2 = R2 - 1 

  #Second coordenate
  c22low = C22.lower()
  for i in c22low:
    c22num = ord(i) - 96

  c22num = c22num - 1
  R22 = R22 - 1 

  CurrentTable2(starList, numList, tabNum, tabStar, R2, c2num, R22, c22num, currentTabcomb1)


def CurrentTable(starList, numList, tabNum, tabStar, R1, c1num, R12, c12num, currentTab, DFStar, counter):
  global currentTabcomb1 

  print("counter: ", counter)

  starList[R1][c1num] = str(numList[R1][c1num])
  starList[R12][c12num] = str(numList[R12][c12num])

  currentTabcomb1 = pd.DataFrame([starList[0],starList[1],starList[2],starList[3],starList[4],starList[5]], columns=['A', 'B', 'C', 'D', 'E', 'F'], index=['1|','2|','3|','4|','5|','6|'])

  currentTab = currentTabcomb1

  print(currentTabcomb1)
  input("Press Enter to continue...")
  if str(numList[R1][c1num]) == str(numList[R12][c12num]):
    currentTab = currentTabcomb1
  elif counter == 0:
    currentTab = currentTab
    starList[R1][c1num] = ' X'
    starList[R12][c12num] = ' X'
    print(DFStar)
  elif counter > 0:
      print(currentTab)
  counter += 1
  print()
  print("counter: ", counter)
  Turn2()


def CurrentTable2(starList, numList, tabNum, tabStar, R2, c2num, R22, c22num, currentTabcomb1):

  starList[R2][c2num] = str(numList[R2][c2num])
  starList[R22][c22num] = str(numList[R22][c22num])

  currentTab2 = pd.DataFrame([starList[0],starList[1],starList[2],starList[3],starList[4],starList[5]], columns=['A', 'B', 'C', 'D', 'E', 'F'], index=['1|','2|','3|','4|','5|','6|'])

  print(currentTab2)
  input("Press Enter to continue...")
  if str(numList[R2][c2num]) == str(numList[R22][c22num]):
    currentTabcomb1 = currentTab2
  else:
    currentTabcomb1 = currentTabcomb1
    starList[R2][c2num] = ' X'
    starList[R22][c22num] = ' X'
    print(currentTabcomb1)
    currentTabcomb1 = currentTab2
  
  print()
  Turn1()

#First calls
Tablero()
TableroOculto()
startingTab(DFStar)
listas(tabStar, tabNum)
Turn1()
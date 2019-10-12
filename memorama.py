import random
import pandas as pd

#This was the fastest way I could find to do this on the bus XD

def Tablero():
  r1 = []
  r2 = []
  r3 = []
  r4 = []
  r5 = []
  r6 = []
  tablero = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18]
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
    
  tabNum = pd.DataFrame([r1, r2, r3, r4, r5, r6], columns=['A', 'B', 'C', 'D', 'E', 'F'], index=[1,2,3,4,5,6])
  print(tabNum)
def TableroOculto():
  stars = []
  star = "*"
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
  tabStar = pd.DataFrame([s1, s2, s3, s4, s5, s6], columns=['A', 'B', 'C', 'D', 'E', 'F'], index=[1,2,3,4,5,6])
  print(tabStar)

#TableroOculto()
#Tablero()
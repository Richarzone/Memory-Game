from random import shuffle
def crearListanum():
    lista = []
    for i in range(18):
        n = i + 1
        for _ in range(2):
            lista.append(n)
    shuffle(lista)
    return lista

def crearTab():
    temp = []
    tablero = []
    for x in numList:
        if len(temp) < 5:
            temp.append(x)
        else:
            temp.append(x)
            tablero.append(temp)
            temp = []
    return tablero

def crearTabOculto():
    #Crea el tablero con las cartas boca abajo
    temp = []
    xlist = []
    for x in range(0,36):
        if len(temp) < 5:
            temp.append(" X")
        else:
            temp.append(" X")
            xlist.append(temp)
            temp = []
    return xlist

def turnos(turno):
  #Marca el turno de los jugadores sacando el residuo del cuntador turno. Si es non es turno del jugador 1 si es par es el turno del jugador 2
    if (turno % 2) == 1:
        playerTurn = True
    else:
        playerTurn = False
    return playerTurn

def desplegarOculto(xTab):
    for x in range(0,6):
        for y in range(0,6):
            print(f'{xTab[x][y]:>5}', end = "")
        print("")

def desplegarNum(numTab):
    for x in range(0,6):
        for y in range(0,6):
            print(f'{numTab[x][y]:>5}', end = "")
        print("")

def inputval(prompt): 
    correct = False
    while not correct:
        try:
            string = int(input(prompt))
            correct = True
        except:
            print("Entrada invalida, prueba otra vez")
            string = input(prompt)
    return string

def validar(R1,C1,R2,C2,numTab):
    if R1 == R2 and C1 == C2:
        valido = False
    elif ((numTab[R1][C1] in correctos) == True) or ((numTab[R2][C2] in correctos) == True):
        valido = False
    else:
        valido = True
    return valido

numList = crearListanum()
numTab = crearTab()
xTab = crearTabOculto()
turno = 1
player1Points = 0
player2Points = 0
correctos = []

while (len(correctos)) != 36 and True:
      print("Turno ", turno)
      playerTurn = turnos(turno)
      if playerTurn == True:
          print("Es el turno del jugador 1")
          print("    1    2    3    4    5    6    ")
          print("==================================")
      else:
          print("Es el turno del jugador 2")
          print("    1    2    3    4    5    6    ")
          print("==================================")
      while True:
          desplegarOculto(xTab)
          #Las siguientes cuatro lineas de codigo se utilizan para hacer debug. Comentar para quitarlas
          #print()
          #print("    1    2    3    4    5    6    ")
          #print("==================================")
          #desplegarNum(numTab)
          #Debuging ^
          print("Selecciona las coordenadas de las cartas que quieras destapar: ")
          elegR1 = int(inputval("Primera fila: "))
          elegC1 = int(inputval("Primera columna: "))
          elegR2 = int(inputval("Segunda fila: "))
          elegC2 = int(inputval("Segunda columna: "))
          
          R1 = elegR1 - 1
          C1 = elegC1 - 1
          R2 = elegR2 - 1
          C2 = elegC2 - 1
          
          valido = validar(R1,C1,R2,C2,numTab)
          if valido == False:
              print("Input Incorrecto. Vuleve a seleccionar tus cartas")
          else:
              if numTab[R1][C1] == numTab[R2][C2]:
                  correctos.append(numTab[R1][C1])
                  correctos.append(numTab[R2][C2])
                  xTab[R1][C1] = numTab[R1][C1]
                  xTab[R2][C2] = numTab[R2][C2]
                  print("    1    2    3    4    5    6    ")
                  print("==================================")
                  desplegarOculto(xTab)
                  if playerTurn == True:
                      player1Points = player1Points + 1
                      print("     Jugador 1 = ", player1Points, "                 //     ", "            Jugador 2 = ", player2Points)
                      print("           /\                                                 /\ ")
                      print(" _         )( ______________________   ______________________ )(         _")
                      print("(_)///////(**)______________________> <______________________(**)///////(_)")
                      print("           )(                                                 )(")
                      print("           \/                                                 \/")
                  else:
                      player2Points = player2Points + 1
                      print("     Jugador 1 = ", player1Points, "                 //     ", "            Jugador 2 = ", player2Points)
                      print("           /\                                                 /\ ")
                      print(" _         )( ______________________   ______________________ )(         _")
                      print("(_)///////(**)______________________> <______________________(**)///////(_)")
                      print("           )(                                                 )(")
                      print("           \/                                                 \/")
              else:
                  temp1 = xTab[R1][C1]
                  temp2 = xTab[R2][C2]
                  xTab[R1][C1] = numTab[R1][C1]
                  xTab[R2][C2] = numTab[R2][C2]
                  print("    1    2    3    4    5    6    ")
                  print("==================================")
                  desplegarOculto(xTab)
                  xTab[R1][C1] = temp1
                  xTab[R2][C2] = temp2
                  print("No son iguales")
              turno = turno + 1
              break
      seguir = input("Quieres seguir jugando?(Presiona ENTER para continuar // Escribe 'no' para salir): ")
      if seguir == "no":
        if player1Points > player2Points:
            print("FIN DEL JUEGO, VICTORIA: JUGADOR 1")
            print()
            print("     Jugador 1 = ", player1Points, "                 //     ", "            Jugador 2 = ", player2Points)
            print("           /\                                                  /\ ")
            print(" _         )( ______________________     ____¬__   _____=____¬ )(         _")
            print("(_)///////(**)______________________>   /#___~~/  /__¬___#__~~(**)///////(_)")
            print("           )(                                                  )(")
            print("           \/                                                  \/")
        elif player1Points < player2Points:
            print("FIN DEL JUEGO, VICTORIA: JUGADOR 2")
            print()
            print("     Jugador 1 = ", player1Points, "                 //     ", "            Jugador 2 = ", player2Points)
            print("           /\                                                  /\ ")
            print(" _         )( _¬______=_____   _¬___    ______________________ )(         _")
            print("(_)///////(**)~~__#____¬___/  /~~__#\  <______________________(**)///////(_)")
            print("           )(                                                  )(")
            print("           \/                                                  \/")
        else:
            print("FIN DEL JUEGO, EMPATE")
            print(",d88b.d88b,")
            print("888[TIE]888")
            print("`Y8888888Y'")
            print("  `Y888Y'  ")
            print("    `Y'    ")
        
        print("Volvamos a jugar pronto")
        exit()
 
if player1Points > player2Points:
      print("FIN DEL JUEGO, VICTORIA: JUGADOR 1")
      print("     Jugador 1 = ", player1Points, "                 //     ", "            Jugador 2 = ", player2Points)
      print("           /\                                                  /\ ")
      print(" _         )( ______________________     ____¬__   _____=____¬ )(         _")
      print("(_)///////(**)______________________>   /#___~~/  /__¬___#__~~(**)///////(_)")
      print("           )(                                                  )(")
      print("           \/                                                  \/")
elif player1Points < player2Points:
      print("FIN DEL JUEGO, VICTORIA: JUGADOR 2")
      print("     Jugador 1 = ", player1Points, "                 //     ", "            Jugador 2 = ", player2Points)
      print("           /\                                                  /\ ")
      print(" _         )( _¬______=_____   _¬___    ______________________ )(         _")
      print("(_)///////(**)~~__#____¬___/  /~~__#\  <______________________(**)///////(_)")
      print("           )(                                                  )(")
      print("           \/                                                  \/")
else:
      print("FIN DEL JUEGO, EMPATE")
      print(",d88b.d88b,")
      print("888[TIE]888")
      print("`Y8888888Y'")
      print("  `Y888Y'  ")
      print("    `Y'    ")

print("Volvamos a jugar pronto")
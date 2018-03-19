import random

def berechnung():
    summe = 0
    multiplikator = 1
    i = "" #Zahl die später erstellt wird

    for z in range(0, 5): #Zahl wird erstellt
        i = i + str(random.randint(0, 7))

    i_rev = str(i)
    print("Wandle die Oktalzahl in eine Dezimalzahl um: ",i_rev)
    input()

    i_rev = i_rev[::-1] # Zahl wird umgedreht

    for x in range(len(i_rev)):
        summe = summe + int(i_rev[x]) * multiplikator
        multiplikator *= 8

    print("Die Dezimalzahl ist ", i_rev[0], "*1 + ",i_rev[1], "*8 + ",i_rev[2], "*64 + ",i_rev[3], "*512 ",i_rev[4], "*4096 = ", summe)

def oktdez_ui():
       berechnung()

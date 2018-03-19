import random

def berechnung():
    summe = 0
    multiplikator = 1
    i = "" #Zahl die später erstellt wird

    for z in range(0, 5): #Zahl wird erstellt
        i = i + str(random.randint(0, 7))
    i_rev = str(i)
    i_rev = i_rev[::-1] # Zahl wird umgedreht

    for x in range(len(i_rev)):
        summe = summe + int(i_rev[x]) * multiplikator
        multiplikator *= 8

    return i_rev, summe


def oktdez_ui():
    i_rev, summe = berechnung()
    print("Wandle die Oktalzahl in eine Dezimalzahl um: ",i_rev[::-1])
    output = "Die Dezimalzahl ist %s *1 + %s *8 + %s *64 + %s *512 %s *4096 = %s " %(i_rev[0],i_rev[1],i_rev[2],i_rev[3],i_rev[4],summe)
    print(output)

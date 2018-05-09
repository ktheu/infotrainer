############################################################
# IMPORTS
############################################################
import random

############################################################
# GLOBALE VARIABELN
############################################################


############################################################
# FUNKTIONEN
############################################################
def modernerEuklid_ui():
    a, b = getNumbers()
    print('Berechne den Größten gemeinsammen Teiler von', a, 'und', b)
    waitUntillFinished()
    print(modernerEuklid(a, b))

def getNumbers():
    return random.randint(0, 500), random.randint(0, 500)

def waitUntillFinished():
    while True:
        temp = input()
        if temp == '': return

def modernerEuklid(a, b):
    string = ''''''
    while b != 0:
        string += str(a) + ' ' + str(b) + '\n'
        a, b = b, a%b
    string += str(a) + ' ' + str(b) + '\n'
    string += 'Der größte gemeinsamme Teiler ist ' + str(a)
    return string

############################################################
# KLASSEN
############################################################


############################################################
# INIT
############################################################


############################################################
# MAIN
############################################################
if __name__ == '__main__':
    modernerEuklid_ui()

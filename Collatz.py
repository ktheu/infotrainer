from random import randint

def Collatz_ui():
    x=randint(10, 100)
    print("Notiere die Folge der Zahlen, die während des Collatz-Algorithmus berechnet werden und das Ergebnis des Algorithmus für die folgende Eingabe:",x)
    input("Press Enter to continue...")
    z=0
    print("Folge der Zahlen:",end=" ")
    while x!= 1:
        if x%2 == 0:
            x=x//2
        else:
            x=3 * x+1
        print(x,end=" ")
        z=z+1
    print("")
    print("Ergebnis: ",end="")
    print(z)

if __name__ == '__main__':
    Collatz_ui()

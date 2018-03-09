def Collatz_ui():
    x = int(input("Bitte eine Zahl eingeben:" ))
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

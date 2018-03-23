def calculator(a):
    a = int(a)
    b = a
    print(a)
    zahl = ""
    while True:
        rest = a%8
        zahl = zahl + str(rest)
        a = a // 8
        print(a, rest)
        if a == 0:
            break
    print( "Die Oktaldarstellung von ",b," ist ", zahl[::-1])



def dezokt_ui():
    calculator(input("Bitte eine Dezimalzahl eingeben:"))

dezokt_ui()

def calculator(a):
    a = int(a)
    if a<0:
        print("Negative Zahl kann nicht umgewandelt werden!")
        sys.exit("")
    b = a
    print(a)
    zahl = ""
    while True:
        rest = a%2
        zahl = zahl + str(rest)
        a = a // 2
        print(a, rest)
        if a == 0:
            break
    return b, zahl




def dezbin_ui():
    number, result = calculator(input("Bitte eine Dezimalzahl eingeben:"))
    print( "Die Binärdarstellung von ",number," ist ", result[::-1])

import random
def machebinaer():
    s=""
    for i in range(random.randint(8,10)):
        s=s+str(random.randint(0,1))
    return s

def bintodec_calc(x):
    aus=""
    dec=0
    for i in range(len(x)):
        if x[::-1][i]=="1":
            aus=aus+str(2**i)+" + "
    aus=aus[0:-3]
    aus=aus+" = "+ str(int(x, 2))
    return aus
def bintodec_ui():
    x = machebinaer()
    print ("wandle die Binärzahl in eine Dezimalzahl um:", x)
    input()
    print("Die Dezimalzahl ist",bintodec_calc(x))


bintodec_ui()


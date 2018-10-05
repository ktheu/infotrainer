############################################################
# IMPORTS
############################################################
import random
import numpy


############################################################
# FUNKTIONEN
############################################################
def ADT_Liste_ui():
    funktions = ['insert', 'advance', 'reset']
    ausgabe = 'a = Liste()\n'
    crash = False
    lösung = ''
    a = Liste()
    for i in range(random.randint(0, 10)):
        auswahl = numpy.random.choice(['insert', 'advance', 'reset'], p=[0.7, 0.2, 0.1])
        if auswahl == 'insert':
            num = random.randint(1, 9)
            ausgabe += 'a.' + auswahl + '(' + str(num) + ')'
            if not crash:
                a.insert(num)
        elif auswahl == 'advance':
            ausgabe += 'a.' + auswahl + '()'
            if not crash:
                try:
                    a.advance()
                except:
                    lösung = 'Fehler: Liste am Ende'
                    crash = True
        else:
            ausgabe += 'a.' + auswahl + '()'
            if not crash:
                a.reset()
        ausgabe += '\n'
    ausgabe += 'a.reset()\nwhile not a.endpos():\n    print(a.elem(), end=" ")\n    a.advance()'
    print('Was erscheint auf der Konsole?')
    print(ausgabe)
    input()
    if crash:
        print(lösung)
    else:
        a.reset()
        while not a.endpos():
            print(a.elem(), end=' ')
            a.advance()
    print()


############################################################
# KLASSEN
############################################################
class Eintrag():
    def __init__(self):
        self.inhalt = None
        self.next = None


class Liste():
    def __init__(self):
        self.anf = Eintrag()
        self.pos = self.anf

    def empty(self):
        return self.anf.next is None

    def endpos(self):
        return self.pos.next is None

    def reset(self):
        self.pos = self.anf

    def advance(self):
        if self.endpos(): raise RuntimeError('Fehler: Liste am Ende')
        self.pos = self.pos.next

    def elem(self):
        if self.endpos(): raise RuntimeError('Fehler: Liste am Ende')
        return self.pos.next.inhalt

    def insert(self, x):
        hilf = Eintrag()
        hilf.inhalt = x
        hilf.next = self.pos.next
        self.pos.next = hilf

    def delete(self):
        if self.endpos(): raise RuntimeError('Fehler: Liste am Ende')
        self.pos.next = self.pos.next.next


############################################################
# MAIN
############################################################
if __name__ == '__main__':
    ADT_Liste_ui()
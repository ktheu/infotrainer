def Huffman_ui():
    string = input('Eingabe des zu codierenden Strings: ')
    buchstaben = getBuchstaben(string)

    richtig_bshk = getBuchstabenhaefigkeiten(buchstaben)
    input('Buchstabenhäufigkeiten:\n')
    print(richtig_bshk)

    buchstaben_raw = buchstaben[:]
    while len(buchstaben) > 1:
        input('Nächster merge: ')
        richtig_next_merge, buchstaben = nextMerge(buchstaben)
        print(richtig_next_merge)

    buchstaben[0].encoding('')
    buchstaben_raw.sort(key=lambda x: x.code)
    right_encodings = getEncoding(buchstaben_raw)
    input('Codierungen:(links nach rechts)\n')
    print(right_encodings)

    richtig_binaer = getBinaer(string, buchstaben_raw)
    input('Verschlüsseltes Wort?\n')
    print(richtig_binaer)

def getEncoding(b):
    right_encodings = ''
    for each in b:
        right_encodings += each.zeichen + ' = ' + each.code + ', '
    right_encodings = right_encodings[:-2]
    return right_encodings

def getBinaer(string, buchstaben_raw):
    richtig_binaer = ''
    for i in string:
        if i.isalpha():
            for u in buchstaben_raw:
                if i.lower() == u.zeichen:
                    richtig_binaer += u.code
    return richtig_binaer

def getBuchstaben(string):
    buchstaben = []
    for i in string:
        if i.isalpha():
            tempbool = False
            for u in buchstaben:
                if i.lower() == u.zeichen:
                    u.addOne()
                    tempbool = True
            if not tempbool:
                buchstaben.append(Buchstabe(i.lower(), 1))
    return buchstaben

def getBuchstabenhaefigkeiten(buchstaben):
    richtig_bshk = ''
    for i in buchstaben:
        richtig_bshk += i.string
        richtig_bshk += ', '
    richtig_bshk = richtig_bshk[:-2]
    return richtig_bshk

def nextMerge(buchstaben):
    if buchstaben[0].nummer <= buchstaben[1].nummer:
        links = buchstaben[0]
        rechts = buchstaben[1]
    else:
        links = buchstaben[1]
        rechts = buchstaben[0]
    for i in buchstaben:
        if not (i == links or i == rechts):
            if i.nummer < links.nummer:
                rechts = links
                links = i
            elif i.nummer < rechts.nummer:
                rechts = i
    buchstaben.remove(links)
    buchstaben.remove(rechts)
    new_Branch = Branch(links, rechts)
    buchstaben.append(new_Branch)
    richtig_next_merge = links.zeichen + ', ' + rechts.zeichen + ' mit ' + str(links.nummer + rechts.nummer)
    return richtig_next_merge, buchstaben

class Buchstabe():
    def __init__(self, char, nummer):
        self.nummer = nummer
        self.zeichen = char
        self.code = None
        self.string = self.zeichen + ' ' + str(self.nummer)
    def addOne(self):
        self.nummer += 1
        self.string = self.zeichen + ' ' + str(self.nummer)
    def encoding(self, code):
        self.code = code

class Branch():
    def __init__(self, left, right):
        self.nummer = left.nummer + right.nummer
        self.left = left
        self.right = right
        self.zeichen = left.zeichen + right.zeichen
    def encoding(self, previos):
        self.left.encoding(previos + '0')
        self.right.encoding(previos + '1')

if __name__ == '__main__':
    Huffman_ui()

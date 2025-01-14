class Node:
    def __init__(self, saturs, limenis=0, vecaks=None, mazais=None, lielais=None):
        self.info = saturs
        self.parent = vecaks
        self.smaller = mazais
        self.bigger = lielais
        self.level = limenis


    def read(self):
        print(f"dati: {self.info}, līmenis: {self.level}")
        return

class Koks:
    def __init__(self):
        self.sakne = None
        return

    def add(self, jaunais):
        if self.sakne == None:
            self.sakne == Node(jaunais)
            return
        limenis = 1
        vecaks = self.sakne
        if jaunais>vecaks.info:
            vieta = vecaks.bigger
        else:
            vieta = vecaks.smaller
        while vieta:
            limenis +=1
            vecaks = vieta
        if jaunais>vecaks.info:
            vieta = vecaks.bigger = Node(jaunais, vecaks=vecaks, liemnis=limenis)
        else:
            vieta = vecaks.smaller = Node(jaunais, vecaks=vecaks, liemnis=limenis)
        return
    
    def read(self):
        if elements == None:
            elements = self.sakne
        if self.sakne == None:
            print("Kokā nav neviena elementa!")
            return
        
        self.read_ja_ir(elements)
       

    def read_ja_ir(self, elements):
        if elements == None:
            return
        elements.read()
        self.read_ja_ir(elements.smaller)
        self.read_ja_ir(elements.bigger)
        return


koks = Koks()
koks.add(8)
koks.add(4)
koks.add(90)
koks.add(1)
koks.add(7)
koks.add(3)
koks.add(2)
koks.add(5)
koks.read()
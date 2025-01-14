class Node:
    def __init__(self, saturs, vecaks=None, mazais=None, lielais=None):
        self.info = saturs
        self.parent = vecaks
        self.smaller = mazais
        self.bigger = lielais

    def read(self):
        print(self.info)
        return

class Koks:
    def __init__(self):
        self.sakne = None
        return

    def add(self, jaunais):
        if self.sakne == None:
            self.sakne == Node(jaunais)
            return
        vecaks = self.sakne
        if jaunais>vecaks.info:
            vieta = vecaks.bigger
        else:
            vietas = vecaks.smaller
        while vieta:
            vecaks = vieta
        if jaunais>vecaks.info:
            vieta = vecaks.bigger
        else:
            vietas = vecaks.smaller 
        

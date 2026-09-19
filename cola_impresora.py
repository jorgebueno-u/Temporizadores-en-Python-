class ColaImpresora:
    def __init__(self):
        self.cola = []

    def encolar(self, doc):
        self.cola.append(doc)

    def desencolar(self):
        if not self.esta_vacia():
            return self.cola.pop(0)
        return None

    def esta_vacia(self):
        return len(self.cola) == 0
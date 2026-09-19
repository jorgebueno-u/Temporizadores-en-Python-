class PilaRobot:
    def __init__(self):
        self.pila = []

    def apilar(self, tarea):
        self.pila.append(tarea)

    def desapilar(self):
        if not self.esta_vacia():
            return self.pila.pop()
        return None

    def esta_vacia(self):
        return len(self.pila) == 0
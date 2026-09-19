class Documento:
    def __init__(self, nombre, paginas, tiempo):
        self.nombre = nombre
        self.paginas = int(paginas)
        self.tiempo = float(tiempo)
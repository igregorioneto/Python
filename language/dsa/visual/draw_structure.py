# Classe base para estrutura do desenho
class DrawStructure:
    def __init__(self):
        self.elements = []

    def draw(self, screen):
        raise NotImplementedError("Método 'draw' deve ser implementado nas subclasses.")

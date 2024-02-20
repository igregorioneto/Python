class Disciplina:
    def __init__(self, disciplina, aluno, nota):
        self._disciplina = disciplina
        self._aluno = aluno
        self._nota = float(nota)

    @property
    def disciplina(self):
        return self._disciplina
    
    @property
    def aluno(self):
        return self._aluno
    
    @property
    def nota(self):
        return self._nota
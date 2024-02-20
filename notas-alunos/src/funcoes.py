from disciplina import Disciplina

def adicionando_nota(notas,disciplina, aluno, nota):
    notas.append(Disciplina(disciplina=disciplina, aluno=aluno, nota=nota))
    print(f"\nNota adicionada com sucesso!\n")

def media(notas):
    print("\nMédia das notas:")
    soma = 0
    total = len(notas)
    for disciplina in notas:
        if isinstance(disciplina, Disciplina):
            soma += disciplina.nota

    return f"Média total é: {soma / total}\n"

def maior_nota(notas):
    print("\nMaior nota:")
    maior_nota = -1
    aluno_maior_nota = None
    disciplina_maior_nota = None

    for disciplina in notas:
        if isinstance(disciplina, Disciplina):
            if disciplina.nota > maior_nota:
                maior_nota = disciplina.nota
                aluno_maior_nota = disciplina.aluno
                disciplina_maior_nota = disciplina.disciplina

    return f"A maior nota é {maior_nota} do aluno {aluno_maior_nota} da disciplina {disciplina_maior_nota}\n"

def menor_nota(notas):
    print("\nMenor nota:")
    menor_nota = 100
    aluno_menor_nota = None
    disciplina_menor_nota = None

    for disciplina in notas:
        if isinstance(disciplina, Disciplina):
            if disciplina.nota < menor_nota:
                menor_nota = disciplina.nota
                aluno_menor_nota = disciplina.aluno
                disciplina_menor_nota = disciplina.disciplina
    
    return f"A menor nota é {menor_nota} do aluno {aluno_menor_nota} da disciplina {disciplina_menor_nota}\n"

def relatorio(notas):
    print("\nInicio do Relatório: ")
    for disciplina in notas:
        if isinstance(disciplina, Disciplina):
            print(f"[{disciplina.disciplina} - {disciplina.aluno} - {disciplina.nota}]")
    print("Fim do Relatório\n")

def notas_de_uma_disciplina(notas, disciplina):
    print("Inicio do Relatório notas por disciplina: \n")
    for d in notas:
        if isinstance(d, Disciplina):
            if d.disciplina == disciplina:
                print(f"[{disciplina.disciplina} - {disciplina.aluno} - {disciplina.nota}]")

    print("Fim do Relatório\n")
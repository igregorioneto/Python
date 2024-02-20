from funcoes import adicionando_nota, maior_nota, menor_nota, media, notas_de_uma_disciplina, relatorio
from notas import notas_alunos
from verificadores import verificador_de_caracteres, verificador_nota, verificador_quantidade_lista

try:
    while True:
        print("Digite uma opção: ")
        print("1 - Adicionar uma nota")
        print("2 - Média das notas")
        print("3 - Nota mais alta")
        print("4 - Nota mais baixa")
        print("5 - Relatório")
        print("6 - Notas de uma determinada disciplina")
        print("7 - Sair")

        opcao = input()
        if opcao == "1":
            disciplina = input("Digite a disciplina: ")
            if (not verificador_de_caracteres(disciplina, 4)):
                continue;
            aluno = input("Digite o aluno: ")
            if not verificador_de_caracteres(aluno, 4):
                continue;
            nota = float(input("Digite a nota: "))
            if not verificador_nota(nota=nota, min=0):
                continue;
            
            adicionando_nota(notas=notas_alunos, disciplina=disciplina, aluno=aluno, nota=nota)
        elif opcao == "2":
            if not verificador_quantidade_lista(notas_alunos):
                continue;    
            media(notas=notas_alunos)
        elif opcao == "3":
            if not verificador_quantidade_lista(notas_alunos):
                continue; 
            maior_nota(notas=notas_alunos)
        elif opcao == "4":
            if not verificador_quantidade_lista(notas_alunos):
                continue; 
            menor_nota(notas=notas_alunos)
        elif opcao == "5":
            if not verificador_quantidade_lista(notas_alunos):
                continue; 
            relatorio(notas=notas_alunos)
        elif opcao == "6":
            if not verificador_quantidade_lista(notas_alunos):
                continue; 
            notas_de_uma_disciplina(notas=notas_alunos)
        elif opcao == "7":
            break;
        else:
            print("Valor digitado não encontra-se no menu\n")
            continue;

except KeyboardInterrupt:
    print("Interrompeu o processo de input")

finally:
    print("Sistema finalizado...")
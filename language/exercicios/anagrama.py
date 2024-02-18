
def anagrama(word1,word2):
    if len(word1) != len(word2):
        return "Não é um anagrama"
    
    listReverse = list(reversed(word2))
    resultadoReverse = ""
    for e in listReverse:
        resultadoReverse += e
    
    if word1 == resultadoReverse:
        return "É um anagrama"
    else:
        return "Não é um anagrama"
    

def sao_anagramas(word1, word2):
    if len(word1) != len(word2):
        return "Não é anagrama"

    if word1 == word2[::-1]:
        return "É anagrama"
    else:
        return "Não é anagrama"

word1 = input("Digite a primeira palavra: ")
word2 = input("Digite a segunda palavra: ")

print(sao_anagramas(word1, word2))
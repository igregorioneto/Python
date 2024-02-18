
def is_palindromo(word):
    if word == word[::-1]:
        return True
    return False

word = input("Digite uma palavra: ")
if is_palindromo(word):
    print(f"A palavra {word} é um palindromo.")
else:
    print(f"A palavra {word} não é um palindromo.")
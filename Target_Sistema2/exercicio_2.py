def verif_letra(string):
    # converte a string para minusculas para que a contagem seja case insensitive
    string_minuscula = string.lower()
    

    # conta quantas vezes tem 'a' na string
    quantidade = string_minuscula.count('a')
    

    # verifica se a palavra contem 'a' ou nao
    if quantidade > 0:
        print(f"a letra 'a' aparece {quantidade} vezes na string.")

    else:
        print("a letra 'a' nao foi encontrada na string.")


entrada = input("informe uma string: ")
verif_letra(entrada)


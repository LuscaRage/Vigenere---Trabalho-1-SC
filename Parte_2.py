import unicodedata
import string

#Lucas Resende Silveira Reis 180144421

def senha_repetida(senha, mensagem):#Repete a senha para descriptografar
    tamanho_senha = len(senha)
    tamanho_mensagem = len(mensagem)
    j = 0
    senha_gerada = ""

    for i in range(tamanho_mensagem):
        char_mensagem = mensagem[i]
        if char_mensagem.isalpha():
            char_senha = senha[j % tamanho_senha]
            senha_gerada += char_senha.upper() if char_mensagem.isupper() else char_senha.lower()
            j += 1
        else:
            senha_gerada += char_mensagem
    return senha_gerada

def decifra_criptograma(senha, criptograma):#descriptografa um crioptograma cifrado em vigenere com chave
    tamanho_criptograma = len(criptograma)
    senha_gerada = senha_repetida(senha, criptograma)
    mensagem_decifrada = ""

    for i in range(tamanho_criptograma):
        char_cifrado = criptograma[i]
        if char_cifrado.isalpha():
            shift = ord('A') if char_cifrado.isupper() else ord('a')
            char_decifrado = ((ord(char_cifrado) - shift - ord(senha_gerada[i]) + shift + 26) % 26) + shift
            mensagem_decifrada += chr(char_decifrado)
        else:
            mensagem_decifrada += char_cifrado

    return mensagem_decifrada



def tamanho_chave(mensagem_alterada): #Função que encontra o tamanho da chave
    repeticoes = {}
    lenmensagem = len(mensagem_alterada) - 2

    
    for i in range(lenmensagem):# Encontra os grupos de 3 caracteres repetidos e os filtra os que apareceram mais de uma vez
        grupo = mensagem_alterada[i:i + 3]
        if grupo in repeticoes:
            repeticoes[grupo].append(i)
        else:
            repeticoes[grupo] = [i]
    repeticoes = {grupo: distancias for grupo, distancias in repeticoes.items() if len(distancias) > 1}

    soma_tamanhos = 0
    total_tamanhos = 0

    # Calcular os tamanhos dos grupos possíveis e a média ao mesmo tempo
    for grupos, distancias_dos_grupos in repeticoes.items(): # Aqui ele tenta calcular os tamanhos dos grupos possíveis e também calcula a média deles
        for divisor in range(1, 21):
            if all(d % divisor == 0 for d in distancias_dos_grupos):
                tamanho = divisor * len(grupos)
                soma_tamanhos += tamanho
                total_tamanhos += 1

    if total_tamanhos == 0:
        return 0  # Evite divisão por zero
    tamanho_chave = round(soma_tamanhos / total_tamanhos)
    return tamanho_chave

def chave_lingua(frequencias_mensagem, frequencias_lingua, caracter_chave, diferenca_chave): # Tenta achar chave em uma linguagem comparando as frequências do texto com as da linguagem selecionada
    diferenca = 0
    for x, y in zip(frequencias_mensagem, frequencias_lingua):
        diferenca += abs(frequencias_mensagem[x] - frequencias_lingua[y]) #Calcula a diferença entra as frequências de caracters da mensagem e da linguagem
    if diferenca < diferenca_chave or diferenca_chave == -1: #Se diferenca menor que diferenca_chave, ou se for a primeira vez (-1)
        diferenca_chave = diferenca # atualiza o valor da firenca_chave para diferença atual
        caracter_chave = next(iter(frequencias_mensagem))# atribui à variável caracter_chave o próximo caractere no dicionário frequencias_mensagem. Esse caractere é considerado candidato a fazer parte da chave.
    move_dicionario_chave = next(iter(frequencias_mensagem))
    move_dicionario_valor = frequencias_mensagem[next(iter(frequencias_mensagem))]
    frequencias_mensagem.pop(next(iter(frequencias_mensagem)))
    frequencias_mensagem[move_dicionario_chave] = move_dicionario_valor
    return frequencias_mensagem, caracter_chave, diferenca_chave



def encontrar_chave(mensagem, tamanho_chave):
    frequencias_ingles = dict(sorted({
        'E': 12.02, 'T': 9.10, 'A': 8.12, 'O': 7.68, 'I': 7.31, 'N': 6.95,
        'S': 6.28, 'R': 6.02, 'H': 5.92, 'D': 4.32, 'L': 3.98, 'U': 2.88,
        'C': 2.71, 'M': 2.61, 'F': 2.30, 'Y': 2.11, 'W': 2.09, 'G': 2.03,
        'P': 1.82, 'B': 1.49, 'V': 1.11, 'K': 0.69, 'X': 0.17, 'Q': 0.11,
        'J': 0.10, 'Z': 0.07
    }.items()))

    frequencias_portugues = dict(sorted({
        'A': 14.63, 'E': 12.57, 'O': 10.73, 'S': 7.81, 'R': 6.53, 'I': 6.18,
        'N': 5.05, 'M': 4.74, 'U': 4.63, 'T': 4.34, 'L': 4.14, 'D': 3.88,
        'C': 3.10, 'P': 2.80, 'V': 1.67, 'G': 1.30, 'Q': 1.20, 'F': 1.02,
        'H': 0.99, 'B': 0.83, 'Z': 0.47, 'J': 0.40, 'X': 0.21, 'K': 0.02,
        'Y': 0.01, 'W': 0.01
    }.items()))

    chave_portugues = ""
    chave_ingles = ""
    for i in range(tamanho_chave): #calcula a frequência dos caracteres da mensagem
        frequencias_mensagem = {letra: 0 for letra in string.ascii_uppercase}
        total_caracteres = 0
        for caracter in range(i, len(mensagem) - 1, tamanho_chave):
            frequencias_mensagem[mensagem[caracter]] += 1
            total_caracteres += 1

        for letra in frequencias_mensagem:
            frequencias_mensagem[letra] = frequencias_mensagem[letra] * 100 / total_caracteres

        caracter_chave_portugues = ""
        diferenca_chave_portugues = -1
        # Chama a função com as frequências da língua portuguesa
        for i in range(26):
             frequencias_mensagem, caracter_chave_portugues, diferenca_chave_portugues = chave_lingua(frequencias_mensagem, frequencias_portugues, caracter_chave_portugues, diferenca_chave_portugues)

        caracter_chave_ingles = ""
        diferenca_chave_ingles = -1
        # Chama a função com as frequências da língua inglesa
        for i in range(26):
            frequencias_mensagem, caracter_chave_ingles, diferenca_chave_ingles = chave_lingua(frequencias_mensagem, frequencias_ingles, caracter_chave_ingles, diferenca_chave_ingles)
           
        
        chave_portugues = chave_portugues + caracter_chave_portugues
        chave_ingles = chave_ingles + caracter_chave_ingles
    return chave_portugues, chave_ingles



mensagem = input("Digite a mensagem cifrada: ").upper()

# Altera pra ficar mais fácil de processar
mensagem_alterada = ''.join(char for char in mensagem if not unicodedata.combining(char) and char.isalpha())

tamanho_chave = tamanho_chave(mensagem_alterada)
flag = 0
while flag == 0 and tamanho_chave > 0: #Loop para o usuário poder falar se está satisfeito com o resultado, ou se tem que testar novamente
    chave_pt, chave_ig = encontrar_chave(mensagem_alterada, tamanho_chave)
    mensagem_decifrada_pt = decifra_criptograma(chave_pt, mensagem)
    print(f'\nChave texto PT-BR = {chave_pt}\nMensagem PT-BR = {mensagem_decifrada_pt}\n')
    mensagem_decifrada_ig = decifra_criptograma(chave_ig, mensagem)
    print(f'\nChave texto EN = {chave_ig}\nMensagem EN = {mensagem_decifrada_ig }\n')
    escolha = input('\nO resultado foi encontrado? (Digite "D" se não foi encontrado, ou qualquer outra tecla se foi encontrado): ')
    
    if escolha == "D"  or escolha == "d":
        # Caso a chave não seja válida para o usuário, é possível procurar outra chave menor
        tamanho_chave = tamanho_chave - 1
    else:
        flag = 1

if tamanho_chave == 0:
    print('\nNão encontrado\n')

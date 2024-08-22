#Vinicius Borrelli Marcon

# TODO: Perguntar pro prof se na resposta final precisar ser {} ou pode ser []

# Extraíndo o arquivo de texto para uma váriavel  
with open("entradas/input.txt","r") as txt:  #ALTERAR AQUI O CAMINHO PARA TESTAR OUTROS ARQUIVOS.TXT - EM "INPUT.TXT"
    raw_text = [line.strip() for line in txt.readlines()] # Tira quebra de linhas e espaços

numero_operacoes = int(raw_text[0])
operador_extenso = {'U': 'União','I': 'Interseção','D': 'Diferença','C': 'Produto Cartesiano'}

# Função para transformar cada elemento do conjunto em um elemento de lista - e botar nessa lista 
def converter_p_lista(texto):
    return [element.strip() for element in texto.split(",")]


# Extraíndo as operações em: Operador os dois conjuntos da operação (c1 e c2)
def extrator(numero_operacoes):
    i = 1 # Contador
    while numero_operacoes > 0: # Loop para extraír as váriaveis e calcular individualmente até acabar o num de operações
        operador = raw_text[i]
        conj_1 = converter_p_lista(raw_text[i + 1])
        conj_2 = converter_p_lista(raw_text[i + 2])
        i += 3 # Pula pro próximo grupo
        numero_operacoes -= 1
        nome_operador = operador_extenso.get(operador, operador)
        print(f'{nome_operador}: conjunto 1 {conj_1}, conjunto 2 {conj_2}. Resultado: {calcular(operador,conj_1,conj_2)}') # chamando a função de calculo para cada grupo no txt

def calcular(operador,conj_A,conj_B): # Chama a função de solução dependendo do operador
    if operador == 'U':
        return uniao(conj_A,conj_B)
    elif operador =='I':
        return intersecao(conj_A,conj_B)
    elif operador == 'D':
        return diferenca(conj_A,conj_B)
    elif operador == 'C':
        return cartesiano(conj_A,conj_B)

# Funções individuais de calculo para cada tipo de operação
def uniao(conj_A,conj_B):
    conjunto_uniao = conj_A
    for i in conj_B:
        if i not in conj_A:
            conjunto_uniao.append(i)
    return conjunto_uniao

def intersecao(conj_A,conj_B):
    conjunto_intersecao = []
    for i in conj_A:
        if i in conj_B:
            conjunto_intersecao.append(i)
    return conjunto_intersecao

def diferenca(conj_A,conj_B):
    conjunto_diferenca = []
    for i in conj_A:
        if i not in conj_B:
            conjunto_diferenca.append(i)
    return conjunto_diferenca

def cartesiano(conj_A,conj_B):
    conjunto_cartesiano = []
    for i in conj_A:
        for j in conj_B:
            if (((i,j)) not in conjunto_cartesiano):
                conjunto_cartesiano += [(i,j)]
    return conjunto_cartesiano

extrator(numero_operacoes) # Chamada da função que executa o programa por inteiro 
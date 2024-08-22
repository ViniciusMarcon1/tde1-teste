#Vinicius Borrelli Marcon

#Extraíndo o arquivo de texto para uma váriavel   -- ARQUIVO TXT PRECISA SER ATUALIADO DENTRO DO ARQUIVO "INPUT TXT" -- 
with open("input.txt","r") as txt:
    raw_text = [line.strip() for line in txt.readlines()] #Tira quebra de linhas que dava problemas

numero_operacoes = int(raw_text[0])

# Função para transformar cada elemento do conjunto em um elemento de lista - e botar nessa lista 
def converter_p_lista(texto):
    return [element.strip() for element in texto.split(",")]


#Extraíndo as operações em operador e listas (c1 e c2)
def extrator(numero_operacoes):
    i = 1
    while numero_operacoes > 0: #continua extraíndo e calculando até acabar o num de operações 
        operador = raw_text[i]
        conj_1 = converter_p_lista(raw_text[i + 1])
        conj_2 = converter_p_lista(raw_text[i + 2])
        i += 3
        numero_operacoes -= 1
        print(f'{operador}: Conjunto 1 {conj_1}, conjunto 2 {conj_2}. Resultado: {calcular(operador,conj_1,conj_2)}') # chamando a função de calculo para cada grupo no txt

def calcular(operador,conj_A,conj_B): #Chama a função dependendo do operador
    if operador == 'U':
        return uniao(conj_A,conj_B)
    elif operador =='I':
        return intersecao(conj_A,conj_B)
    elif operador == 'D':
        return diferenca(conj_A,conj_B)
    elif operador == 'C':
        return cartesiano(conj_A,conj_B)

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

extrator(numero_operacoes) #Chamada da função que executa o programa
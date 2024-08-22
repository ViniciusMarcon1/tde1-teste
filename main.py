#Vinicius Borrelli Marcon

#OBS: MELHORAR NOME DAS VÁRIAVEIS E FUNÇÕES (PADRONIZAR) 

#Extraíndo o arquivo de texto para uma váriavel   -- ARQUIVO TXT PRECISA SER ATUALIADO DENTRO DO ARQUIVO "INPUT TXT" -- 
with open("input.txt","r") as txt:
    raw_text = [line.strip() for line in txt.readlines()] #Tira quebra de linhas que dava problemas

#Número de operações 
op_numbers = int(raw_text[0])

# Função para transformar cada elemento do conjunto em um elemento de lista - e botar nessa lista 
def convert_to_list(conj_str):
    return [element.strip() for element in conj_str.split(",")]


#Extraíndo as operações em operador e listas (c1 e c2)
def extractor(op_numbers):
    i = 1
    while op_numbers > 0: #continua extraíndo e calculando até acabar o num de operações 
        operator = raw_text[i]
        conj1 = convert_to_list(raw_text[i + 1])
        conj2 = convert_to_list(raw_text[i + 2])
        i += 3
        op_numbers -= 1
        print(f'{operator}: Conjunto 1 {conj1}, conjunto 2 {conj2}. Resultado: {calcular(operator,conj1,conj2)}') # chamando a função de calculo para cada grupo no txt

def calcular(operator,conj_A,conj_B): #Chama a função dependendo do operador
    if operator == 'U':
        return union(conj_A,conj_B)
    elif operator =='I':
        return intersection(conj_A,conj_B)
    elif operator == 'D':
        return diference(conj_A,conj_B)
    elif operator == 'C':
        return cartesian(conj_A,conj_B)

def union(conj_A,conj_B):
    union_conjuto = conj_A
    for i in conj_B:
        if i not in conj_A:
            union_conjuto.append(i)
    return union_conjuto

def intersection(conj_A,conj_B):
    intersection_conjunto = []
    for i in conj_A:
        if i in conj_B:
            intersection_conjunto.append(i)
    return intersection_conjunto

def diference(conj_A,conj_B):
    diference_conjunto = []
    for i in conj_A:
        if i not in conj_B:
            diference_conjunto.append(i)
    return diference_conjunto

def cartesian(conj_A,conj_B):
    cartesian_conjuto = []
    for i in conj_A:
        for j in conj_B:
            if (((i,j)) not in cartesian_conjuto):
                cartesian_conjuto += [(i,j)]
    return cartesian_conjuto

extractor(op_numbers) #Chamada da função que executa o programa
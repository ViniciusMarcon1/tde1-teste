#Vinicius Borrelli Marcon

#OBS: MELHORAR NOME DAS VÁRIAVEIS E FUNÇÕES (PADRONIZAR) 

#Extraíndo o arquivo de texto para uma váriavel 
with open("TDE/input.txt","r") as txt:
    raw_text = [line.strip() for line in txt.readlines()] #Tira quebra de linhas que dava problemas

#Número de ops
op_numbers = int(raw_text[0])

# Função para transformar cada elemento do conjunto em um elemento de lista - e botar nessa lista 
def convert_to_list(conj_str):
    elements = [element.strip() for element in conj_str.split(",")] # Divide a string depois de cada vírgula e remove espaços em branco ao redor
    converted_elements = []
    for element in elements:
        converted_elements.append(element)
    return converted_elements

#Extraíndo as operações em operador e listas (c1 e c2)
def extractor(op_numbers):
    i = 1
    while op_numbers > 0: #Lógica: ele continuar extraíndo e calculando até acabar o num de operações 
        operator = raw_text[i]
        conj1 = convert_to_list(raw_text[i + 1])
        conj2 = convert_to_list(raw_text[i + 2])
        i += 3
        op_numbers -= 1
        #print(f'{operator},\n{conj1},\n{conj2}')
        calcular(operator,conj1,conj2) # chamando a função de calculo para cada grupo no txt

def calcular(operator,conjunto1,conjunto2):
    if operator == 'U':
        union(conjunto1,conjunto2)
    elif operator =='I':
        intersection(conjunto1,conjunto2)
    elif operator == 'D':
        diference(conjunto1,conjunto2)
    elif operator == 'C':
        cartesian(conjunto1,conjunto2)

def union(conjunto1,conjunto2):
    union_conjuto = conjunto1
    for i in conjunto2:
        if i not in conjunto1:
            union_conjuto.append(i)
    return(print(union_conjuto))

def intersection(conjunto1,conjunto2):
    intersection_conjunto = conjunto1
    for i in conjunto1:
        if conjunto1 in conjunto2:
            intersection_conjunto.append(i)
    return(print(intersection_conjunto))


def diference(conjunto1,conjunto2):
    print('a')

def cartesian(conjunto1,conjunto2):
    print('a')

extractor(op_numbers)
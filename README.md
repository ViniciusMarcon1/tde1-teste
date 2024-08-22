# TDE INDIVIDUAL - TRABALHO 1: CONJUNTOS 

## Descrição do projeto
Projeto para calcular o resultado de operações de conjuntos em Python,, dado um input de arquivo txt.

Projeto recebe arquivo txt, passa por um processo de transformação para extraír o conteúdo de acordo com as epecificações e em cima disso faz a 
separação em grupos de conjuto e operadores.

Em seguida, dependendo do tipo de operador os conjuntos passam pelo respectivo calculo e são devolvidos em forma de resposta.

A lógica das funções está especificada dentro de comentários no código "main.py" 

### Como usar 
O projeto aceita um único arquivo txt por vez e ao ser executado realiza todos os cálculos em cima do txt e printa o resultado em uma linha única por operação formatada.

Para executar outros arquivos txt, simplesmente adicionar o arquivo na pasta ENTRADAS dentro do diretório do projeto e alterar o caminho em ("entradas/...") na seguinte linha dentro de "main.py":

- with open("entradas/input.txt","r") as txt:   #Linha 7 

### Autor 
Vinicius Borrelli Marcon 

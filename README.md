# Digital Innovation One - Formações e Bootcamps
Repositório para os desafios de código e de projeto dos bootcamps e formações.

## Bootcamp Geração Tech Unimed-BH - Ciência de Dados
### Desafio de Código: As Duas Torres

Arquivo: duas_torres.py

Saruman, o Branco, um grande mago da Terra-média, traiu os bons costumes e se filiou ao lorde do mal, Sauron. Sauron comanda a torre de Minas Morgul, que abriga um dos seus mais temidos servos, o Rei Bruxo de Angmar, um dos Nazgûl (antigos reis humanos que foram corrompidos pelos poderes dos anéis de Sauron). Saruman comanda a torre de Orthanc, onde cria seus servos Uruk-hai, orcs mais terríveis que os convencionais. Para comunicação, eles utilizam as relíquias esféricas chamadas Palantír, que ficam no topo de suas torres.

A Terra-média avança cada vez mais em tecnologia, muito impulsionada pelas guerras que a acometem diariamente. Um dos problemas que tem atrapalhado sua população é a Interferência de Comunicação Mágica (ICM). Os estudiosos de Minas Tirith, grande cidadela de Gondor, concluíram que para calcular o ICM para Palantír’s, basta dividir a distância entre os dois Palantír’s, pela soma do diâmetro dos mesmos. Gandalf, o Cinza, chegou a questionar essa conclusão, alegando que ela não fazia muito sentido, mas ele mesmo concluiu que dar sentido às coisas não faz sentido.

Saruman e Sauron precisam de uma comunicação estável, pois têm medo que Frodo e seus amigos consigam atrapalhar seus planos, portanto, querem saber quanto de ICM há na comunicação de seus Palantír’s, para que saibam quanto de magia devem empregar na comunicação.

**Entrada**

A entrada é composta por 3 inteiros, **N**(0 < **N** < 10000), **X** e **Y**(0 < **X**, **Y** < 100), que indicam, respectivamente, a distância entre os Palantír, o diâmetro do Palantír de Sauron e o diâmetro do Palantír de Saruman.

**Saída**

Um valor real indicando o ICM da comunicação dos Palatír de Sauron e Saruman, com 2 casas decimais. 

| Exemplos de Entrada | Exemplos de Saída |
| ------------------- | ----------------- |
| 100 2 2             | 25.00             |

| Exemplos de Entrada | Exemplos de Saída |
| ------------------- | ----------------- |
| 200 3 8             | 18.18             |

Fonte: IX Olimpíada Interna de Programação do IFSULDEMINAS - OLIP 2019

### Desafio de Código: Cachorros Quentes

Arquivo: cachorro_quente.py

Em 2012 foi alcançado um novo recorde mundial na famosa Competição de Cachorros-Quentes do Nathan: o campeão, Joey Chestnut, devorou 68 cachorros-quentes em dez minutos, um aumento incrível em relação aos 62 sanduíches devorados pelo mesmo Chestnut em 2011.

O restaurante Nathan’s Famous Corporation, localizado no Brooklyn, NY, é o responsável pela competição. Eles produzem deliciosos cachorros-quentes, mundialmente famosos, mas quando o assunto é matemática eles não são tão bons. Eles desejam ser listados no Livro de Recordes do Guinness, mas para isso devem preencher um formulário descrevendo os fatos básicos da competição. Em particular, eles devem informar o número médio de cachorros-quentes consumidos pelos participantes durante a competição.

Você pode ajudá-los? Eles prometeram pagá-lo com um dos seus saborosos cachorros-quentes. Dados o número total de cachorros-quentes consumidos e o número total de participantes na competição, você deve escrever um programa para determinar o número médio de cachorros-quentes consumidos pelos participantes.

**Entrada**

A entrada consiste de uma única linha que contém dois inteiros **H** e **P** (1 ≤ **H, P** ≤ 1000) indicando respectivamente o número total de cachorros-quentes consumidos e o número total de participantes na competição.

**Saída**

Seu programa deve produzir uma única linha com um número racional representando o número médio de cachorros-quentes consumidos pelos participantes. O resultado deve ser escrito como um número racional com exatamente dois dígitos após o ponto decimal, arredondado se necessário.

| Exemplos de Entrada | Exemplos de Saída |
| ------------------- | ----------------- |
| 10 90               | 0.11              |

| Exemplos de Entrada | Exemplos de Saída |
| ------------------- | ----------------- |
| 840 11              | 76.36             |

| Exemplos de Entrada | Exemplos de Saída |
| ------------------- | ----------------- |
| 1 50                | 0.02              |

| Exemplos de Entrada | Exemplos de Saída |
| ------------------- | ----------------- |
| 34 1000             | 0.03              |

| Exemplos de Entrada | Exemplos de Saída |
| ------------------- | ----------------- |
| 35 1000             | 0.04              |

### Desafio de Código: Cálculo de Viagem

Arquivo: viagem_carro.py

Rubens quer calcular e mostrar a quantidade de litros de combustível gastos em uma viagem de carro, sendo que seu carro faz 12 KM/L. Como ele não sabe fazer um programa que o auxilie nessa missão, ele te pede ajuda. Para efetuar o cálculo, deve-se fornecer o tempo gasto em horas na viagem e a velocidade média durante a mesma em km/h. Assim, você conseguirá passar para Rubens qual a distância percorrida e, em seguida, calcular quantos litros serão necessários para a viagem que ele quer fazer. Mostre o valor com 3 casas decimais após o ponto.

**Entrada**

O arquivo de entrada contém dois inteiros. O primeiro é o tempo gasto na viagem em horas e o segundo é a velocidade média durante a mesma em km/h.

**Saída**

Imprima a quantidade de litros necessária para realizar a viagem, com três dígitos após o ponto decimal

| Exemplo de Entrada | Exemplo de Saída |
| ------------------ | ---------------- |
| 10 85              | 70.833           |

| Exemplo de Entrada | Exemplo de Saída |
| ------------------ | ---------------- |
| 22 67              | 122.833          |

### Desafios Intermediários Py: Alfabeto

Arquivo: alfabeto.py

**Desafio**

Dada a letra N do alfabeto, nos diga qual a sua posição.

**Entrada**

Um único caracter N, uma letra maiúscula ('A'-'Z') do alfabeto (que contém 26 letras).

**Saída**

Um único inteiro, que representa a posição da letra no alfabeto.

| Exemplo de Entrada | Exemplo de Saída |
| ------------------ | ---------------- |
| C                  | 3                |
| J                  | 10               |
| Z                  | 26               |
| A                  | 1                |

### Desafios Intermediários Py: Papagaio Poliglota

Arquivo: papagaioPoliglota.py

**Desafio**

Humberto tem um papagaio muito esperto. Quando está com as duas pernas no chão, o papagaio fala em português. Quando levanta a perna esquerda, fala em inglês. Por fim, quando levanta a direita fala em francês. Nico, amigo de Humberto, ficou fascinado com o animal. Em sua emoção perguntou: “E quando ele levanta as duas?”. Antes que Humberto pudesse responder, o papagaio gritou: “Aí eu caio, idiota!”.

**Entrada**

A entrada consiste de diversos casos de teste. Cada caso de teste consiste uma string informando qual a situação de levantamento de pernas do papagaio.

**Saída**

Para cada condição de levantamento de pernas do papagaio, imprima a linguagem que ele utilizará. Caso ele levante ambas as pernas, imprima “caiu”. Quebre uma linha a cada caso de teste.

| Exemplo de Entrada | Exemplo de Saída |
| ------------------ | ---------------- |
| esquerda           | ingles           |
| direita            | frances          |
| nenhuma            | portugues        |
| ambas              | caiu             |

### Desafios Intermediários Py: Aumento Salarial

Arquivo: aumentoSalarial.py

A empresa que você trabalha resolveu conceder um aumento salarial a todos funcionários, de acordo com a tabela abaixo:

| Salário           | Percentual de Reajuste |
| ----------------- | ---------------------- |
| 0 - 600.00        | 17%                    |
| 600.01 - 900.00   | 13%                    |
| 900.01 - 1500.00  | 12%                    |
| 1500.01 - 2000.00 | 10%                    |
| Acima de 2000.00  | 5%                     |

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

A entrada contém apenas um valor de ponto flutuante, que pode ser maior ou igual a zero, com duas casas decimais, conforme exemplos abaixo.

**Exemplo 1**

| Entrada           | Saída                  |
| ----------------- | ---------------------- |
| 1000              | Novo salario: 1120,00  |
|                   | Reajuste ganho: 120,00 |
|                   | Em percentual: 12 %    |

**Exemplo 2**

| Entrada           | Saída                  |
| ----------------- | ---------------------- |
| 2000              | Novo salario: 2200,00  |
|                   | Reajuste ganho: 200,00 |
|                   | Em percentual: 10 %    |

### Descomplicando a criação de pacotes de processamento de imagens em Python

Pasta: package_template

Projeto de aprendizado de criação de um pacote de processamento de imagens em Python.
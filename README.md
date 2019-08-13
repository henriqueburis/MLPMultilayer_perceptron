# MLP--Multilayer-perceptron
Esse modelo de rede neural em regressão foi construído para prever o preço dos imóveis dada uma nova entrada, não foi realizado 
o tratamento nos dados esse e um outro assunto, o intuito e a construção do modelo de regressão. Regressão valor continuo.
Falamos em regressão quando querendo prever algo a frente não classificar rotular, bom pagador mau pagador ou uma coisa ou outra, exemplo, tipo valor de imóveis, quantidade de chuva etc. Dentro do dado.csv ha X atributos de entrada e y atributo de saída mesmo para regressão temos que ter nosso y 
já que e um aprendizado supervisiona, temos que conhecer a saída do nossos exemplos, então para cada conjunto de  x1,x2...xn temos nosso y, então
logo x1,x2,x3,x4,x5,y1

++ Sobre o dados.csv contem como atributos tando de entrada como de saida 
property_type, state_name, surface_covered_in_m2, rooms, price".

property_type: primeiro atributo, tipo da propriedade, há 4 tipo que existe listarei esse 
são convertido para que o algoritmo entender o relacionamento entra os atributos

state_name: nome dos estados terá que fazer a discretização para achar o nome de cada estado associado a seu número.

surface_covered_in_m2: superfície coberta em metros quadrado já esta no formato ideal para o algoritmo.

rooms: números de quarto.

price: tb já esta no formato certo, esse e nosso atributo alvo que queremos prever, dado os atributo de entrada acima relaciona com a saída assim achando um padrão ou tendência para que o modelo aprenda.

# Executando o Modelo
basta clona o repositório, junto terá o mlp.py python e o dados.csv donde contém as informações que o modelo ira aprender e avaliar.
comando python3 MLP.py

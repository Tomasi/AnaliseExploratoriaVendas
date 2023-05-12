# Análise Exploratória 

Para essa problemática será criada uma massa de dados com dados ficticios com o intuíto de explorar algumas ferramentas de análise.

# Empresa e sua expansão

A empresa FabProdresponsável fabrica e distribui uma família de produtos de limpeza de veículos para região Sul do Brasil. No entanto, CEO dessa empresa não tem conhecimento do quanto a FabProdpode pode expandir a distribuição nessa região e nas demais regiões do Brasil. O CEO têm apenas informações sobre as vendas oriundas do ERP, e está interessado em conhecer melhor as possibilidades de expansão dos negócios para FabProd. Ele sabe que existe uma área multidisciplinar (ciência de dados) que pode ajudá-lo, mas ele não sabe como. 

# Dados Explorados

Dados Oriundos do ERP ([URL do arquivo](https://github.com/Tomasi/AnaliseExploratoriaVendas/blob/master/dados_vendas.xlsx))

# Descrição e Estatística

Olhando para as informações contidas, considerando todos os seus produtos vendidos e distribuídos por região. Podemos entender através desse gráfico de barras o volume de vendas por região.


![graficoBarras](https://github.com/Tomasi/AnaliseExploratoriaVendas/assets/61890715/eb559b49-3f64-49b9-b6c7-5518f1efd3f9)


Os dados explorados possuem data de venda, ou seja, assim podemos comprender e acompanhar a consistência nas vendas.

![GraficoLinha](https://github.com/Tomasi/AnaliseExploratoriaVendas/assets/61890715/c438b52f-e0c1-492d-9b21-8fb9ff1ed7c1)

Começamos a compreender o poder dos dados obtidos, já conseguimos entender o volume de vendas para cada região, assim como a consistência histórica de vendas no perído de 05/01/2019 à 28/12/2022. Complementando nossa análise até o momento, acrescento nosso histograma de vendas, com ele podemos ententer a frequência com que um valor de venda é fechado na negociação.

![histograma](https://github.com/Tomasi/AnaliseExploratoriaVendas/assets/61890715/88d1fa27-71ce-4849-a2b7-f7afecd33cd1)

Complementado nossa visão, com o gráfico de bloxplot podemos compreender qual a proporção dos valores mais negociados em todas as regiões.

![boxplot](https://github.com/Tomasi/AnaliseExploratoriaVendas/assets/61890715/4594abea-f3d8-420d-88cb-4add9a20bf26)

Olhando até o momento, entendemos quais regiões possuem um maior poder de vendas, a frequência dos valores e os preços mais procurados. Agora vamos entender qual a proporção de cada produto nas vendas totais através deste gráfico de pizza.

![GraficoPizza](https://github.com/Tomasi/AnaliseExploratoriaVendas/assets/61890715/4dcd8a02-3a22-4bb8-ab68-c51f72af508d)

# Predição

Nossa base de dados comtempla algumas informações úteis para o entendimento do modelo de negócio, com valores reais de venda por região e produto. No entando para gerar um modelo de predição, ou seja, prever futuras vendas com base em dados históricos, ela acaba não contendo dados suficientes ou não possuindo informações relevantes para tentar predizer um modelo.
Idealmente seria interessantes que ela contesse uma massa maior de dados, com mais detalhes de vendas, tais dados poderiam influenciar na previsão de vendas futuras.  

![GraficoDeDispersao](https://github.com/Tomasi/AnaliseExploratoriaVendas/assets/61890715/ca890f47-a65a-4895-b013-c02acdbeba21)

# Conclusão

Durante nossa análise exploratória e aplicação de um modelo preditivo de regressão linear, pudemos obter algumas informações relevantes sobre as vendas da empresa FabProd e outras afim de entender as oportunidades de vendas.
Iniciamos explorando os dados de vendas por região, analisando medidas de tendência central, como média, mediana e moda, bem como a dispersão dos dados por meio do desvio padrão. Identificamos que a região Sudeste apresentou a maior média de vendas, enquanto a região Norte teve a menor média.


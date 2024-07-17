# Análise de Dados - Relatório Descritivo

## Descrição

Este repositório contém uma análise descritiva de dados de fiscalizações remotas, economia financeira e economia de tempo realizadas por diferentes subsedes. Os dados foram coletados e analisados para entender a distribuição e as tendências relacionadas a essas variáveis.

## Dados
Os dados utilizados nesta análise são:

Número de Fiscalizações Remotas (Numero-fisc-rem): Quantidade de fiscalizações remotas realizadas por cada subsede.
Economia Financeira (Eco-fin): Economia financeira obtida após as ações de fiscalização, em reais (R$).
Economia de Tempo (Eco-tempo-minutos): Economia de tempo alcançada após as ações de fiscalização, em minutos.

## Análise Realizada

Foram realizadas as seguintes etapas de análise:

Descrição Estatística: Cálculo de medidas descritivas como média, mediana, quartis e desvio padrão para cada variável.

## Como Usar

### Para replicar ou utilizar esta análise:

Pré-requisitos:

1. Python 3.x
2. Pandas
3. matplotlib

## Instalação

Clone o repositório:

https://github.com/caio-videmelo/RelatorioFiscRemoto/

### Instale as dependências:

pip install -r requirements.txt
pip install matplotlib
pip install pandas

## Execução

Execute o script Python para reproduzir a análise e visualizações:

python main.py

python graficos.py

## Resultados

### Interpretação dos resultados obtidos

#### Número de Fiscalizações Remotas

O número médio de fiscalizações remotas por Subsedes foi de aproximadamente 3.1, com uma variação de 1 a 6 fiscalizações. Isso indica uma atividade significativa de monitoramento e supervisão em várias regiões. O número mediano de fiscalizações remotas por Subsedes foi de 3, indicando que metade das Subsedes realizaram 3 fiscalizações remotas ou menos.

#### Economia Financeira

A economia financeira média obtida foi de aproximadamente R$ 2.667 por Subsede. No entanto, é importante notar que os valores variaram consideravelmente, com a menor economia registrada sendo R$ 324,46 e a maior alcançando R$ 11.482,34. A mediana da economia financeira obtida foi de aproximadamente R$ 1.294 por Subsede. Isso significa que metade das Subsedes alcançou economias financeiras iguais ou inferiores a esse valor. A mediana é calculada encontrando o valor central dos dados ordenados, o que a torna uma medida robusta em presença de valores extremos.

#### Economia de Tempo

As fiscalizações remotas resultaram em uma economia média de tempo de aproximadamente 9 horas e 39 minutos por Subsede. Os tempos economizados variaram de 1 hora e 30 minutos a 35 horas e 10 minutos, refletindo diferentes níveis de eficiência e impacto das fiscalizações remotas nas diversas Subsedes. As fiscalizações remotas resultaram em uma economia mediana de tempo de aproximadamente 5 horas e 40 minutos economizados em cada região.

![Figure_1](https://github.com/user-attachments/assets/0ad43663-a77d-4918-a59b-8545383d8452)

![Figure_2](https://github.com/user-attachments/assets/9e5bbb6b-8b5b-4bbb-ad83-cf481fe20a58)

![Figure_3](https://github.com/user-attachments/assets/7990a0fc-00d0-4c72-8426-7a7a3ae006db)

#### Análise Descritiva

A análise descritiva dos dados revelou que, em média, as Subsedes realizaram aproximadamente 3 fiscalizações remotas, obtiveram uma economia financeira de R$ 2.667 e economizaram cerca de 9 horas e 39 minutos. Os desvios padrão indicam que os dados estão dispersos em relação às médias, sugerindo variações significativas entre as Subsedes.

#### Considerações Finais

Este relatório destaca os benefícios substanciais das fiscalizações remotas em termos de eficiência operacional e economia de recursos, embora os resultados possam variar consideravelmente entre as diferentes regiões analisadas. Tais insights são fundamentais para aprimorar estratégias de fiscalização e alocação de recursos, visando otimizar os resultados em todas as Subsedes.

## Contribuição

Contribuições são bem-vindas! Se deseja melhorar este projeto, siga estes passos:

1. Fork do projeto
2. Crie uma branch com sua feature (git checkout -b feature/nova-feature)
3. Commit suas mudanças (git commit -am 'Adicionando nova feature')
4. Push para a branch (git push origin feature/nova-feature)
5. Crie um novo Pull Request

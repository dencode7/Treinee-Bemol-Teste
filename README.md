# Análise de Vendas - Loja Bemol

Este projeto apresenta uma análise de dados de vendas da Loja Bemol, utilizando Python e bibliotecas como *pandas* e *numpy*. O objetivo é demonstrar técnicas de manipulação e análise de dados em um conjunto fictício de vendas, exibindo resultados relevantes diretamente no terminal.

---

## Índice

- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Como Executar](#como-executar)
- [Contribuição](#contribuição)
- [Licença](#LICENSE)

---

## Visão Geral

O script realiza diversas análises, como:
- Cálculo do total de vendas por unidade.
- Identificação da unidade com maior faturamento e do produto mais vendido nessa unidade.
- Verificação do vendedor com o maior total de vendas.
- Agrupamento dos dados para obter o faturamento por categoria em cada centro.
- Cálculo do ticket médio, dentre outras análises.

Cada passo é explicado com comentários detalhados no código, facilitando o entendimento e a manutenção.

---

## Funcionalidades

1. **Valor Total de Vendas por Unidade:**  
   Agrupa os dados pela coluna `unidade` e soma os valores da coluna `valor_total`.

2. **Unidade com Maior Venda e Produto Mais Vendido:**  
   Identifica a unidade com o maior total de vendas e, dentro dela, o produto que mais vendeu (com base na quantidade).

3. **Vendedor com Maior Venda:**  
   Agrupa os dados por `cod_vendedor` para encontrar o vendedor com o maior total de vendas.

4. **Faturamento por Categoria em Cada Centro de Vendas:**  
   Exibe o total de vendas para cada combinação de centro e categoria.

5. **Centro com Maior Ticket Médio:**  
   Calcula a média dos valores de venda por centro e identifica aquele com o maior ticket médio.

6. **Unidade com Maior Número de Vendas e Detalhamento:**  
   Determina a unidade com o maior número de registros de vendas e, dentro dela, a categoria e o produto mais vendidos.

7. **Diferença Percentual entre 1º e 2º Produto por Centro:**  
   Para cada centro, calcula a diferença percentual entre o valor do produto mais vendido e o segundo colocado, identificando o centro com a maior diferença.

8. **Percentual de Vendas por Categoria:**  
   Calcula a participação percentual de cada categoria no total de vendas.

9. **Vendedores com Menor Desempenho:**  
   Lista os 5 vendedores com o menor total de vendas.

10. **Média de Produtos Vendidos por Venda em Cada Unidade:**  
    Calcula a média da quantidade de produtos vendidos por venda para cada unidade.

---

## Estrutura do Projeto

├── Daniel_Guimaraes_Trainee_Bemol_Digital.py  # Script principal com as análises
├── base_dados_basico_(2).xlsx                  # Base de dados fictícia de vendas
├── README.md                                   # Documentação do projeto
├── requirements.txt                            # Dependências do projeto
└── LICENSE                                     # Licença do projeto (MIT)


---

## Requisitos

- **Python:** 3.6 ou superior  
- **Bibliotecas:**
  - `pandas`
  - `numpy`
  - `openpyxl` (necessário para leitura de arquivos Excel)

---

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://seu-repositorio-url.git
   cd nome-do-repositorio

## Como Executar

1. Certifique-se de que o arquivo `base_dados_basico_(2).xlsx` está no mesmo diretório do script.
2. Execute o script:

   ```bash
   python Daniel_Guimaraes_Trainee_Bemol_Digital.py

## Contribuição
Contribuições são sempre bem-vindas! Se você deseja melhorar ou adaptar o projeto, siga os passos abaixo:

Faça um fork do projeto.

Crie uma branch para sua feature ou correção:
git checkout -b minha-nova-feature

Realize suas alterações e faça commit:
git commit -m "Descrição da alteração"

Envie sua branch para o repositório remoto:
git push origin minha-nova-feature

Abra um Pull Request descrevendo suas mudanças.

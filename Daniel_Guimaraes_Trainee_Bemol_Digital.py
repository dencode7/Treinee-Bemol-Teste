# Autor: Daniel Guimarães
# Data: 2021-09-30

# Descrição: Script Python para análise de dados de vendas de uma empresa fictícia. O script lê um arquivo Excel com os dados de vendas e executa diversas análises, como:
# - Valor total de vendas por unidade
# - Unidade com maior venda e produto mais vendido nessa unidade
# - Vendedor com maior total de vendas
# - Faturamento por categoria em cada centro de vendas
# - Centro com maior ticket médio (valor médio por venda)
# - Unidade com maior número de vendas e, dentro dela, a categoria e o produto mais vendidos
# - Para cada centro, calcular a diferença percentual entre o 1º e o 2º produto (por valor_total)
# - Percentual de vendas de cada categoria em relação ao total
# - 5 vendedores com menor desempenho (menor total de vendas)
# - Média de produtos vendidos por venda em cada unidade
# O script exibe os resultados na tela.

import pandas as pd
import numpy as np

# 1. Leitura e preparação dos dados
# ---------------------------------------------------------------------
# Lê o arquivo Excel. Certifique-se de que o arquivo "base_dados_basico_(2).xlsx" está no mesmo diretório.
df = pd.read_excel('base_dados_basico_(2).xlsx')

# Exibe os nomes originais das colunas para conferência
print("Colunas originais:", df.columns.tolist())

# Normaliza os nomes: remove espaços, converte para minúsculas e substitui espaços por underlines.
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
print("Colunas normalizadas:", df.columns.tolist())

# Filtra registros inválidos (valor_total <= 0 são descartados)
if 'valor_total' not in df.columns:
    raise KeyError("A coluna 'valor_total' não foi encontrada.")
df = df[df['valor_total'] > 0]

# 2. Análises dos dados
# ---------------------------------------------------------------------

# 2.1 Valor total de vendas por unidade
vendas_unidade = df.groupby('unidade')['valor_total'].sum()
print("\n1. Valor total de vendas por unidade:")
print(vendas_unidade)

# 2.2 Unidade com maior venda e produto mais vendido nessa unidade (usando quantidade 'qtd')
unidade_max = vendas_unidade.idxmax()       # Unidade com maior valor total
venda_max = vendas_unidade.max()              # Valor total nessa unidade
df_unidade = df[df['unidade'] == unidade_max]  # Filtra os dados dessa unidade
produto_max = df_unidade.groupby('produto')['qtd'].sum().idxmax()  # Produto com maior quantidade
print("\n2. Unidade com maior venda:")
print(f"   Unidade: {unidade_max}")
print(f"   Produto mais vendido: {produto_max}")
print(f"   Valor total: R$ {venda_max:.2f}")

# 2.3 Vendedor com maior total de vendas
vendas_vendedor = df.groupby('cod_vendedor')['valor_total'].sum()
vendedor_max = vendas_vendedor.idxmax()
venda_vendedor_max = vendas_vendedor.max()
print("\n3. Vendedor com maior venda:")
print(f"   Vendedor: {vendedor_max}")
print(f"   Total vendido: R$ {venda_vendedor_max:.2f}")

# 2.4 Faturamento por categoria em cada centro de vendas
faturamento = df.groupby(['centro', 'categoria'])['valor_total'].sum()
print("\n4. Faturamento por categoria em cada centro:")
print(faturamento)

# 2.5 Centro com maior ticket médio (valor médio por venda)
ticket_medio = df.groupby('centro')['valor_total'].mean()
centro_ticket = ticket_medio.idxmax()
ticket_valor = ticket_medio.max()
print("\n5. Centro com maior ticket médio:")
print(f"   Centro: {centro_ticket}")
print(f"   Ticket médio: R$ {ticket_valor:.2f}")

# 2.6 Unidade com maior número de vendas e, dentro dela, a categoria e o produto mais vendidos
unidade_mais_vendas = df['unidade'].value_counts().idxmax()
df_unidade_mais = df[df['unidade'] == unidade_mais_vendas]
categoria_max = df_unidade_mais.groupby('categoria')['qtd'].sum().idxmax()
df_categoria = df_unidade_mais[df_unidade_mais['categoria'] == categoria_max]
produto_categoria_max = df_categoria.groupby('produto')['qtd'].sum().idxmax()
quantidade_produto = df_categoria.groupby('produto')['qtd'].sum().max()
print("\n6. Unidade com maior número de vendas:")
print(f"   Unidade: {unidade_mais_vendas}")
print(f"   Categoria mais vendida: {categoria_max}")
print(f"   Produto mais vendido na categoria: {produto_categoria_max}")
print(f"   Quantidade vendida: {quantidade_produto}")

# 2.7 Para cada centro, calcular a diferença percentual entre o 1º e o 2º produto (por valor_total)
def diff_percent(group):
    vendas_prod = group.groupby('produto')['valor_total'].sum().sort_values(ascending=False)
    if len(vendas_prod) < 2:
        return np.nan
    return ((vendas_prod.iloc[0] - vendas_prod.iloc[1]) / vendas_prod.iloc[1]) * 100

diffs = df.groupby('centro').apply(diff_percent)
centro_diff_max = diffs.idxmax()
diff_max = diffs.max()
print("\n7. Centro com maior diferença percentual entre 1º e 2º produto:")
print(f"   Centro: {centro_diff_max}")
print(f"   Diferença percentual: {diff_max:.2f}%")

# 2.8 Percentual de vendas de cada categoria em relação ao total
total_vendas = df['valor_total'].sum()
perc_categoria = (df.groupby('categoria')['valor_total'].sum() / total_vendas) * 100
print("\n8. Percentual de vendas por categoria:")
print(perc_categoria)

# 2.9 5 vendedores com menor desempenho (menor total de vendas)
menores_vendedores = vendas_vendedor.sort_values().head(5)
print("\n9. 5 vendedores com menor desempenho:")
print(menores_vendedores)

# 2.10 Média de produtos vendidos por venda em cada unidade
media_produtos = df.groupby('unidade')['qtd'].mean()
print("\n10. Média de produtos vendidos por venda em cada unidade:")
print(media_produtos)

import pandas as pd

# Criando um dataframe a partir de um dicionário
venda = {'data': ['15/02/2021', '16/02/2021'],
         'valor': [500, 300],
         'produto': ['feijao', 'arroz'],
         'qtde': [50, 70],
        }

# criar uma tabela com o dicionario do python
dicionario_vendas_df = pd.DataFrame(venda)

# Importando arquivo e bases de dados
vendas_df = pd.read_excel('Vendas.xlsx')

# print(vendas_df.head(10))
# print(vendas_df.shape)
# print(vendas_df.describe())

# Uma forma de pegar apenas uma coluna de um dataframe.
# print(pd.Series(vendas_df['Produto']))

# Pegando duas colunas
produtos = vendas_df[['Produto', 'ID Loja']]

# Método loc pega sempre os indices
# Pegar uma linha especifica


# print(vendas_df.loc[1:5])

# Pegar linhas que corresponde a uma condição

# print(vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping'])

vendas_norte_shopping_df = vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping']

vendas_norte_shopping_df = vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping', ['ID Loja', 'Produto', 'Quantidade']]
# print(vendas_norte_shopping_df)

# Pegar uma linha e coluna especifica
# print(vendas_df.loc[1, 'Produto'])

# Adicionar 1 coluna a partir de uma coluna que existe 5%
vendas_df['Comissão'] = vendas_df['Valor Final'] * 0.05
# print(vendas_df)

# Criar uma coluna com valor padrão
vendas_df.loc[:, 'Imposto'] = 0
# print(vendas_df)

vendas_dez_df = pd.read_excel('Vendas-Dez.xlsx')
vendas_dez_df['Comissão'] = vendas_dez_df['Valor Final'] * 0.05
vendas_dez_df.loc[:, 'Imposto'] = 0

vendas_df = pd.concat([vendas_df, vendas_dez_df], ignore_index=True)

vendas_df = vendas_df.drop('Imposto', axis=1)


# Tratar valores vazios
# Deletar linhas e colunas completamente vazias
 
# vendas_df = vendas_df.drop(columns=['Imposto']) # Irá excluir a coluna imposto

#vendas_df = vendas_df.dropna(how='all') # Irá excluir todos as linhas que estão vazia.
#vendas_df = vendas_df.dropna(how='all', axis=1) # Irá excluir todas colunas que estão completamente vazia.

# deletar linhas que possuem pelo menos 1 valor vazio
#vendas_df = vendas_df.dropna() # Exclui todas as linhas que tem pelo menos 1 numero vazio.

# preencher valores vazios
# preencher com a média da coluna

#vendas_df['Comissão'] = vendas_df['Comissão'].fillna(vendas_df['Comissão'].mean()) # fillna irá preencher a coluna comissão que estiver vazia e calcular a media com o metodo mean()


# Preencher com o último valor
# vendas_df = vendas_df.ffill()

# Calcular indicadores
# value_counts()
transacoes_loja = vendas_df['ID Loja'].value_counts()

# groupby
faturamente_produto = vendas_df[['Produto', 'Valor Final']].groupby('Produto').sum(numeric_only=True)

# Mesclar dois dataframes (Procurar informações de um dataframe em outro)
gerentes_df = pd.read_excel('Gerentes.xlsx')

vendas_df = vendas_df.merge(gerentes_df)
print(vendas_df)







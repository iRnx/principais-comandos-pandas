import pandas as pd


table = pd.read_excel('Vendas.xlsx')

total_billing = table['Valor Final'].sum()

# invoicing per store
invoicing_per_store = table[['ID Loja','Valor Final']].groupby('ID Loja').sum()

# billing by product
billing_by_product = table[['ID Loja', 'Produto', 'Valor Final']].groupby(['ID Loja', 'Produto']).sum()

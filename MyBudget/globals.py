import pandas as pd
import os

# Carrega ou cria os DataFrames de despesas e receitas
if ("df_despesas.csv" in os.listdir()) and ("df_receitas.csv" in os.listdir()):
    df_receitas = pd.read_csv("df_receitas.csv", parse_dates=['Data'])
    df_despesas = pd.read_csv("df_despesas.csv", parse_dates=['Data'])
    df_receitas["Data"] = df_receitas["Data"].apply(lambda x: x.date())
    df_despesas["Data"] = df_despesas["Data"].apply(lambda x: x.date())
    
    # Remover a coluna 'Unnamed: 0' se existir (índice salvo incorretamente)
    if 'Unnamed: 0' in df_receitas.columns:
        df_receitas = df_receitas.drop('Unnamed: 0', axis=1)
    if 'Unnamed: 0' in df_despesas.columns:
        df_despesas = df_despesas.drop('Unnamed: 0', axis=1)
        
else:
    # CORREÇÃO: Estrutura de dados na ordem correta: Valor, Efetuado, Fixo, Data, Categoria, Descrição
    data_structure = {
        'Valor': [],
        'Efetuado': [],  # Renomeado de 'Recebido' para 'Efetuado'
        'Fixo': [],
        'Data': [],
        'Categoria': [],
        'Descrição': []
    }
    df_receitas = pd.DataFrame(data_structure)
    df_despesas = pd.DataFrame(data_structure)
    df_receitas.to_csv("df_receitas.csv", index=False)
    df_despesas.to_csv("df_despesas.csv", index=False)

# Carrega ou cria os DataFrames de categorias
if ("df_cat_receitas.csv" in os.listdir()) and ("df_cat_despesas.csv" in os.listdir()):
    df_cat_receita = pd.read_csv("df_cat_receitas.csv", index_col=0)
    df_cat_despesa = pd.read_csv("df_cat_despesas.csv", index_col=0)
    cat_receita = df_cat_receita.values.tolist()
    cat_despesa = df_cat_despesa.values.tolist()
else:
    # Categorias padrão
    cat_receita = ["Salário", "Investimentos", "Comissão"]
    cat_despesa = ["Alimentação", "Aluguel", "Gasolina", "Saúde", "Lazer"]
    
    # Cria DataFrames das categorias
    df_cat_receita = pd.DataFrame({'Categoria': cat_receita})
    df_cat_despesa = pd.DataFrame({'Categoria': cat_despesa})
    
    # Salva os arquivos CSV
    df_cat_receita.to_csv("df_cat_receita.csv")
    df_cat_despesa.to_csv("df_cat_despesas.csv")
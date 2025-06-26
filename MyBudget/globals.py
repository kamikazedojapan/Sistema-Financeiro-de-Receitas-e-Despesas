import pandas as pd
import os

# Carrega ou cria os DataFrames de despesas e receitas
if ("df_despesas.csv" in os.listdir()) and ("df_receitas.csv" in os.listdir()):
    df_despesas = pd.read_csv("df_despesas.csv", index_col=0, parse_dates=True)
    df_receitas = pd.read_csv("df_receitas.csv", index_col=0, parse_dates=True)
else:
    # Estrutura de dados para criar DataFrames vazios
    data_structure = {
        'Valor': [],
        'Fixo': [],
        'Data': [],
        'Categoria': [],
        'Descrição': []
    }
    df_receitas = pd.DataFrame(data_structure)
    df_despesas = pd.DataFrame(data_structure)
    df_receitas.to_csv("df_receitas.csv")
    df_despesas.to_csv("df_despesas.csv")

# Carrega ou cria os DataFrames de categorias
if ("df_cat_receita.csv" in os.listdir()) and ("df_cat_despesas.csv" in os.listdir()):
    df_cat_receita = pd.read_csv("df_cat_receita.csv", index_col=0)
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
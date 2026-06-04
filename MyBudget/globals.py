from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent

ARQ_RECEITAS = BASE_DIR / 'df_receitas.csv'
ARQ_DESPESAS = BASE_DIR / 'df_despesas.csv'
ARQ_CAT_RECEITAS = BASE_DIR / 'df_cat_receitas.csv'
ARQ_CAT_DESPESAS = BASE_DIR / 'df_cat_despesas.csv'

CATEGORIAS_RECEITAS = ['Salário', 'Investimento']
CATEGORIAS_DESPESAS = [
    'alimentação','energia','internet','saúde','transporte',
    'estudo','lazer','quarto','tatuagens','perfurmes',
    'acessorios','desejos','jogos'
]

COLUNAS = ['Valor','Efetuado','Fixo','Data','Categoria','Descrição']

def _criar_movimentacoes(caminho):
    df = pd.DataFrame(columns=COLUNAS)
    df.to_csv(caminho, index=False, encoding='utf-8-sig')
    return df


def _criar_categorias(caminho, categorias):
    df = pd.DataFrame({'Categoria': categorias})
    df.to_csv(caminho, index=False, encoding='utf-8-sig')
    return df


def carregar_dados():
    global df_receitas, df_despesas, df_cat_receita, df_cat_despesa, cat_receita, cat_despesa

    df_receitas = pd.read_csv(ARQ_RECEITAS, encoding='utf-8-sig') if ARQ_RECEITAS.exists() else _criar_movimentacoes(ARQ_RECEITAS)
    df_despesas = pd.read_csv(ARQ_DESPESAS, encoding='utf-8-sig') if ARQ_DESPESAS.exists() else _criar_movimentacoes(ARQ_DESPESAS)

    df_cat_receita = _criar_categorias(ARQ_CAT_RECEITAS, CATEGORIAS_RECEITAS)
    df_cat_despesa = _criar_categorias(ARQ_CAT_DESPESAS, CATEGORIAS_DESPESAS)

    cat_receita = CATEGORIAS_RECEITAS.copy()
    cat_despesa = CATEGORIAS_DESPESAS.copy()

    return df_receitas, df_despesas

carregar_dados()

from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from app import app

layout = dbc.Container([

    html.H3("Regra de Orçamento Mensal"),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dbc.Label("Necessidades (%)"),
            dbc.Input(
                id="input-necessidades",
                type="number",
                value=50,
                min=0,
                max=100,
                step=1,
                class_name="form-control"
            )
        ], xs=12, md=4),

        dbc.Col([
            dbc.Label("Desejos (%)"),
            dbc.Input(
                id="input-desejos",
                type="number",
                value=30,
                min=0,
                max=100,
                step=1,
                className="form-control"
            ),
        ], xs=12, md=4),

        dbc.Col([
            dbc.Label("Investimentos(%)"),
            dcc.Input(
                id="input-investimentos",
                type="number",
                value=20,
                min=0,
                max=100,
                step=1,
                className="form-control"
            )
        ], xs=12, md=4),
    ], className="mb-4"),

    html.Div(id="alerta-regra-orcamento"),

    dbc.Row([

        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Necessidades"),
                    html.H4(id="valor-necessidades")
                ])
            ])
        ], xs=12, md=4),

        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Desejos"),
                    html.H4(id="valor-desejos")
                ])
            ])
        ], xs=12, md=4),

        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Investimentos"),
                    html.H4(id="valor-investimentos")
                ])
            ])
        ], xs=12, md=4),
    ], className="md-4"),

    dcc.Graph(id="grafico-regra-orcamento")
], fluid=True)

@app.callback(
    Output("valor-necessidades", "children"),
    Output("valor-desejos", "children"),
    Output("valor-investimentos", "children"),
    Output("grafico-regra-orcamento", "figure"),
    Output("alerta-regra-orcamento", "children"),
    Input("store-receitas", "data"),
    Input("input-necessidades", "value"),
    Input("input-desejos", "value"),
    Input("input-investimentos", "value")
)
def atualizar_regra_orcamento(receitas, necessidades, desejos, investimentos):

    necessidades = necessidades or 0
    desejos = desejos or 0
    investimentos = investimentos or 0

    soma = necessidades + desejos + investimentos

    if soma != 100:
        fig = px.pie(
            names=["Necessidades", "Desejos", "Investimentos"],
            values=[necessidades, desejos, investimentos],
            title="Distribuição inválida"
        )

        alerta = dbc.Alert(
            "A soma dos percentuais precisa ser exatamente 100%.",
            color="danger"
        )

        return "R$ 0.00", "R$ 0.00", "R$ 0.00", fig, alerta

    df_receitas = pd.DataFrame(receitas)

    if df_receitas.empty or "Valor" not in df_receitas.columns:
        receita_total = 0
    else:
        receita_total = df_receitas["Valor"].sum()

    valor_necessidades = receita_total * (necessidades / 100)
    valor_desejos = receita_total * (desejos / 100)
    valor_investimentos = receita_total * (investimentos / 100)

    df_grafico = pd.DataFrame({
        "Categoria": ["Necessidades", "Desejos", "Investimentos"],
        "Valor": [
            valor_necessidades,
            valor_desejos,
            valor_investimentos
        ]
    })

    fig = px.pie(
        df_grafico,
        names="Categoria",
        values="Valor",
        title="Distribuição do Orçamento Mensal"
    )

    alerta = dbc.Alert(
        f"Regra atual: {necessidades}-{desejos}-{investimentos}",
        color="success"
    )

    return (
        f"R$ {valor_necessidades:.2f}",
        f"R$ {valor_desejos:.2f}",
        f"R$ {valor_investimentos:.2f}",
        fig,
        alerta
    )
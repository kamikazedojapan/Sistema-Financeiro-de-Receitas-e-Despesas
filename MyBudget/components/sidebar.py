import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app

from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd
from globals import *

# ========= Layout ========= #
layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("MyDesktop", className="text-primary"),
            html.Hr(),

            # ====== Avatar ====== #
            html.Img(
                src='/assets/img_hom.png',
                id="avatar_change",
                alt='Avatar',
                className='perfil_avatar',
                style={
                    'width': '200px',
                    'height': 'auto',
                    'border-radius': '50%',
                    'object-fit': 'cover',
                    'display': 'block',
                    'margin': '0 auto'
                }
            ),

            html.Br(),

            # ====== Botões Receita e Despesa ====== #
            dbc.Row([
                dbc.Col(
                    dbc.Button(
                        "+ Receita",
                        color='success',
                        id='open-novo-receita',
                        className='w-100'
                    ),
                    width=6,
                    class_name='pe-3'
                ),
                dbc.Col(
                    dbc.Button(
                        "- Despesa",
                        color='danger',
                        id='open-novo-despesa',
                        className='w-100'
                    ),
                    width=6,
                    class_name='ps-3'
                )
            ], justify='center'),

            html.Br(),

            # Modal Receita
            dbc.Modal([
                dbc.ModalHeader(dbc.ModalTitle('Adicionar receita')),
                dbc.ModalBody([
                    dbc.Row([
                        dbc.Col([
                            dbc.Label('Descrição: '),
                            dbc.Input(placeholder="Ex.: Salário, Fonte de Renda...", id="txt-receita"),
                        ], width=6),
                        dbc.Col([
                            dbc.Label("Valor: "),
                            dbc.Input(placeholder="R$ 100.00", id="valor_receita", value="")
                        ], width=6)
                    ]),

                    dbc.Row([
                        dbc.Col([
                            dbc.Label("Data: "),
                            dcc.DatePickerSingle(id="date-receitas",
                                min_date_allowed=date(2025, 1, 1),
                                max_date_allowed=date(2035, 12, 31),
                                date=datetime.today(),
                                style={"width": "100%"}
                            ),
                        ], width=4),

                        dbc.Col([
                            dbc.Label("Extras"),
                            dbc.Checklist(
                                options=[{"label": "Foi recebida", "value": 1},
                                         {"label": "Receita Recorrente", "value": 2}],
                                value=[1],
                                id='switches-input-receita',
                                switch=True
                            )
                        ], width=4),

                        dbc.Col([
                            html.Label('Categoria da receita'),
                            dbc.Select(id='select_receita', 
                                       options=[{'label': i, 'value': i} for i in cat_receita], 
                                       value=cat_receita[0])
                        ], width=4)
                    ], style={'margin-top': '25px'}),

                    dbc.Row([
                        dbc.Accordion([
                            dbc.AccordionItem(children=[
                                dbc.Row([
                                    dbc.Col([
                                        html.Legend('Adicionar categoria', style={'color': 'green'}),
                                        dbc.Input(type="Text", placeholder="Nova categoria", id="input-add-receita", value=""),
                                        html.Br(),
                                        dbc.Button("Adicionar", class_name="btn btn-success", id="add-category-receita", style={"margin-top": "20px"}),
                                        html.Br(),
                                        html.Div(id="category-div-add-receita", style={}),
                                    ], width=6),

                                    dbc.Col([
                                        html.Legend('Excluir categorias', style={'color': 'red'}),
                                        dbc.Checklist(
                                            id='checklist-selected-style-receita',  # Corrigido o nome
                                            options=[{"label": i, "value": i} for i in cat_receita],
                                            value=[],
                                            label_checked_style={'color': 'red'},
                                            input_checked_style={'backgroundColor': 'blue', 'borderColor': 'orange'},
                                        ),
                                        dbc.Button('Remover', color='warning', id='remove-category-receita', style={'margin-top': '20px'}),
                                    ], width=6)
                                ])
                            ], title='Adicionar/Remover Categorias')
                        ], flush=True, start_collapsed=True, id='accordion-receita')
                    ], style={'margin-top': '25px'}),

                    html.Div(id='id_teste_receita', style={'padding-top': '20px'}),
                ]),
                dbc.ModalFooter([
                    dbc.Button("Adicionar Receita", id='salvar_receita', color='success'),
                    dbc.Popover(dbc.PopoverBody("Receita Salva"), target="salvar_receita", placement="left", trigger="click"),
                ])
            ], style={"background-color": "rgba(17, 140, 79, 0.05)"},
            id="modal-novo-receita",
            size='lg',
            is_open=False,
            centered=True,
            backdrop=True),

            # Modal Despesa
            dbc.Modal([
                dbc.ModalHeader(dbc.ModalTitle('Adicionar despesa')),
                dbc.ModalBody([
                    dbc.Row([
                        dbc.Col([
                            dbc.Label('Descrição: '),
                            dbc.Input(placeholder="Ex.: Supermercado, Combustível...", id="txt-despesa"),
                        ], width=6),
                        dbc.Col([
                            dbc.Label("Valor: "),
                            dbc.Input(placeholder="R$ 100.00", id="valor_despesa", value="")
                        ], width=6)
                    ]),

                    dbc.Row([
                        dbc.Col([
                            dbc.Label("Data: "),
                            dcc.DatePickerSingle(id="date-despesas",
                                min_date_allowed=date(2025, 1, 1),
                                max_date_allowed=date(2035, 12, 31),
                                date=datetime.today(),
                                style={"width": "100%"}
                            ),
                        ], width=4),

                        dbc.Col([
                            dbc.Label("Extras"),
                            dbc.Checklist(
                                options=[{"label": "Foi recebida", "value": 1},
                                         {"label": "Receita Recorrente", "value": 2}],
                                value=[1],
                                id='switches-input-despesa',
                                switch=True
                            )
                        ], width=4),

                        dbc.Col([
                            html.Label('Categoria da despesa'),
                            dbc.Select(id='select_despesa',
                                       options=[{'label': i, 'value': i} for i in cat_despesa], 
                                       value=cat_despesa[0])
                        ], width=4)
                    ], style={'margin-top': '25px'}),

                    dbc.Row([
                        dbc.Accordion([
                            dbc.AccordionItem(children=[
                                dbc.Row([
                                    dbc.Col([
                                        html.Legend('Adicionar categoria', style={'color': 'green'}),
                                        dbc.Input(type="Text", placeholder="Nova categoria", id="input-add-despesa", value=""),
                                        html.Br(),
                                        dbc.Button("Adicionar", class_name="btn btn-success", id="add-category-despesa", style={"margin-top": "20px"}),
                                        html.Br(),
                                        html.Div(id="category-div-add-despesa", style={}),
                                    ], width=6),

                                    dbc.Col([
                                        html.Legend('Excluir categorias', style={'color': 'red'}),
                                        dbc.Checklist(
                                            id='checklist-selected-style-despesa',
                                            options=[{"label": i, "value": i} for i in cat_despesa],
                                            value=[],
                                            label_checked_style={'color': 'red'},
                                            input_checked_style={'backgroundColor': 'blue', 'borderColor': 'orange'},
                                        ),
                                        dbc.Button('Remover', color='warning', id='remove-category-despesa', style={'margin-top': '20px'}),
                                    ], width=6)
                                ])
                            ], title='Adicionar/Remover Categorias')
                        ], flush=True, start_collapsed=True, id='accordion-despesa')
                    ], style={'margin-top': '25px'}),

                    html.Div(id='id_teste_despesa', style={'padding-top': '20px'}),
                ]),
                dbc.ModalFooter([
                    dbc.Button("Adicionar Despesa", id='salvar_despesa', color='danger'),
                    dbc.Popover(dbc.PopoverBody("Despesa Salva"), target="salvar_despesa", placement="left", trigger="click"),
                ])
            ],
            id="modal-novo-despesa",
            size='lg',
            is_open=False,
            centered=True,
            backdrop=True),

            # ====== Navbar (Dashboard e Extratos) ====== #
            html.Hr(),
            dbc.Nav(
                [
                    dbc.NavLink("Dashboard", href="/dashboards", active="exact"),
                    dbc.NavLink("Extratos", href="/extratos", active="exact"),
                ],
                vertical=True,
                pills=True,
                id='nav_buttons',
                style={'margin-bottom': "50px"})

        ], width=12)
    ])
], fluid=True, id='sidebar_completa')

# ========= CALLBACKS ========= #

# Pop-up receita
@app.callback(
    Output('modal-novo-receita', 'is_open'),
    Input('open-novo-receita', 'n_clicks'),
    State('modal-novo-receita', 'is_open')
)
def toggle_modal_receita(n1, is_open):
    if n1:
        return not is_open
    return is_open

# Pop-up despesa
@app.callback(
    Output('modal-novo-despesa', 'is_open'),
    Input('open-novo-despesa', 'n_clicks'),
    State('modal-novo-despesa', 'is_open')
)
def toggle_modal_despesa(n1, is_open):

    if n1:
        return not is_open
    return is_open

@app.callback(
     Output('store-receitas', 'data'),
     Input('salvar_receita', 'n_clicks'),
    [
        State('txt-receita', 'value'),
        State('valor_receita', 'value'),
        State('date-receitas','date'),
        State('switches-input-receita', 'value'),
        State('select_receita', 'value'),
        State('store-receitas', 'data')
    ]
)
def salve_form_receita(n, descricao, valor, date, switches, categoria, dict_receitas):
    df_receitas = pd.DataFrame(dict_receitas)

    if n and not (valor == "" or valor is None):
        print("DEBUG:", descricao, valor, date, switches, categoria)  # <-- Adicione isso para depurar

        valor = round(float(valor), 2)

        # Verificação da data
        if date is None:
            date = datetime.today().date()
        else:
            date = pd.to_datetime(date).date()

        if isinstance(categoria, list):
            categoria = categoria[0] if categoria else "Não Informada"

        efetuado = 1 if switches and 1 in switches else 0
        fixo = 1 if switches and 2 in switches else 0

        nova_linha = {
            "Valor": valor,
            "Efetuado": efetuado,
            "Fixo": fixo,
            "Data": date,
            "Categoria": categoria or "Sem categoria",
            "Descrição": descricao or "Sem descrição"
        }

        df_receitas = pd.concat([df_receitas, pd.DataFrame([nova_linha])], ignore_index=True)
        df_receitas = df_receitas[["Valor", "Efetuado", "Fixo", "Data", "Categoria", "Descrição"]]
        df_receitas.to_csv("df_receitas.csv", index=False)

    return df_receitas.to_dict()
    
@app.callback(
     Output('store-despesas', 'data'),
     Input('salvar_despesa', 'n_clicks'),
    [
        State('txt-despesa', 'value'),
        State('valor_despesa', 'value'),
        State('date-despesas','date'),
        State('switches-input-despesa', 'value'),
        State('select_despesa', 'value'),
        State('store-despesas', 'data')
    ]
)
def salve_form_despesa(n, descricao, valor, date, switches, categoria, dict_despesas):
    df_despesas = pd.DataFrame(dict_despesas)

    if n and not (valor == "" or valor is None):
        print("DEBUG:", descricao, valor, date, switches, categoria)  # <-- Adicione isso para depurar

        valor = round(float(valor), 2)

        # Verificação da data
        if date is None:
            date = datetime.today().date()
        else:
            date = pd.to_datetime(date).date()

        if isinstance(categoria, list):
            categoria = categoria[0] if categoria else "Não Informada"

        efetuado = 1 if switches and 1 in switches else 0
        fixo = 1 if switches and 2 in switches else 0

        nova_linha = {
            "Valor": valor,
            "Efetuado": efetuado,
            "Fixo": fixo,
            "Data": date,
            "Categoria": categoria or "Sem categoria",
            "Descrição": descricao or "Sem descrição"
        }

        df_despesas = pd.concat([df_despesas, pd.DataFrame([nova_linha])], ignore_index=True)
        df_despesas = df_despesas[["Valor", "Efetuado", "Fixo", "Data", "Categoria", "Descrição"]]
        df_despesas.to_csv("df_despesas.csv", index=False)

    return df_despesas.to_dict()

@app.callback(
    [Output("select_receita", "options"),
     Output('checklist-selected-style-receita', 'options'),
     Output('checklist-selected-style-receita', 'value'),
     Output('stored-cat-receitas', 'data')],
    [Input("add-category-receita", "n_clicks"),
     Input('remove-category-receita', "n_clicks")],
    [State("input-add-receita", "value"),
     State("checklist-selected-style-receita", 'value'),
     State('stored-cat-receitas', 'data')]
)
def update_categoria_receita(n_add, n_remove, nova_categoria, categorias_remover, data_atual):
    cat_receita = list(data_atual["Categoria"].values())

    if n_add and nova_categoria and nova_categoria not in cat_receita:
        cat_receita.append(nova_categoria)

    if n_remove and categorias_remover:
        cat_receita = [i for i in cat_receita if i not in categorias_remover]

    opcoes = [{"label": i, "value": i} for i in cat_receita]
    df_cat_receita = pd.DataFrame(cat_receita, columns=["Categoria"])
    df_cat_receita.to_csv("df_cat_receita.csv", index=False)
    return opcoes, opcoes, [], df_cat_receita.to_dict()

@app.callback(
    [Output("select_despesa", "options"),
     Output('checklist-selected-style-despesa', 'options'),
     Output('checklist-selected-style-despesa', 'value'),
     Output('stored-cat-despesas', 'data')],
    [Input("add-category-despesa", "n_clicks"),
     Input('remove-category-despesa', "n_clicks")],
    [State("input-add-despesa", "value"),
     State("checklist-selected-style-despesa", 'value'),
     State('stored-cat-despesas', 'data')]
)
def update_categoria_despesa(n_add, n_remove, nova_categoria, categorias_remover, data_atual):
    cat_despesa = list(data_atual["Categoria"].values())

    if n_add and nova_categoria and nova_categoria not in cat_despesa:
        cat_despesa.append(nova_categoria)

    if n_remove and categorias_remover:
        cat_despesa = [i for i in cat_despesa if i not in categorias_remover]

    opcoes = [{"label": i, "value": i} for i in cat_despesa]
    df_cat_despesa = pd.DataFrame(cat_despesa, columns=["Categoria"])
    df_cat_despesa.to_csv("df_cat_despesa.csv", index=False)
    return opcoes, opcoes, [], df_cat_despesa.to_dict()


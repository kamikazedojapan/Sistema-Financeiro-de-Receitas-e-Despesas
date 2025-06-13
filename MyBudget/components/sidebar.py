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

# ========= Layout ========= #
layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Home Page", className="text-primary text-center"),
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
                    width=6
                ),
                dbc.Col(
                    dbc.Button(
                        "- Despesa",
                        color='danger',
                        id='open-novo-despesa',
                        className='w-100'
                    ),
                    width=6
                )
            ], justify='center'),

            html.Br(),

            # Modal Receita
            dbc.Modal([
                dbc.ModalHeader(dbc.ModalTitle('Adicionar receita')),
                dbc.ModalBody([
                    
                ])
            ], id='modal-novo-receita'),
            dbc.Modal([
                dbc.ModalHeader(dbc.ModalTitle('Adicionar despesa')),
                dbc.ModalBody([
                    
                ])
            ], id='modal-novo-despesa'),

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
def toggle_modal(n1, is_open):
    if n1:
        return not is_open

# Pop-up despesa
@app.callback(
    Output('modal-novo-despesa', 'is_open'),
    Input('open-novo-despesa', 'n_clicks'),
    State('modal-novo-despesa', 'is_open')
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
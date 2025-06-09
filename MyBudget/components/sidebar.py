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
layout = dbc.Col([
    html.H1("Home Page", className="text-primary"),
    html.Hr(),

    # Seção PERFIL----------------
    dbc.Button(
        id='botao_avatar',
        children=[
            html.Img(
                src='/assets/img_hom.png',
                id="avatar_change",
                alt='Avatar',
                className='perfil_name',
                style={
                    'width': '200px',           # tamanho opcional
                    'height': 'auto',
                    'border-radius': '50%',     # se quiser arredondar a imagem
                    'object-fit': 'cover'
                }
            )
        ],
        style={
            'position': 'absolute',
            'top': '100px',
            'left': '40px',
            'background-color': 'transparent',
            'border': 'none',
            'padding': '0'
        }
    )
], style={
    'position': 'relative',
    'height': '100vh',
    'padding': '20px'
})




# =========  Callbacks  =========== #
# Pop-up receita

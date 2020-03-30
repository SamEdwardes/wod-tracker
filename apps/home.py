import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from app import app

##############################################
# Layouts
##############################################

text_welcome = """
    Welcome to WOD Log! The best place to track all of your workouts
"""

##############################################
# Final layout
##############################################
layout = html.Div([
    dbc.Col(html.Div([
        html.Br(),
        html.P(text_welcome)
    ]))
])
import os

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import dash
from dash.dependencies import Input, Output, State



##############################################
# Boilterplate
##############################################
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
app.title = "WOD Log"
app.config.suppress_callback_exceptions = True
server = app.server

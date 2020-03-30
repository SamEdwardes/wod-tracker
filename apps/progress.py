import boto3
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

from app import app
from dash.dependencies import Input, Output
from src.aws import refresh_aws_table
from src.helpers import create_dropdown

##############################################
# Data
##############################################
dynamodb = boto3.resource('dynamodb', region_name='ca-central-1')
wod_log = dynamodb.Table('wod_log')
wod_log_df = refresh_aws_table(wod_log, n=10)[0]


##############################################
# Layouts
##############################################


##############################################
# Final layout
##############################################
layout = html.Div([
    dbc.Col(html.Div([
        html.Br(),
        dbc.Label("Progress"),
        dcc.Graph(id="fig-line-over-time"),
        dbc.Select(id='selected-movement-name', 
                   options=create_dropdown(wod_log_df, 'name')),
        html.Hr(),
        html.P("")
    ]))
])

##############################################
# Callbacks
##############################################

@app.callback(
    Output('fig-line-over-time', 'figure'),
    [Input('selected-movement-name', 'value')]
)
def plot_over_time(selected_name):
    df = refresh_aws_table(wod_log, n=10)[0]
    df = df[df['name']==selected_name]
    print(df)
    fig = px.line(df, x="date", y="weight", color='name',
                  title='Progress over time')
    return fig

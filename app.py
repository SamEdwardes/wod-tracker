import os

import boto3
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd

import dash
from dash.dependencies import Input, Output, State

dynamodb = boto3.resource('dynamodb', region_name='ca-central-1')


##############################################
# Boilterplate
##############################################
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
app.title = "UBC MDS GitHub Search"
port = int(os.environ.get("PORT", 5000))
server = app.server

##############################################
# Data
##############################################
wod_log = dynamodb.Table('wod_log')
wod_log_df = pd.DataFrame(data=wod_log.scan()['Items'])


##############################################
# App layout
##############################################
app.layout = html.Div([
    html.H1("Wod Tracker"),
    html.P("This is my WOD tracking app"),
    dbc.Table.from_dataframe(wod_log_df),
    html.P("Log a new workout"),
    dbc.Input(id='new-date', placeholder="YYYY-MM-DD", type='text'),
    dbc.Input(id='new-name', placeholder="Name of Movement", type='text'),
    dbc.Input(id='new-sets', placeholder="Number of Sets", type='number'),
    dbc.Input(id='new-weight', placeholder="Weight in Pounds", type='number'),
    dbc.Button(id='submit-entry-button',  children="Submit Movement"),
    dbc.Alert(id='submit-status')

])

##############################################
# App Callbacks
##############################################
@app.callback(
    Output("submit-status", "children"), 
    [Input("submit-entry-button", "n_clicks")],
    [State("new-date", "value"),
     State("new-name", "value"),
     State("new-sets", "value"),
     State("new-weight", "value")]
        
)
def on_button_click(n_clicks, date, name, sets, weight):
    current_state = 0
    if n_clicks is None:
        return "No action"
    else:
        wod_log.put_item(
        Item={
            'name': name,
            'date': date,
            'sets': sets,
            'weight': weight
            }
        )
        current_state += 1
        return f"""
            Workout logged!
            Performed {sets} of {name} using {weight} lbs on {date}.
        """

##############################################
# Run
##############################################
if __name__ == '__main__':
    app.run_server(
        debug=True,
        host="0.0.0.0",
        port=port
    )

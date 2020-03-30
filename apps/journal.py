import boto3
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import pandas as pd

from app import app
from src.aws import refresh_aws_table
from src.helpers import clean_text

from apps.journal_new_entry import layout_workout_entry


##############################################
# Data
##############################################
dynamodb = boto3.resource('dynamodb', region_name='ca-central-1')
wod_log = dynamodb.Table('wod_log')

##############################################
# Layouts
##############################################


##############################################
# Final layout
##############################################
layout = html.Div([
    dbc.Col(html.Div([
        html.Br(),
        dbc.Label("History"),
        html.Div(id="wod-log-table"),
        html.Hr(),
        html.P("Log a new workout"),
        layout_workout_entry,
        html.P("")
    ]))
])


##############################################
# App Callbacks
##############################################
@app.callback(
    [Output("submit-status", "children"),
     Output("wod-log-table", "children")], 
    [Input("submit-entry-button", "n_clicks")],
    [State("new-date", "value"),
     State("new-name", "value"),
     State("new-sets", "value"),
     State("new-reps", "value"),
     State("new-weight", "value"),
     State("new-user", "value"),
     State("new-note", "value")])
def submit_new_entry(n_clicks, date, name, sets, reps, weight, user, note):
    if n_clicks is None:
        return (
            "",
            refresh_aws_table(wod_log, n=10)[1]
        )
    else:
        wod_log.put_item(
        Item={
            'name': clean_text(name),
            'date': date,
            'sets': sets,
            'reps': reps,
            'weight': weight,
            'user': clean_text(user),
            'note': clean_text(note)
            }
        )
        return (
             f"Workout logged! Performed {sets} of {name} using {weight} lbs on {date}.",
             refresh_aws_table(wod_log, n=10)[1]
        )
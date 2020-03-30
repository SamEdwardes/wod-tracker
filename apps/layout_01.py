import boto3
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from app import app
from src.aws import refresh_aws_table
from src.helpers import clean_text

##############################################
# Data
##############################################
dynamodb = boto3.resource('dynamodb', region_name='ca-central-1')
wod_log = dynamodb.Table('wod_log')

##############################################
# Layouts
##############################################

layout_01_navbar = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(dbc.NavbarBrand("Wod Log", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            ),
        ),
    ],
    color="primary",
    dark=True,
)

layout_02_workout_entry = dbc.Col([
    # Row 1: User and Date
    dbc.Row(
        [
            dbc.Col(
                dbc.FormGroup(
                    [
                        dbc.Label("User", html_for="new-user"),
                        dbc.Input(
                            type="text",
                            id="new-user",
                            placeholder="Enter name of user (e.g. Sam Edwardes",
                        ),
                    ]
                ),
                width=6,
            ),
            dbc.Col(
                dbc.FormGroup(
                    [
                        dbc.Label("Date", html_for="new-date"),
                        dbc.Input(
                            type="date",
                            id="new-date",
                            placeholder="Enter date",
                        ),
                    ]
                ),
                width=6,
            ),
        ],
        form=True,
    ),
    # Row 2: Exercise
    dbc.Row(
        [
            dbc.Col(
                dbc.FormGroup(
                    [
                        dbc.Label("Name of exercise", html_for="new-name"),
                        dbc.Input(
                            type="text",
                            id="new-name",
                            placeholder="Name of movement (e.g. 'Squat')",
                        ),
                    ]
                )
            )
        ]
    ),
    # Row 3: Sets, reps, weight
    dbc.Row(
        [
            dbc.Col(
                dbc.FormGroup(
                    [
                        dbc.Label("Sets", html_for="new-sets"),
                        dbc.Input(
                            type="number",
                            id="new-sets",
                            placeholder="Enter number of sets (e.g. '3')",
                        ),
                    ]
                ),
                width=4,
            ),
            dbc.Col(
                dbc.FormGroup(
                    [
                        dbc.Label("Reps", html_for="new-reps"),
                        dbc.Input(
                            type="number",
                            id="new-reps",
                            placeholder="Enter the number of reps (e.g. '10'",
                        ),
                    ]
                ),
                width=4,
            ),
            dbc.Col(
                dbc.FormGroup(
                    [
                        dbc.Label("Weight", html_for="new-weight"),
                        dbc.Input(
                            type="number",
                            id="new-weight",
                            placeholder="Enter date",
                        ),
                    ]
                ),
                width=4,
            ),
        ],
        form=True,
    ),
    # Row 4: Submit button
    dbc.Row(dbc.Col([
        dbc.Button(id='submit-entry-button',  children="Submit Movement")

    ])),
    dbc.Row(dbc.Col([
        dbc.Label(id='submit-status')
    ]))
])

##############################################
# Final layout
##############################################
layout = html.Div([
    layout_01_navbar,
    dbc.Col(html.Div([
        html.Br(),
        html.P('''Welcome to WOD Log. A tool for tracking the progress of your
                  workouts'''),
        dbc.Label("History"),
        html.Div(id="wod-log-df"),
        html.Hr(),
        html.P("Log a new workout"),
        layout_02_workout_entry,
        html.P("End of app...")
    ]))
])


##############################################
# App Callbacks
##############################################
@app.callback(
    [Output("submit-status", "children"),
     Output("wod-log-df", "children")], 
    [Input("submit-entry-button", "n_clicks")],
    [State("new-date", "value"),
     State("new-name", "value"),
     State("new-sets", "value"),
     State("new-reps", "value"),
     State("new-weight", "value"),
     State("new-user", "value")])
def submit_new_entry(n_clicks, date, name, sets, reps, weight, user):
    if n_clicks is None:
        return (
            "Press button to submit workout",
            refresh_aws_table(wod_log)[1]
        )
    else:
        wod_log.put_item(
        Item={
            'name': clean_text(name),
            'date': date,
            'sets': sets,
            'reps': reps,
            'weight': weight,
            'user': clean_text(user)
            }
        )
        return (
             f"Workout logged! Performed {sets} of {name} using {weight} lbs on {date}.",
             refresh_aws_table(wod_log)[1]
        )
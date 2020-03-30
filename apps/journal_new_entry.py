import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


layout_workout_entry = dbc.Col([
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
    # Row 4: Note
    dbc.Row(
        [
            dbc.Col(
                dbc.FormGroup(
                    [
                        dbc.Label("Note", html_for="new-note"),
                        dbc.Input(
                            type="text",
                            id="new-note",
                            placeholder="Comments on movement",
                        ),
                    ]
                )
            )
        ]
    ),
    # Row 5: Submit button
    dbc.Row(dbc.Col([
        dbc.Button(id='submit-entry-button',  children="Submit Movement",
                   n_clicks=None)

    ])),
    dbc.Row(dbc.Col([
        dbc.Label(id='submit-status')
    ]))
])
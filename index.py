import os

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from app import app
from apps import home, journal, progress
from dash.dependencies import Input, Output

##############################################
# App Layout
##############################################

nav_bar = dbc.NavbarSimple(
    [
        dbc.NavItem(dbc.NavLink("Journal", href="/apps/journal")),
        dbc.NavItem(dbc.NavLink("Progress", href="/apps/progress"))
    ],
    brand="Wod Log",
    brand_href="/apps/home",
    color="primary",
    dark=True
)
#

app.layout = html.Div([
    nav_bar,
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/journal':
        return journal.layout
    elif pathname == '/apps/progress':
        return progress.layout
    else:
        return home.layout

##############################################
# Run
##############################################
port = int(os.environ.get("PORT", 5000))
if __name__ == '__main__':
    app.run_server(
        debug=True,
        host="0.0.0.0",
        port=port
    )

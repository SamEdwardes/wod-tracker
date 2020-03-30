import os

import dash_core_components as dcc
import dash_html_components as html

from app import app
from dash.dependencies import Input, Output
from apps import layout_01, layout_02

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/layout_01':
        return layout_01.layout
    elif pathname == '/apps/layout_02':
        return layout_02.layout
    else:
        return '404'

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

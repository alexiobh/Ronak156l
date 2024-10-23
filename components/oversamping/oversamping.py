import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from components.oversamping.input import OversampingInput
from components.oversamping.select import SelectOversamping

Oversamping = html.Div([
   dbc.InputGroup(
    id="oversamping-control-components",
    children=[
        SelectOversamping,
        OversampingInput,   
        dbc.Button("oversamping", id="oversamping-btn", color="primary")
    ]),
    html.H5(id="oversamping-message", className="text-warning")
]) 
 
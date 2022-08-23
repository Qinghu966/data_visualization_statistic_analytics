import dash
from dash import dcc
from dash import html

import pandas as pd
import plotly.express as px

from dash.dependencies import Input
from dash.dependencies import Output
from dash.exceptions import PreventUpdate


df = pd.read_csv('dataset/winequality.csv')

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.P("Choose data1:"),
        dcc.Dropdown(
            id="x_axis",
            options=[{"value": x, "label": x} for x in df.keys()],
            clearable=False,
            style={"width": "40%"},
        ),
        html.P("Choose data2:"),
        dcc.Dropdown(
            id="y_axis",
            options=[{"value": x, "label": x} for x in df.keys()],
            clearable=False,
            style={"width": "40%"},
        ),
        html.P("Choose a graph to display:"),
        dcc.Dropdown(
            id="graph",
            options=[
                {"value": "pie", "label": "Pie chart"},
                {"value": "line", "label": "Line chart"},
                {"value": "bar", "label": "Bar chart"},
                {"value": "scatter", "label": "Scatter chart"},
                {"value": "histogram", "label": "histogram chart"},
            ],
            clearable=False,
            style={"width": "40%"},
            # multi=True
        ),
        dcc.Graph(id="my_graph", figure={}),
    ]
)


@app.callback(
    Output("my_graph", "figure"),
    [
        Input("x_axis", "value"),
        Input("y_axis", "value"),
        Input("graph", "value"),
    ],
)
def generate_chart(x_axis, y_axis, graph):
    if not x_axis:
        raise PreventUpdate
    if not y_axis:
        raise PreventUpdate
    if not graph:
        raise PreventUpdate
    dff = df
    if graph == "pie":
        fig = px.pie(dff, values=y_axis, names=x_axis, title="Pie Chart")
    elif graph == "line":
        fig = px.line(dff, x=x_axis, y=y_axis, title="Line Chart")
    elif graph == "bar":
        fig = px.bar(dff, x=x_axis, y=y_axis, title="Bar Chart")
    elif graph == "scatter":
        fig = px.scatter(dff, x=x_axis, y=y_axis, title="Scatter Chart")
    elif graph == "histogram":
        fig = px.histogram(
            dff,
            x=x_axis,
            y=y_axis,
            nbinsx=20,
            nbinsy=20,
            color_continuous_scale="Viridis",
            title="2D Histogram Chart",
        )
    else:
        fig = px.pie(dff, values=y_axis, names=x_axis, title="Pie Chart")

    return fig


app.run_server(debug=True, dev_tools_hot_reload=True)
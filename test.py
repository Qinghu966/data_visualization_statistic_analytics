# -*- coding: utf-8 -*-
import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)




#  PART 1 -   load data (+arrange data)

df = pd.read_csv('dataset/resale-flat-prices-based-on-registration-date-from-jan-2017-onwards.csv')


#  PART 2 - Produces charts

fig = px.line(df, x = 'floor_area_sqm', y = 'resale_price', title='flat resale price (2017)')


#  PART 3 - Create layout

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'line', 'name': u'Montréal'},
                {'x': [1, 2, 3], 'y': [ 3, 5, 7], 'type': 'line', 'name': u'Paris'}
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),
    dcc.Graph(
        id='example',
        figure={
            'data': [
                    {'x': df.flat_model , 'y': df.resale_price, 'type': 'bar', 'name': 'Apple'}
                ],
                'layout': {
                    'title': 'floor model VS resale price'
                }
        }
    ),
    dcc.Graph(
            id='aapl-graph',
            figure={
                'data': [
                    {'x': df.flat_type , 'y': df.resale_price, 'type': 'bar', 'name': 'Apple'}
                ],
                'layout': {
                    'title': 'flat type VS resale price'
                }
            }
        )

    ])


#  PART 4 - Callbacks (later)


# end of part 4

if __name__ == '__main__':
    app.run_server(debug=True)

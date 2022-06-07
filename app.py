# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.




import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#read dataset
df = pd.read_csv('dataset/resale-flat-prices-based-on-registration-date-from-jan-2017-onwards.csv')

#display three different graphs
fig1 = px.histogram(df, x="lease_commence_date", title="The resale flat amount of each lease year")

fig2 = px.scatter(df, x="floor_area_sqm", y="resale_price", title="Floor Area VS Resale Price")

fig3 = px.pie(df, values='resale_price', names='flat_model', title="Flat Model VS Resale Price")

app.layout = html.Div(children=[
    html.H1(children='Flat Resale Graphs'),

    html.Div(children='''
        According to lease date, floor area and flat model
    '''),

    dcc.Graph(
        id='graph1',
        figure=fig1
    )
    ,
    dcc.Graph(
        id='graph2',
        figure=fig2
    )
    ,
    dcc.Graph(
        id='graph3',
        figure=fig3
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)

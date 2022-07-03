from locale import D_FMT
import dash
from dash import dcc, html
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#read dataset
df = pd.read_csv('dataset/winequality.csv')

#less suger(median 3), high quality
fig1 = px.histogram(df, x = "residual sugar", y = "quality", marginal = "box", color = None, hover_data  = df.columns)

#high quality, less suger, PH higher
fig2 = px.density_heatmap(df, x = "pH", y = "quality", z = "residual sugar", color_continuous_scale = "solar", text_auto = True)

#less chlorides, higher quality
fig3 = px.density_heatmap(df, x = "chlorides", y = "quality", text_auto = True, color_continuous_scale = "sunsetdark")

#less suger, PH higher
fig4 = px.scatter(df, x="residual sugar", y = "pH", color='quality', title="Floor Area VS Resale Price")

#high quality, less alcohol
subject = df["quality"]
score = df["alcohol"]
data = [dict(x = subject, y = score, mode = "markers", type = "scatter",
             transforms = [dict(type = "groupby", groups = subject)])]
fig5 = dict(data = data)

#Most of wine PH 3-3.4 sulphates 0.4-0.6 alcohol 9-9.5
fig6 = px.ecdf(df, x = ["pH", "sulphates", "alcohol"], marginal = "histogram", markers = False)

#fig6 = px.ecdf(df, x = "alcohol", log_x = True, log_y = True, color = "quality")

app.layout = html.Div(children=[
    html.H1(children='Wine Quality Analysis'),

    html.Div(children='''
        Based on residual sugar, pH, sulphates, alcohol, chlorides
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
    ,
    dcc.Graph(
        id='graph4',
        figure=fig4
    )
    ,
    dcc.Graph(
        id='graph5',
        figure=fig5
    )
    ,
    dcc.Graph(
        id='graph6',
        figure=fig6
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)

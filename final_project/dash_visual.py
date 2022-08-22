from locale import D_FMT
import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots


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
fig4 = px.scatter(df, x="residual sugar", y = "pH", color='quality', title="residual sugar VS pH")

#high quality, less alcohol
subject = df["quality"]
score = df["alcohol"]
data = [dict(x = subject, y = score, mode = "markers", type = "scatter",
             transforms = [dict(type = "groupby", groups = subject)])]
fig5 = dict(data = data)

#Most of wine PH 3-3.4 sulphates 0.4-0.6 alcohol 9-9.5
fig6 = px.ecdf(df, x = ["pH", "sulphates", "alcohol"], marginal = "histogram", markers = False)

#fig6 = px.ecdf(df, x = "alcohol", log_x = True, log_y = True, color = "quality")

fig7 = px.histogram(df, x="pH")

fig8 = px.scatter(df, x="free sulfur dioxide", y="pH", color="quality")

fig9 = px.box(df, x="quality", y="total sulfur dioxide", color="type", points='all')
fig9.update_traces(quartilemethod="exclusive") 

fig10 = px.histogram(df, x="quality", y="volatile acidity", color="quality", pattern_shape="type")


app.layout = html.Div(children=[
    html.H1(children='Wine Quality Analysis'),
    html.H3(children='Ali Massoud'),
    html.H3(children='Qinghua Ye'),

    html.H4(children="Wine quality distribute on the amount of sugar remaining after fermentation stops"),
    html.Div(children='''
        For most of wine, the amount of sugar are betwwen 1.8 ~ 8.1(greater than 45 grams/liter are considered sweet)
        '''),
    dcc.Graph(
        id='graph1',
        figure=fig1
    ),
    html.H4(children="Correlation between wine quality and pH and residual sugar"),
    html.Div(children='''
        high quality, less sugar, pH higher
        '''),
    dcc.Graph(
        id='graph2',
        figure=fig2
    ),
    html.H4(children="Correlation between wine quality and chlorides"),
    html.Div(children='''
        less chlorides, higher quality
        '''),
    dcc.Graph(
        id='graph3',
        figure=fig3
    ),
    html.H4(children="Correlation between pH and residual sugar based on wine quality"),
    html.Div(children='''
        high quality wine distribute on less suger, PH scale is on 3-4
        '''),
    dcc.Graph(
        id='graph4',
        figure=fig4
    ),
    html.H4(children="Correlation between wine quality and alcohol"),
    html.Div(children='''
        For most of wine,alcohol is between 8-14
        '''),
    dcc.Graph(
        id='graph5',
        figure=fig5
    ),
    html.H4(children="The distribution of pH and sulphates and alcohol"),
    html.Div(children='''
         Most of wine PH 3-3.4 sulphates 0.4-0.6 alcohol 9-9.5
        '''),
    dcc.Graph(
        id='graph6',
        figure=fig6
    ),
    html.H4(children='Plot the distribution of pH level in the wine industry'),
    html.Div(children='''
        It seems to be the wine industry fixates on a certain range for the pH level in the win in order to
        produce good wine. (the range is [2.8, 3.5] for pH)
        '''),
    dcc.Graph(
        id='graph7',
        figure=fig7        
    ),
    html.H4(children="Scatter plot pH in relation with 'free sulfur dioxide' and wine quality"),
    html.Div(children='''
        From the graph, we notice that the more we add free sulfur dioxide (FSX), the more the quality reduces,
        and if we increase FSX, we need to increase the pH level in order to maintain good quality.
        '''),
    dcc.Graph(
    id='graph8',
    figure=fig8
    ),
    html.H4(children="Box plot to show the amount of sulfur dioxide compared to the type of wine (white/red)"),
    html.Div(children='''
        Sulfur dioxide is clearly used in bigger amount in white wine than the red wine.
        '''),
    dcc.Graph(
    id='graph9',
    figure=fig9
    ),
    dcc.Graph(
    id='graph10',
    figure=fig10
    ),
    dcc.Graph(id="graph11"),
    html.Div(children=[
    html.P("Mean:"),
    dcc.Slider(id="mean", min=-3, max=3, value=0, 
               marks={-3: '-3', 3: '3'}),
    html.P("Standard Deviation:"),
    dcc.Slider(id="std", min=1, max=3, value=1, 
               marks={1: '1', 3: '3'}),
    ],style={'width': '100vh', 'height': '25vh'}),

])


@app.callback(
    Output("graph11", "figure"), 
    Input("mean", "value"),
    Input("std", "value"))
def display_color(mean, std):
    # data = np.random.normal(mean, std, size=800) # replace with your own data source
    data = pd.DataFrame()
    data['pH'] = df['pH'].values - (mean/std)
    fig = px.histogram(data, range_x=[-10, 10])
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
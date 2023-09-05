import dash
import pandas as pd
from dash import dcc, html
import plotly.graph_objs as go
import plotly.express as px

app= dash.Dash(__name__)

titanic= pd.read_csv('titanic.csv')

app.layout= html.Div([
    html.H1(children='Titanic Visuals', style={'textAlign': 'center', 'color':"blue"}),

    html.Label('Sex: ') ,
    dcc.Dropdown(id='sex_dropdown', options=titanic.Sex.unique(), value='male'),

    dcc.Graph(id='age_distribution', figure={
        'data': [
            go.Histogram(x= titanic['Age'], nbinsx=30)
        ],
        'layout': go.Layout(
            title='Age Distribution',
            xaxis={'title': 'Age'},
            yaxis={'title': 'Count'},
        )
    })
])

if __name__ == '__main__':
    app.run_server(port=8090)
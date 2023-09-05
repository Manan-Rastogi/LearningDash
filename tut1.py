import dash
from dash import dcc
import dash_html_components as html
import numpy as np
import plotly.graph_objs as go

app = dash.Dash(__name__)

# Setting color from outside: This will help in changing color dynamically
colors = {
    'text': 'red',
    'plot_color': '#bfb9b9',
    'paper_color': '#e8e5e5',
}

np.random.seed(50)
x_rand = np.random.randint(0, 61, 60)
y_rand = np.random.randint(0, 61, 60)


# A default layout
app.layout = html.Div(
    [
        html.H1(children='Hello Dash', style={
                'textAlign': 'center', 'color': colors['text'], 'fontWeight':'bold'}),
        html.Div(children='We are Working here.', style={
                 'textAlign': 'center', 'color': 'blue', 'fontWeight': 'bold'}),

        dcc.Graph(
            id='sample-graph',
            figure={
                'data': [
                   {
                       'x': x_rand,
                       'y': y_rand,
                       'type': 'bar',
                       'name': 'Fc'
                   },
                    # Second bars
                    # {
                    # 'x':[5, 6, 7],
                    # 'y':[22, 25, 16],
                    # 'type':'bar',
                    # 'name': 'SC'
                    # }
                ],
                'layout': {
                    # 'plot_bgcolor': colors['plot_color'],
                    # 'paper_bgcolor': colors['paper_color'],
                    'font':{
                        'color': 'blue',
                    },
                    'title': 'Simple Bar Chart',
                }
            }
        ),

        html.Hr(),

        dcc.Graph(
            id='scatter_plot',
            figure={
                'data': [
                    go.Scatter(x=x_rand, y=y_rand, mode='markers')
                ],
                'layout':go.Layout(
                    title='Scatterplot',
                    xaxis={'title': 'Random X Values'},
                    yaxis={'title': 'Random Y Values'},
                ),
                # 'plot_bgcolor': colors['plot_color'],
                # 'paper_bgcolor': colors['paper_color'],
                'font':{
                    'color': 'blue',
                },
            }
        )

    ]
)


if __name__ == '__main__':
    app.run_server(port=4050)

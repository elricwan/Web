import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

def init_dashboard(server):
    #Create a Plotly Dash dashboard.
    app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp/',
        external_stylesheets=[
            'https://codepen.io/chriddyp/pen/bWLwgP.css'
        ]
    )

    # Load DataFrame
    df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

    fig = px.scatter(df, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60)

    app.layout = html.Div([
        dcc.Graph(
            id='life-exp-vs-gdp',
            figure=fig
        )
    ])
    
    
    return app.server
    
# if __name__ == '__main__':
#     app.run_server(debug=True)
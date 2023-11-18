# https://dash.plotly.com/tutorial
# https://dash-example-index.herokuapp.com/
# https://dash.plotly.com/dash-core-components

# Import packages
import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import requests

# Incorporate data
# df = pd.read_csv('
# https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv
# ')

path = ""
db_file = path + "test.db"
model_file = path + "finalized_model.sav"
host = "http://127.0.0.1:5500"
# host = "http://127.0.0.1:8000"


# data = requests.get("http://127.0.0.1:8000/api/create_data")
# # print(data.json())
# data = requests.get("http://127.0.0.1:8000/api/train_model")
# # print(data.json())
# data = requests.get("http://127.0.0.1:8000/api/score_model_test")
# # print(data.json())
# data = requests.get("http://127.0.0.1:8000/api/score_dataset")
# # print(data.json())
# new_df_dict = data.json()
# df = pd.DataFrame(new_df_dict['data'])
# # print(new_df)
# df.sort_values('pred')
# Initialize the app
app = Dash(__name__)


def pullDataFromAPI():
    data = requests.get(host + "/api/create_data")
    data = requests.get(host + "/api/train_model")
    data = requests.get(host + "/api/score_dataset")
    new_df_dict = data.json()
    df = pd.DataFrame(new_df_dict["data"])
    df.sort_values("pred")
    return df


# to do - add time of call to dash and check data
df2 = pullDataFromAPI()

# App layout
app.layout = html.Div(
    [
        html.Div(children="My First App with Data, Graph, and Controls"),
        html.Hr(),
        # dash_table.DataTable(id='table',
        #                         data=df.to_dict('records'),
        #                         page_size=10),
        # dcc.Graph(figure=px.scatter(df, x='3', y='pred')),
        # updated by button
        html.Button("New Data", id="submit-val", n_clicks=0),
        html.Div(
            className="row",
            children=[
                html.Div(
                    className="six columns",
                    children=[
                        dash_table.DataTable(
                            id="update-table", data=df2.to_dict("records"), page_size=10
                        ),
                    ],
                    style={"width": "49%", "display": "inline-block"},
                ),
                html.Div(
                    className="six columns",
                    children=[
                        dcc.Graph(
                            figure=px.scatter(df2, x="3", y="pred"), id="update-graph"
                        )
                    ],
                    style={"width": "49%", "display": "inline-block"},
                ),
            ],
        )
        # dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id='controls-and-radio-item'),
        # dcc.Graph(figure={}, id='controls-and-graph')
    ]
)


@callback(
    [Output("update-graph", "figure"), Output("update-table", "data")],
    [Input("submit-val", "n_clicks")],
    # State('input-on-submit', 'value'),
    # prevent_initial_call=True
)
def update_output(n_clicks):
    if n_clicks is None:
        return dash.no_update, dash.no_update
    df2 = pullDataFromAPI()
    return px.scatter(df2, x="3", y="pred"), df2.to_dict("records")


# Add controls to build the interaction
# @callback(
#     Output(component_id='controls-and-graph', component_property='figure'),
#     Input(component_id='controls-and-radio-item', component_property='value')
# )
# def update_graph(col_chosen):
#     fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
#     return fig

# Run the app
if __name__ == "__main__":
    app.run(debug=True)

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from google.oauth2 import service_account
import pandas_gbq as pd

font_awesome = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
meta_tags = [{"name": "viewport", "content": "width=device-width"}]
external_stylesheets = [meta_tags, font_awesome]

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)
server = app.server
app.title = 'Solar Power'

app.layout = html.Div([

    html.Div([
        dcc.Interval(id = 'update_date_time_value',
                     interval = 64000,
                     n_intervals = 0),
    ]),

    html.Div([
        html.Div([
            html.Div([
                html.Div(id = 'first_card')
            ], className = 'adjust_card'),
        ], className = 'background1')
    ], className = 'adjust_margin1'),
])


@app.callback(Output('first_card', 'children'),
              [Input('update_date_time_value', 'n_intervals')])
def solar_first_card_value_callback(n_intervals):
    credentials = service_account.Credentials.from_service_account_file('solardata-key.json')
    project_id = 'solardata-360222'
    df_sql = f"""SELECT
    DateTime,
    Voltage,
    ValueCurrent
    FROM `solardata-360222.SolarSensorsData.SensorsData`
    ORDER BY DateTime
    """
    df = pd.read_gbq(df_sql, project_id = project_id, dialect = 'standard', credentials = credentials)
    get_voltage = df['Voltage'].tail(1).iloc[0]
    get_current = df['ValueCurrent'].tail(1).iloc[0]
    power_watt = get_voltage * get_current
    power_kilo_watt = power_watt / 1000

    return [
        html.P('Current Solar Power', className = 'card_text'),
        html.Div([
            html.P('{0:,.5f}'.format(power_kilo_watt) + ' ' + 'KW',
                   className = 'card_value1'),
            html.P('{0:,.5f}'.format(power_watt) + ' ' + 'W',
                   className = 'card_value2')
        ], className = 'card_values_gap'),
        html.Div([
            html.P('Voltage: ' + '{0:,.2f}'.format(get_voltage) + ' ' + 'V',
                   className = 'card_value3'),
            html.P('Current: ' + '{0:,.2f}'.format(get_current) + ' ' + 'A',
                   className = 'card_value4')
        ], className = 'card_value_3_4')
    ]


if __name__ == "__main__":
    app.run_server(debug = True)

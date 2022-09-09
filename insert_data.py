import os
from google.cloud import bigquery
import pandas as pd
import time

while True:
    time.sleep(65)
    header_list = ['DateTime', 'Voltage', 'Current']
    df = pd.read_csv('https://raw.githubusercontent.com/Mubeen31/solar-power-and-weather-data/main/sensors_data.csv',
                     names = header_list)
    data_time = df['DateTime'].tail(1).iloc[0]
    voltage = df['Voltage'].tail(1).iloc[0]
    current = df['Current'].tail(1).iloc[0]

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'solardata-key.json'

    client = bigquery.Client()
    table_id = 'solardata-360222.SolarSensorsData.SensorsData'

    rows_to_insert = [
        {u'DateTime': data_time, u'Voltage': voltage, u'ValueCurrent': current}
    ]

    insert_row = client.insert_rows_json(table_id, rows_to_insert)
    if insert_row == []:
        print('New row have been added.')
    else:
        print(f'Encountered errors while inserting rows: {insert_row}')

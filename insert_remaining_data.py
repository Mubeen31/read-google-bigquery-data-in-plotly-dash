from google.oauth2 import service_account
import pandas as pd1
import pandas_gbq as pd2

# header_list = ['DateTime', 'Voltage', 'ValueCurrent']
df = pd1.read_csv(
    'D:\solar energy monitoring and prediction system\solar power and weather data/sensors_data.csv',
    # names = header_list
)
# df4 = df[(df['DateTime'] >= '2022-10-04 00:13:11') & (df['DateTime'] <= '2022-10-04 11:55:42')][
#     ['DateTime', 'Voltage', 'ValueCurrent']]
credentials = service_account.Credentials.from_service_account_file('data-streaming-key.json')
project_id = 'data-streaming-368616'
table_id = 'data-streaming-368616.DataStreamingSolarData.SolarSensorsData'
df5 = pd2.to_gbq(df,
                 destination_table = table_id,
                 project_id = project_id,
                 credentials = credentials,
                 chunksize = None,
                 if_exists = 'append')

# if df5 == []:
#     print('New rows have been added.')
# else:
#     print(f'Encountered errors while inserting rows: {df5}')

from google.oauth2 import service_account
import pandas as pd1
import pandas_gbq as pd2

header_list = ['DateTime', 'Voltage', 'ValueCurrent']
df = pd1.read_csv(
    'D:\solar energy monitoring and prediction system\solar power and weather data/sensors_data.csv',
    names = header_list)
df4 = df[(df['DateTime'] >= '2022-09-30 08:53:15') & (df['DateTime'] <= '2022-09-30 15:10:10')][
    ['DateTime', 'Voltage', 'ValueCurrent']]
credentials = service_account.Credentials.from_service_account_file('solardata-key.json')
project_id = 'solardata-360222'
table_id = 'solardata-360222.SolarSensorsData.SensorsData'
df5 = pd2.to_gbq(df4,
                 destination_table = table_id,
                 project_id = project_id,
                 credentials = credentials,
                 chunksize = None,
                 if_exists = 'append')

# if df5 == []:
#     print('New rows have been added.')
# else:
#     print(f'Encountered errors while inserting rows: {df5}')

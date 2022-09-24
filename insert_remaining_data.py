from google.oauth2 import service_account
import pandas as pd1
import pandas_gbq as pd2

header_list = ['DateTime', 'Voltage', 'ValueCurrent']
df = pd1.read_csv(
    'D:\solar energy monitoring and prediction system\solar power and weather data/sensors_data.csv',
    names = header_list)
df4 = df[(df['DateTime'] >= '2022-09-23 17:29:48') & (df['DateTime'] <= '2022-09-23 18:27:57')][
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

# if insert_row == []:
#     print('New row have been added.')
# else:
#     print(f'Encountered errors while inserting rows: {insert_row}')

from google.oauth2 import service_account
import pandas as pd1
import pandas_gbq as pd2

# header_list = ['DateTime', 'Voltage', 'ValueCurrent']
df = pd1.read_csv(
    'sensors_data.csv',
    # names = header_list
)
# df4 = df[(df['DateTime'] >= '2022-10-04 00:13:11') & (df['DateTime'] <= '2022-10-04 11:55:42')][
#     ['DateTime', 'Voltage', 'ValueCurrent']]
credentials = service_account.Credentials.from_service_account_file('key.json')
project_id = 'type here project id'
table_id = 'type here table id'
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

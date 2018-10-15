from datetime import datetime

import pandas as pd


def extract_dataframe(file_path):
    dataframe = pd.DataFrame(
        pd.read_csv(file_path, delimiter=';'),
        columns=['Data_Mov', 'Historico', 'Valor', 'Deb_Cred']
    )

    dataframe.rename(
        columns={
            'Data_Mov': 'data',
            'Historico': 'quem',
            'Valor': 'valor',
            'Deb_Cred': 'operacao',
        },
        inplace=True,
    )

    dataframe['data'] = dataframe['data'].apply(format_date)
    dataframe['valor'] = dataframe.apply(format_value, axis=1)
    dataframe['origem'] = 'caixa'

    return dataframe[['data', 'quem', 'origem', 'valor']]


def format_date(date):
    return datetime.strptime(str(date), '%Y%m%d').strftime('%d/%m/%Y')


def format_value(line):
    if line['operacao'] == 'D' and line['valor'] != 0:
        return line['valor'] * -1
    else:
        return line['valor']

from datetime import datetime

import pandas as pd


def extract_dataframe(file_path):
    dataframe = pd.DataFrame(
        pd.read_csv(file_path, encoding='utf-8'),
        columns=[
            'Data',
            'Nome',
            'Status',
            'Líquido',
            'Do endereço de e-mail',
            'Para endereço de e-mail',
        ]
    )

    dataframe = dataframe[dataframe['Status'] != 'Pendente']

    dataframe.rename(
        columns={
            'Data': 'data',
            'Nome': 'quem',
            'Líquido': 'valor',
        },
        inplace=True,
    )

    dataframe['quem'].fillna(dataframe['Do endereço de e-mail'], inplace=True)
    dataframe['quem'].fillna(
        dataframe['Para endereço de e-mail'], inplace=True,
    )
    dataframe['quem'] = dataframe['quem'].apply(format_name)
    dataframe['data'] = dataframe['data'].apply(format_date)
    dataframe['valor'] = dataframe['valor'].apply(format_value)
    dataframe['origem'] = 'paypal'

    return dataframe[['data', 'quem', 'origem', 'valor']]


def format_name(value):
    return str(value).split('@')[0]


def format_date(date):
    return datetime.strptime(str(date), '%d/%m/%Y').strftime('%d/%m/%Y')


def format_value(value):
    return float(value.replace(".", "").replace(",", "."))

from datetime import datetime

import pandas as pd


def extract_dataframe(file_path):
    dataframe = pd.DataFrame(
        pd.read_excel(file_path, sheet_name=0),
        columns=['Data de pagamento', 'Tipo de operação', 'Valor']
    )

    dataframe.rename(
        columns={
            'Data de pagamento': 'data',
            'Tipo de operação': 'quem',
            'Valor': 'valor',
        },
        inplace=True,
    )

    dataframe['data'] = dataframe['data'].apply(format_date)
    dataframe['origem'] = 'mercado pago'

    return dataframe[['data', 'quem', 'origem', 'valor']]


def format_date(date):
    return datetime.strptime(date, '%d/%m/%Y %H:%M').strftime('%d/%m/%Y')

import pandas as pd

def xlsx_to_csv(categories, path):
    """convert files .xlsx to .csv

    Args:
        categories (list): list of categories
        path (string): route of file where .xlsx is located

    Returns:
        .CSV: .csv files
    """
    for category in categories:
        aux_1 = str(path) + '/' + category + '.csv'
        aux_2 = str(path) + '/' + category + '.metadata.xlsx'
        df_aux = pd.read_excel(aux_2)
        df_aux.to_csv(aux_1)
    return

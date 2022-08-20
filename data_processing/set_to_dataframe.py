import pandas as pd

def set_to_dataframe(categories, path):
    """Convert file .CSV to dataframe

    Args:
        categories (array): arrays of categories
        path (string): route of .csv file

    Returns:
        Dataframe: dataframe generated from .csv file
    """
    category_2 = pd.DataFrame()
    for category in categories:
        cat = category
        cat_path = path + '/' + cat + '.csv'   
        category = pd.read_csv(cat_path, sep=',')
        category['CATEGORY'] = cat        
        category_2 = pd.concat([category_2, category], axis = 0)
    category_3 = category_2.reset_index()
    category_3 = category_3.drop(['index', 'Unnamed: 0'], axis=1)
    return category_3

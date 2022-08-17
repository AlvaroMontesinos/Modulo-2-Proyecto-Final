import pandas as pd

def most_repeated_category(dataset):
    """most_repeated_category

    Args:
        dataset (dataframe): dataframe which will be analyzed

    Returns:
        most repeated category
    """
    df_aux = pd.DataFrame(dataset.groupby(['CATEGORY'], as_index=False)['FORMAT'].count())
    cat_max = pd.DataFrame(df_aux.max())
    cat_max = cat_max.reset_index()
    cat_max = cat_max.iloc[0][0]
    return print(cat_max)

def less_repeated_category(dataset):
    """less_repeated_category

    Args:
        dataset (dataframe): dataframe which will be analyzed

    Returns:
        less repeated category
    """
    df_aux = pd.DataFrame(dataset.groupby(['CATEGORY'], as_index=False)['FORMAT'].count())
    cat_min = pd.DataFrame(df_aux.min())
    cat_min = cat_min.reset_index()
    cat_min = cat_min.iloc[0][0]
    return print(cat_min)

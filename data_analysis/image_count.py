import pandas as pd

def image_count(dataset, category):
    """image_count

    Args:
        dataset (dataframe): dataframe where images are identified
        category (string): category which images we want to count
    Returns:
        count of images of category
    """
    df_aux = pd.DataFrame(dataset)
    df_res = df_aux[df_aux.CATEGORY == category].shape[0]
    return df_res

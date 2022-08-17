import pandas as pd

def count_graph_category(dataset):
    """count_graph_image

    Args:
        dataset (dataframe): dataframe which have categories in order to be count

    Returns:
        _type_: graphic with count of categoires
    """
    df_aux = pd.DataFrame(dataset)
    df_aux = pd.DataFrame(df_aux.groupby(['CATEGORY']
                                         , as_index=False)['CATEGORY_ID'].count())
    df_aux.columns = ['CATEGORY', 'CATEGORY_ID']
    graph_res = df_aux.plot.barh(x='CATEGORY', y='CATEGORY_ID'
                                 , rot=0, figsize=(20,5), color = 'blue')
    return graph_res

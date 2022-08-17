import os

def delete_image(dataset, name, file_name_column):
    """delete_image

    Args:
        dataset (dataframe): dataframe in which the image is located
        name (string): name of the image
        file_name_column (string): name of the column of image name

    Returns:
        deleted image
    """
    df_aux = dataset.loc[dataset[file_name_column] == name]
    route_image = df_aux.iloc[0]['ROUTE']
    os.remove(route_image)
    df_2 = dataset.loc[dataset['ROUTE'] != route_image]
    df_2 = df_2.reset_index()
    df_2 = df_2.drop(['index'], axis=1)
    return print('Imagen ' + name +' removida correctamente')

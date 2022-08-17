import os

def rename_image(path, dataset, last_name, new_name, file_name_column):
    """rename_image

    Args:
        path (string): route of file
        dataset (dataframe): name of dataframe in which the image is located
        last_name (string): actual name
        new_name (string): new name
        file_name_column (string): name of the column of image name

    Returns:
        image renamed
    """
    df_aux = dataset.loc[dataset[file_name_column] == last_name]
    last_image = df_aux.iloc[0]['ROUTE']
    cat_image = df_aux.iloc[0]['CATEGORY']
    new_image = path+ '/' + cat_image +"/images/"+ new_name + '.png'
    os.rename(last_image, new_image)
    df_aux.iloc[0].replace(to_replace=last_image, value = new_image)
    return print('Imagen ' + last_name +' cambio su nombre a:' + new_name)

import pandas as pd
from PIL import Image
from tqdm.auto import tqdm

def add_dim_images(dataset, path, file_name_column, subfolder):
    """ Add new columns with the dimenssion of the images

    Args:
        dataset (dataframe): dataframe where images are
        path (string): route of images
        file_name_column (string): name of the column of image name
        subfolder (string): name of folder where images are

    Returns:
        Dataframe: dataframe with height and width added
    """
    dataset = pd.DataFrame(dataset)
    for idx, sample in tqdm(dataset.iterrows(), total=len(dataset)):
        image_name = dataset.at[idx, file_name_column]
        category = dataset.at[idx,"CATEGORY"]
        new_path = path +'/'+category+"/"+subfolder+"/"+image_name+'.png'
        aux_1 = Image.open(new_path)
        aux_2 = str(subfolder)+'_HEIGHT'
        aux_3 = str(subfolder)+'_WIDTH'
        w_aux,h_aux = aux_1.size
        dataset.at[idx,aux_2] = h_aux
        dataset.at[idx,aux_3] = w_aux
    return dataset

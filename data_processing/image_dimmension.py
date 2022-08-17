import pandas as pd
from PIL import Image
from tqdm.auto import tqdm

def add_dim_images(dataset, path, file_name_column):
    """add_dim_images

    Args:
        dataset (dataframe): dataframe where images are
        path (string): route of images
        file_name_column (string): name of the column of image name

    Returns:
        dataframe with height and width added
    """
    dataset = pd.DataFrame(dataset)
    for idx, sample in tqdm(dataset.iterrows(), total=len(dataset)):
        image_name = dataset.at[idx, file_name_column]
        category = dataset.at[idx,"CATEGORY"]
        new_path = path +'/'+category+"/images/"+image_name+'.png'
        aux_1 = Image.open(new_path)
        w_aux,h_aux = aux_1.size
        dataset.at[idx,'IMG_HEIGHT'] = h_aux
        dataset.at[idx,'IMG_WIDTH'] = w_aux
    return dataset

def add_dim_masks(dataset, path, file_name_column):
    """add_dim_images

    Args:
        dataset (dataframe): dataframe where images of masks are
        path (string): route of images
        file_name_column (string): name of the column of image name

    Returns:
        dataframe with height and width added of masks of the images
    """
    dataset = pd.DataFrame(dataset)
    for idx, sample in tqdm(dataset.iterrows(), total=len(dataset)):
        image_name = dataset.at[idx, file_name_column]
        category = dataset.at[idx,"CATEGORY"]
        new_path = path +'/'+category+"/masks/"+image_name+'.png'
        aux_1 = Image.open(new_path)
        w_aux,h_aux = aux_1.size
        dataset.at[idx,'MASK_HEIGHT'] = h_aux
        dataset.at[idx,'MASK_WIDTH'] = w_aux
    return dataset

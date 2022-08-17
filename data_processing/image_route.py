import pandas as pd
from tqdm.auto import tqdm

def add_route(dataset, path, file_name_column):
    """add_route

    Args:
        dataset (dataframe): dataframe whre images are located
        path (string): route where images are located
        file_name_column (string): name of the column of image name

    Returns:
        dataframe with route of images added
    """
    dataset = pd.DataFrame(dataset)
    for idx, sample in tqdm(dataset.iterrows(), total=len(dataset)):
        image_name = dataset.at[idx,file_name_column]
        category = dataset.at[idx,"CATEGORY"]
        new_path = path +'/'+category+"/images/"+image_name+'.png'
        dataset.at[idx,"ROUTE"] = new_path
    return dataset

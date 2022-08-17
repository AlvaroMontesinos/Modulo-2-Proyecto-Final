import os

def create_file(path, categories):
    """create_file

    Args:
        dataset (dataframe): dataframe
        path (string): route of files
        categories (list): list of categories

    Returns:
        folders with images separated by categories
    """
    dirs = {}
    for idx, category in enumerate(categories): 
        os.mkdir('$path/$category')
        dirs[idx] = path+"/"+category
    print("Done! ",path)
    return

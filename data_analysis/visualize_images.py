from matplotlib import pyplot as plt
import pandas as pd
import cv2
import random

def visualize_all(dataset, columns, categories):
    """visualize_all

    Args:
        dataset (dataframe): dataframe in which images are located
        columns (int): number of columns
        categories (array): array of categories
    Returns:
        array of random images separated by category
    """
    dataset = pd.DataFrame(dataset)
    len_cat = len(dataset["CATEGORY"].unique())
    plt.rcParams["figure.figsize"] = (15,8) 
    images = []    
    num_images = 3
    cat = dataset["CATEGORY"].unique()

    for classes in cat:
        vars()[classes] = pd.DataFrame(dataset[dataset['CATEGORY'] == classes]).reset_index()

        for num in range(num_images):
            aux_1 = vars()[classes]

            random_image = random.randint(0,len(aux_1)-1)
            images.append([aux_1.at[random_image,"ROUTE"]
                           ,categories[aux_1.at[random_image,"CATEGORY_ID"]]])

    for index, sample in enumerate(images):
        img = cv2.imread(sample[0])
        plt.subplot(len_cat, columns, index+1), plt.imshow(img)
        plt.title(sample[1])
        plt.xticks([]), plt.yticks([])

def visualize_img_category(dataset, category):
    """visualize_img_category

    Args:
        dataset (dataframe): dataframe in which image are located
        category (string): category of image which will be showed
    Returns:
        random image defined by category
    """
    dataset = pd.DataFrame(dataset)
    df_aux = dataset.loc[dataset['CATEGORY'] == category]
    df_aux = df_aux.reset_index()
    random_image = random.randint(0,len(df_aux)-2)
    var = df_aux.at[random_image,"ROUTE"]
    plt.rcParams["figure.figsize"] = (15,8)
    img = cv2.imread(var)
    plt.imshow(img)
    plt.title(category)

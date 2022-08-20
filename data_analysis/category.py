import pandas as pd
import cv2
import random
from matplotlib import pyplot as plt


class Category:
    """atributes and function of category
    """
    def __init__(self, name, dataset):
        self.name = name
        self.dataset = dataset

    def image_count(self):
        """Count of images

        Returns:
            String: count of images of category
        """
        df_aux = pd.DataFrame(self.dataset)
        df_res = df_aux[df_aux.CATEGORY == self.name].shape[0]
        return df_res

    def visualize_img_category(self):
        """ Visualization or random image of the category

        Returns:
            Image: random image defined by category
        """
        dataset = pd.DataFrame(self.dataset)
        df_aux = dataset.loc[dataset['CATEGORY'] == self.name]
        df_aux = df_aux.reset_index()
        random_image = random.randint(0,len(df_aux)-2)
        var = df_aux.at[random_image,"ROUTE"]
        plt.rcParams["figure.figsize"] = (15,8)
        img = cv2.imread(var)
        #plt.imshow(img)
        #plt.title(self.name)
        cv2.imshow(self.name,img)
        cv2.waitKey(0)
        
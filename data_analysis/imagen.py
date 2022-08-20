import os
import cv2
import pandas as pd
from matplotlib import pyplot as plt

class Imagen:
    """Atributes and functions of images which are in a dataset
    """
    def __init__(self, name, path, dataset, file_name_column, subfolder):
        self.name = name
        self.path = path
        self.dataset = dataset
        self.file_name_column = file_name_column
        self.subfolder = subfolder
        self.height()
        self.width()
        self.category_image()

    def height(self):
        """Hight of image

        Returns:
            String: Hight of image
        """
        df_aux = self.dataset.loc[
            self.dataset[self.file_name_column] == self.name]
        var_aux = str(self.subfolder)+'_HEIGHT'
        res_aux = df_aux.iloc[0][var_aux]
        return res_aux

    def width(self):
        """Width of image

        Returns:
            String: Width of image
        """
        df_aux = self.dataset.loc[
            self.dataset[self.file_name_column] == self.name]
        var_aux = str(self.subfolder)+'_WIDTH'
        res_aux = df_aux.iloc[0][var_aux]
        return res_aux

    def category_image(self):
        """Category of image

        Returns:
            String: Category of image
        """   
        df_aux = self.dataset.loc[
            self.dataset[self.file_name_column] == self.name]
        res_aux = df_aux.iloc[0]['CATEGORY']
        return res_aux


    def rename_image(self, new_name):
        """Rename_image

        Args:
            new_name (string): new name of image

        Returns:
            String: image renamed
        """
        df_aux = self.dataset.loc[
            self.dataset[self.file_name_column] == self.name]
        last_image = df_aux.iloc[0]['ROUTE']
        cat_image = df_aux.iloc[0]['CATEGORY']
        new_image = self.path+ '/' + cat_image +"/images/"+ new_name + '.png'
        os.rename(last_image, new_image)
        df_aux.iloc[0].replace(to_replace=last_image, value = new_image)
        return print('Imagen ' + self.name 
                     +' cambio su nombre a: ' + new_name)

    def delete_image(self):
        """Delete image

        Returns:
            String: deleted image
        """
        df_aux = self.dataset.loc[
            self.dataset[self.file_name_column] == self.name]
        route_image = df_aux.iloc[0]['ROUTE']
        os.remove(route_image)
        df_2 = self.dataset.loc[self.dataset['ROUTE'] != route_image]
        df_2 = df_2.reset_index()
        df_2 = df_2.drop(['index'], axis=1)
        return print('Imagen ' + self.name +' removida correctamente')

    def visualize_img_category(self):
        """Visualization of the image

        Returns:
            Image: visualization of the image
        """
        dataset = pd.DataFrame(self.dataset)
        df_aux = dataset.loc[dataset[self.file_name_column] == self.name]
        df_aux = df_aux.reset_index()
        var = df_aux.at[0,"ROUTE"]
        plt.rcParams["figure.figsize"] = (15,8)
        img = cv2.imread(var)
        #plt.title(self.name)
        #plt.imshow(img)
        cv2.imshow(self.name,img)
        cv2.waitKey(0)

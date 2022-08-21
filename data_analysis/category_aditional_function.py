import pandas as pd
import cv2
import random

from matplotlib import pyplot as plt

class CategoryAditionalFunction:
    """Aditional functions (Graphic of image per category
    , visualization of 3 random images per category
    , most and less repeated category by number of images)
    """
    def __init__(self, dataset, categories):
        self.dataset = dataset
        self.categories = categories

    def count_graph_category(self):
        """Graphic of categorias by number of images

        Returns:
            Plot: number of images by category
        """
        df_aux = pd.DataFrame(self.dataset)
        df_aux = pd.DataFrame(
            df_aux.groupby(['CATEGORY']
                           , as_index=False)['CATEGORY_ID'].count())
        df_aux1 = df_aux['CATEGORY'].to_numpy()
        df_aux2 = df_aux['CATEGORY_ID'].to_numpy()
        plt.rcdefaults()
        fig, ax = plt.subplots()
        imagenes = (len(df_aux1))

        ax.barh(df_aux1, df_aux2, align='center')
        ax.invert_yaxis()
        ax.set_xlabel('Imagenes')
        ax.set_title('Grafico de imagen por categoria')
        plt.show()
        fig.savefig('nueva_imagen.jpeg', dpi = 100)

    def visualize_all(self):
        """3 random images per catogory

        Returns:
            Array of random images separated by category
        """
        dataset = pd.DataFrame(self.dataset)
        len_cat = len(dataset["CATEGORY"].unique())
        plt.rcParams["figure.figsize"] = (15,8) 
        images = []
        num_images = 3
        cat = dataset["CATEGORY"].unique()

        for classes in cat:
            vars()[classes] = pd.DataFrame(dataset[
                dataset['CATEGORY'] == classes]).reset_index()

            for num in range(num_images):
                aux_1 = vars()[classes]

                random_image = random.randint(0,len(aux_1)-1)
                images.append(
                    [aux_1.at[random_image,"ROUTE"]
                            ,self.categories[aux_1.at[random_image
                                                      ,"CATEGORY_ID"]]])

        for index, sample in enumerate(images):
            img = cv2.imread(sample[0])
            plt.subplot(len_cat, 3, index+1), plt.imshow(img)
            plt.title(sample[1])
            plt.xticks([]), plt.yticks([])

    def most_repeated_category(self):
        """Category with most images

        Returns:
            String: category with most images
        """
        dataset = pd.DataFrame(self.dataset)
        df_aux = pd.DataFrame(dataset.groupby(['CATEGORY']
                                 , as_index=False)['CATEGORY_ID'].count())
        cat_max = pd.DataFrame(df_aux.max())
        cat_max = cat_max.reset_index()
        cat_max = cat_max.iloc[0][0]
        return print(cat_max)

    def less_repeated_category(self):
        """Category with less images

        Returns:
            String: category with less images
        """
        dataset = pd.DataFrame(self.dataset)
        df_aux = pd.DataFrame(dataset.groupby(['CATEGORY']
                                 , as_index=False)['CATEGORY_ID'].count())
        cat_min = pd.DataFrame(df_aux.min())
        cat_min = cat_min.reset_index()
        cat_min = cat_min.iloc[0][0]
        return print(cat_min)
    
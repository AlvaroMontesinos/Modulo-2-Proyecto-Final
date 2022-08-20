import unittest
import sys
from tkinter import Image
from os.path import dirname, abspath
d= dirname(dirname(abspath(__file__)))
sys.path.append(d)

from data_analysis.imagen import Imagen
from data_processing.set_to_dataframe import set_to_dataframe
from data_processing.encode_dataframe import encoder_dataframe
from data_processing.image_dimmension import add_dim_images

name = 'COVID-1'
path = r'C:/Users/Eduardo/Documents/Estudios/MCDD/Modulo2 IS/Proyecto_Final/dataset'
categories = ['COVID', 'Lung_Opacity', 'Normal', 'Viral Pneumonia']
column_name = 'FILE NAME'
subfolder = 'images'

dataset = set_to_dataframe(categories, path)
dataset = encoder_dataframe(dataset, 'CATEGORY')
dataset = add_dim_images(dataset, path, column_name, subfolder)

class TestImageDim(unittest.TestCase):
    """Test to verify image dimmension
    """
    def test_image_height(self):
        '''test to verify image height'''
        res = dataset.loc[dataset['FILE NAME'] == name]
        res = res.iloc[0]['images_HEIGHT']
        self.assertEqual(res,299.0)

    def test_image_width(self):
        '''test to verify image width'''
        res = dataset.loc[dataset['FILE NAME'] == name]
        res = res.iloc[0]['images_WIDTH']
        self.assertEqual(res,299.0)

suite = unittest.TestLoader().loadTestsFromTestCase(TestImageDim)
_ = unittest.TextTestRunner().run(suite)
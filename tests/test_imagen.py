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
from data_processing.image_path import add_route

name = 'COVID-1'
path = r'C:/Users/Eduardo/Documents/Estudios/MCDD/Modulo2 IS/Proyecto_Final/dataset'
categories = ['COVID', 'Lung_Opacity', 'Normal', 'Viral Pneumonia']
file_name_column = 'FILE NAME'
subfolder = 'images'

dataset = set_to_dataframe(categories, path)
dataset = encoder_dataframe(dataset, 'CATEGORY')
dataset = add_route(dataset, path, file_name_column)
dataset = add_dim_images(dataset, path, file_name_column, subfolder)

img = Imagen(name, path, dataset, file_name_column, subfolder)

class TestImage(unittest.TestCase):
    """Test to verify image dimension
    """
    def test_image_height(self):
        '''test to verify image height'''
        res = img.height()
        self.assertEqual(res,299.0)

    def test_image_width(self):
        '''test to verify image widtht'''
        res = img.width()
        self.assertEqual(res,299.0)

    def test_image_category(self):
        '''test to verify image category'''
        res = img.category_image()
        self.assertEqual(res,'COVID')

suite = unittest.TestLoader().loadTestsFromTestCase(TestImage)
_ = unittest.TextTestRunner().run(suite)
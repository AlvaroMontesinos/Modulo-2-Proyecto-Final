import unittest
import sys
from tkinter import Image
from os.path import dirname, abspath
d= dirname(dirname(abspath(__file__)))
sys.path.append(d)

from data_analysis.imagen import Imagen
from data_processing.set_to_dataframe import set_to_dataframe
from data_processing.encode_dataframe import encoder_dataframe
from data_processing.image_path import add_route

name = 'COVID-1'
path = r'C:/Users/Eduardo/Documents/Estudios/MCDD/Modulo2 IS/Proyecto_Final/dataset'
categories = ['COVID', 'Lung_Opacity', 'Normal', 'Viral Pneumonia']
column_name = 'FILE NAME'

dataset = set_to_dataframe(categories, path)
dataset = encoder_dataframe(dataset, 'CATEGORY')
dataset = add_route(dataset, path, column_name)

class TestImageRoute(unittest.TestCase):
    """Test to verify a new column with route of image
    """
    def test_image_path(self):
        '''test to verify route of image'''
        res = dataset.loc[dataset['FILE NAME'] == name]
        res = res.iloc[0]['ROUTE']
        self.assertEqual(
            res
            ,'''C:/Users/Eduardo/Documents/Estudios/MCDD/Modulo2 IS/Proyecto_Final/dataset/COVID/images/COVID-1.png''')

suite = unittest.TestLoader().loadTestsFromTestCase(TestImageRoute)
_ = unittest.TextTestRunner().run(suite)
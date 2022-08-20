import unittest
import sys
from tkinter import Image
from os.path import dirname, abspath
d= dirname(dirname(abspath(__file__)))
sys.path.append(d)

from data_analysis.imagen import Imagen
from data_processing.set_to_dataframe import set_to_dataframe
from data_processing.encode_dataframe import encoder_dataframe

name = 'COVID-1'
path = r'C:/Users/Eduardo/Documents/Estudios/MCDD/Modulo2 IS/Proyecto_Final/dataset'
categories = ['COVID', 'Lung_Opacity', 'Normal', 'Viral Pneumonia']

dataset = set_to_dataframe(categories, path)
dataset = encoder_dataframe(dataset, 'CATEGORY')

class TestEncodeDataframe(unittest.TestCase):
    """Test to verify encode column in dataframe
    """
    def test_image_height(self):
        '''test to verify image height'''
        res = dataset.loc[dataset['FILE NAME'] == name]
        res = res.iloc[0]['CATEGORY_ID']
        self.assertEqual(res,0)

suite = unittest.TestLoader().loadTestsFromTestCase(TestEncodeDataframe)
_ = unittest.TextTestRunner().run(suite)

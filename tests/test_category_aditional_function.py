import unittest
import sys
from datetime import date
from os.path import dirname, abspath
d= dirname(dirname(abspath(__file__)))
sys.path.append(d)

from data_analysis.category_aditional_function import CategoryAditionalFunction
from data_processing.set_to_dataframe import set_to_dataframe
from data_processing.encode_dataframe import encoder_dataframe

categories = ['COVID', 'Lung_Opacity', 'Normal', 'Viral Pneumonia']
path = r'C:/Users/Eduardo/Documents/Estudios/MCDD/Modulo2 IS/Proyecto_Final/dataset'

dataset = set_to_dataframe(categories, path)
dataset = encoder_dataframe(dataset, 'CATEGORY')
cat_aux = CategoryAditionalFunction(dataset,categories)

class TestAditionalFunction(unittest.TestCase):
    """Test to verify the category with most images
    """
    def test_most_repeat(self):
        '''test to see most repeated image'''
        res = str(cat_aux.most_repeated_category())
        self.assertTrue(res,'Viral Pneumonia')

    def test_less_repeat(self):
        '''test to see less repeated image'''
        res = str(cat_aux.less_repeated_category())
        self.assertTrue(res,'COVID')

suite = unittest.TestLoader().loadTestsFromTestCase(TestAditionalFunction)
_ = unittest.TextTestRunner().run(suite)

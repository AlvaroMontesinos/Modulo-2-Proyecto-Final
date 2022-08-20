import unittest
import sys
from os.path import dirname, abspath
d= dirname(dirname(abspath(__file__)))
sys.path.append(d)

from data_analysis.category import Category
from data_processing.set_to_dataframe import set_to_dataframe

categories = ['COVID', 'Lung_Opacity', 'Normal', 'Viral Pneumonia']
path = r'C:/Users/Eduardo/Documents/Estudios/MCDD/Modulo2 IS/Proyecto_Final/dataset'
category_1 = 'COVID'
category_2 = 'Lung_Opacity'
category_3 = 'Normal'
category_4 = 'Viral Pneumonia'

dataset = set_to_dataframe(categories, path)
category_var_1 = Category(category_1, dataset)
category_var_2 = Category(category_2, dataset)
category_var_3 = Category(category_3, dataset)
category_var_4 = Category(category_4, dataset)

class TestImageCount(unittest.TestCase):
    """Test to verify count of images
    """
    def test_equal_count_covid(self):
        '''test to count covid images'''
        res = category_var_1.image_count()
        self.assertEqual(res,3616)

    def test_equal_count_lung(self):
        '''test to count lung images'''
        res = category_var_2.image_count()
        self.assertEqual(res,6012)

    def test_equal_count_normal(self):
        '''test to count normal images'''
        res = category_var_3.image_count()
        self.assertEqual(res,10192)

    def test_equal_count_pnemunonia(self):
        '''test to count penumonia images'''
        res = category_var_4.image_count()
        self.assertEqual(res,1345)


suite = unittest.TestLoader().loadTestsFromTestCase(TestImageCount)
_ = unittest.TextTestRunner().run(suite)
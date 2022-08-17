import unittest

from data_analysis.image_count import image_count
from data_management.set_to_dataframe import set_to_dataframe

categories = ['COVID', 'Lung_Opacity', 'Normal', 'Viral Pneumonia']
path = r'C:/Users/Eduardo/Documents/Estudios/MCDD/Modulo2 IS/datasetCovid'
dataset = set_to_dataframe(categories, path)



class Test_image_count(unittest.TestCase):

    def test_equal_count_covid(self):
        '''test to count covid images'''
        res = image_count(dataset, 'COVID')
        self.assertEqual(res,3616)

    def test_equal_count_lung(self):
        '''test to count lung images'''
        res = image_count(dataset, 'Lung_Opacity')
        self.assertEqual(res,6012)

    def test_equal_count_normal(self):
        '''test to count normal images'''
        res = image_count(dataset, 'Normal')
        self.assertEqual(res,10192)

    def test_equal_count_pnemunonia(self):
        '''test to count penumonia images'''
        res = image_count(dataset, 'Viral Pneumonia')
        self.assertEqual(res,1345)


suite = unittest.TestLoader().loadTestsFromTestCase(Test_image_count)
_ = unittest.TextTestRunner().run(suite)
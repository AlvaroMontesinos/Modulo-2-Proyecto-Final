import pandas as pd
import numpy as np
import os
import random
import cv2
import unittest
import statistics
import plotext as plt 

from json import encoder
from re import sub
from matplotlib import pyplot as plt
from sklearn.preprocessing import OrdinalEncoder
from PIL import Image
from tqdm.auto import tqdm
from tkinter.messagebox import RETRY

from data_processing.xlsx_to_csv import xlsx_to_csv
from data_processing.set_to_dataframe import set_to_dataframe
from data_processing.encode_dataframe import encoder_dataframe
from data_processing.image_dimmension import add_dim_images
from data_processing.image_path import add_route
from data_processing.create_file import create_file

from data_analysis.imagen import Imagen
from data_analysis.category import Category
from data_analysis.category_aditional_function import CategoryAditionalFunction

print('''*************************************
        \n***** PROCESAMIENTO DE DATASETS *****
        \n*************************************''')

print('''\nProyecto para la lectura y procesamiento de datasets
        \nLos datos necesario son:'''+
        '\n- Lista con las categorias de las imagenes.'+
        '\n- Ubicacion de la carpeta con imagenes y '+
        'los sets de datos en formato .xlsx o .csv'+
        '\n- Nombre de la columna con el nombre de las imagenes. '+
        '\n- Nombre del subfolder con las imagenes en la ubicacion.')

print('\nEl dataset generado contendra las siguientes columnas:'+
        '\n- Columnas por defecto del archivo original.'+
        '\n- Columna CATEGORY.'+
        '\n- Columna CATEGORY_ID.'+
        '\n- Columna ROUTE.'+
        '\n- Columnas con el alto y ancho de las imagenes.\n')

categories = []
var_cat = int(input('''Ingrese el Nro de categorias y categorias: '''))
#['COVID', 'Lung_Opacity', 'Normal', 'Viral Pneumonia']

for i in range(0, var_cat):
    aux_cat = str(input())
    categories.append(aux_cat)

var_path = input('Ingrese la ubicacion de los set de datos: ')
#C:/Users/Eduardo/Documents/Estudios/MCDD/Modulo2 IS/Proyecto_Final/dataset
#C:/Users/lmamanic/Documents/MCDD/Final/Data

var_column_name = input('Ingrese el nombre de la columna de imagenes: ')
# FILE NAME

var_subfolder = input('Ingrese el nombre del folder con las imagenes: ' )
# images

var_format = input('Ingrese el formato de archivo XLSX/CSV: ' )
# XLSX o CSV

var_folder = input('Las imagenes estan en carpetas por categoria? S/N: ' )
# SI o NO



if var_folder == 'N':
    create_file(var_path, categories)

if var_format == 'XLSX':
    xlsx_to_csv(categories, var_path)

dataset = set_to_dataframe(categories, var_path)
dataset = encoder_dataframe(dataset, 'CATEGORY')
dataset = add_route(dataset, var_path, var_column_name)
dataset = add_dim_images(dataset, var_path, var_column_name, var_subfolder)

print('\nA continuacion se muestra el dataset resultante: \n')
print(dataset)

var_analysis = ''
var_img_2 = 0
cat_2 = 0
adi_1 = 0

while var_analysis != 'EXIT' and var_img_2 < 7 and cat_2 < 3 and adi_1 < 5:
    print('\n- Para analizar categorias ingrese: CAT'+
                    '\n- Para analizar imagenes ingrese: IMG'+
                    '\n- Para analisis adicional: AUX'+
                    '\n- Para salir, ingrese: EXIT')
    var_analysis = input('\nIngrese el valor de categoria: ')

    if var_analysis == 'IMG':
        var_img = input('Ingrese el nombre de la imagen: ')
        print('\n- Para ver la altura de la imagen ingrese: 1'+
                '\n- Para ver el ancho de la imagen ingrese: 2'+
                '\n- Para ver la categoria de la imagen ingrese: 3'+
                '\n- Para visualizar la imagen ingrese: 4'+
                '\n- Para renombrar la imagen ingrese: 5'+
                '\n- Para eliminar la imagen ingrese: 6')
        var_img_2 = int(input('\nIngrese el valor de analisis por imagen:'))
        img = Imagen(var_img, var_path, dataset
                        , var_column_name, var_subfolder)

        if var_img_2 == 1:
            res_1 = img.height()
            print(res_1)
        elif var_img_2 == 2:
            res_1 = img.width()
            print(res_1)
        elif var_img_2 == 3:
            res_1 = img.category_image()
            print(res_1)
        elif var_img_2 == 4:
            img.visualize_img_category()
        elif var_img_2 == 5:
            res_aux = input('Ingrese el nuevo nombre: ')
            res_1 = img.rename_image(res_aux)
            print(res_1)
        elif var_img_2 == 6:
            res_1 = img.delete_image()
            print(res_1)
        else:
            print('Valor no valido')

    elif var_analysis == 'CAT':
        cat_1 = input('Ingrese el nombre de la categoria a analizar: ')
        print('\n- Para ver la cantidad de imagenes: 1'+
                '\n- Para visualizar una imagen aleatoria: 2')
        cat_2 = int(input('\nIngrese el valor de analisis por categoria:'))
        category_var = Category(cat_1, dataset)

        if cat_2 == 1:
            res_1 = category_var.image_count()
            print(res_1)
        elif cat_2 == 2:
            category_var.visualize_img_category()
        else:
            print('Valor no valido')

    elif var_analysis == 'AUX':
        print('\n- Para ver el grafico de cantidad de imagenes: 1'+
                '\n- Para ver 3 imagenes aleatorias por categoria: 2'+
                '\n- Para ver la categoria mas repetida: 3'+
                '\n- Para ver la categoria menos repetida: 4')
        adi_1 = int(input('\nIngrese el valor de analisis adicional:'))
        adi_var = CategoryAditionalFunction(dataset, categories)

        if adi_1 == 1:
            adi_var.count_graph_category()
        elif adi_1 == 2:
            adi_var.visualize_all()
        elif adi_1 == 3:
            adi_var.most_repeated_category()
        elif adi_1 == 4:
            adi_var.less_repeated_category()
        else:
            print('Valor no valido')
    else:
        print('Adios!')

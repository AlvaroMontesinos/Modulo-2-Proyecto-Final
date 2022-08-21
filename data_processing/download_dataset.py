import json
from sklearn.model_selection import train_test_split
import os
from tqdm.auto import tqdm
import shutil


def import_dataset_kaggle(user, key, path, path_json, name_zip):

    # Ver si el archivo no ha sido creado
    KAGGLE_PATH = path_json
    #C:/Users/Eduardo/Documents/Estudios/MCDD/Modulo2 IS/Proyecto_Final/.kaggle
    if os.path.exists(KAGGLE_PATH):
      !rm -r "$KAGGLE_PATH"

    !mkdir "$KAGGLE_PATH"
    !touch "$KAGGLE_PATH/kaggle.json"

    api_token = {"username":user,"key":key}

    # Crea el archivo con las credenciales
    with open(KAGGLE_PATH +'/kaggle.json', 'w') as file:
        json.dump(api_token, file)

    # Cambia los permisos de acceso
    !chmod 600 ~/.kaggle/kaggle.json

    %cd C:/Users/Eduardo/Documents/Estudios/MCDD/Modulo2 IS/Proyecto_Final

    # Valida si el conjunto de datos ya se ha descargado y sino reemplaza
    #C:/Users/Eduardo/Documents/Estudios/MCDD/Modulo2 IS/Proyecto_Final/dataset
    if not os.path.exists(path):
      os.makedirs('dataset')
    else: 
      !rm -rf dataset
      os.makedirs('dataset')

    # Descargar el dataset desde Kaggle
    !kaggle datasets download -d tawsifurrahman/covid19-radiography-database -p dataset

    # Descomprimir el dataset 
    var_zip = path + '/' + name_zip + '.zip'
    #C:/Users/Eduardo/Documents/Estudios/MCDD/Modulo2 IS/Proyecto_Final/dataset/covid19-radiography-database.zip
    !unzip -qn var_zip -d path > /dev/null
    !rm var_zip
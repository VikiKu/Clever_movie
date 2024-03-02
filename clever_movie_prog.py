# -*- coding: utf-8 -*-
"""clever_movie_prog.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TCSa-GOaF2WaEQFIClxUXR2Q5yrVcY4j
"""

# загрузка необходимых библиотек
import zipfile #для работы с архивами
import os #для работы с файловой системой
import numpy as np
import pandas as pd
from google.colab import drive #для работы с диском

#подключение гугл диска
drive.mount('/content/drive')

zip_file='/content/drive/MyDrive/archive.zip'
#распаковка архива
z = zipfile.ZipFile(zip_file, 'r')
z.extractall()
#просмотр результата
print(os.listdir())

path = 'dataset'
df = pd.DataFrame(columns=['id1','review','sentiment']) # подготовка таблицы
prop = 0.01 # часть файлов, которую использую

for directory in os.listdir('dataset'): # перебираем все папки из датасета (нейтральные, позитивные, негативные отзывы)
    if os.path.isdir('dataset'+'/'+ directory): # если это папка
        dirs = np.array(os.listdir('dataset'+ '/'+ directory)) # создаем массив названий файлов
        np.random.shuffle(dirs) # перемешиваем порядок файликов
        rews_fhs = np.random.choice(dirs, round(len(dirs) * prop)) # выбор рандомных prop процентов с округлением

        for rew_fh in rews_fhs: # для каждого файла из выбранных
            a = os.path.splitext(rew_fh)[0]
            with open(os.path.join('dataset' + '/'+ directory + '/', rew_fh), encoding='utf-8') as f: # тут оператор with открывает и автоматически закрывает файл по выходу из блока
                review = f.read() # записываем в переменную текст с отзывом
                current_df = pd.DataFrame({'id1':[a],'review': [review], 'sentiment': directory}) # запись в dataframe
                df = df.append(current_df, ignore_index=True) # добавляем построчно в датафрейм каждый файл

df = df.sample(frac=1).reset_index(drop=True) # перемешивание строк

new_df = df['id1'].str.split('-',expand=True)
new_df.columns=['id','comment_number']
final_df = pd.concat([new_df, df],axis=1).drop('id1', axis=1)
data_types_dict = {'id': int}
final_df=final_df.astype(data_types_dict)
final_df.sort_values(by='id',ascending=True, ignore_index=True) # сортировка по возрастанию id
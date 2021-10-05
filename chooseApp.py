import os
import glob
import csv
import pandas as pd
import re
import shutil

def chooseapp():
    df = pd.read_excel(r'new.xlsx', skiprows='2:11', usecols='A,B,C')
    df = df[df['Name'].astype(str).str.startswith('CVE-')]
    df.to_excel('cvelist.xlsx')

    my_list = []
    while True:
        inpt = (input("Введите наименование ПО, Enter - выход\n"))
        if inpt == '':
            # Закончить ввод чисел
            break
        else:
            my_list.append(inpt)

    path = "output"
    try:
        os.mkdir(path)
    except OSError:
        print("Создать директорию %s не удалось или директория была создана ранее" % path)
    else:
        print("Успешно создана директория %s " % path)

    for apps in my_list:
        #    res = df[df["Description"].str.contains(apps, case=False, na=False).astype(int)]
        res = df[df["Description"].str.contains(apps)]
        output_file = apps + '.xlsx'
        res.to_excel(output_file, index=False)
        shutil.copy(
            os.path.join(output_file),
            os.path.join('output')
        )

    in_3 = 'output\*.xlsx'
    files = glob.glob(in_3)

    df = pd.concat([pd.read_excel(f) for f in files])
    df.to_excel(r'vulnreport.xlsx', index=False)

    print("Информация об уязвимостях всех указанных компонентов представлена в файле vulnreport.xlsx в каталоге output")
    print("Информация об уязвимостях компонентов по отдельности находится в каталоге output")

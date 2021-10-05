import os
import shutil

def prepare():
    path = os.getcwd()

    try:
        shutil.rmtree('/output/')
        os.rmdir(path)
    except:
        pass

    filelist = []
    for root, dirs, files in os.walk(path):
        for file in files:
            filelist.append(os.path.join(root, file))

    csvlist = []
    csvname = ".csv"
    xlsxlist = []
    xlsxname = ".xlsx"
    for name in filelist:
        if xlsxname in name:
            xlsxlist.append(name)
        elif csvname in name:
            csvlist.append(name)

    for name in xlsxlist:
        os.remove(name)

    for name in csvlist:
        os.remove(name)
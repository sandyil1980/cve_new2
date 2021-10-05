import os
import shutil

def finish():
    shutil.copy(
        os.path.join('vulnreport.xlsx'),
        os.path.join('output')
    )

    path = os.getcwd()
    filelist = []
    for root, dirs, files in os.walk(path):
        for file in files:
            filelist.append(os.path.join(root, file))

    xlsxlist = []
    csvlist = []
    xlsxname = ".xlsx"
    csvname = ".csv"

    listonlyfiles = []
    dirname = 'output'
    for name in filelist:
        if dirname in name:
            pass
        else:
            listonlyfiles.append(name)

    for name in listonlyfiles:
        if xlsxname in name:
            xlsxlist.append(name)
        elif csvname in name:
            csvlist.append(name)
        else:
            pass

    for name in xlsxlist:
        os.remove(name)

    for name in csvlist:
        os.remove(name)

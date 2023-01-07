import os
import datetime


def rename_file(filename):
    project_path = os.getcwd()
    path = project_path + '\\data\\'
    now = datetime.datetime.now().strftime("%Y_%m_%d_%H")
    os.rename(path + filename, path + f'offers_{now}.xlsx')

if __name__ == '__main__':
    rename_file('offers_07_01_2023_21H')
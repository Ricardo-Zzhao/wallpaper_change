import os, sys
import random
import shutil
import time

def getJpg(filename: str):
    return filename.endswith("jpg")

def getFile(fileDir, toFileDir, number):
    path = os.path.abspath(fileDir) + "/"
    path.replace("\\", "/")
    if os.path.isdir(fileDir):
        pathList = os.listdir(fileDir)
        jpgList = [i for i in filter(getJpg, pathList)]
        if jpgList:
            try:
                sample = random.sample(jpgList, number)
            except:
                print("某层文件夹图片数量不够")
                return
            for name in sample:
                try:
                    shutil.copy(path + name, toFileDir)
                except:
                    filename = str(time.time()).replace('.', '') + ".jpg"
                    path = path.replace("\\", "/")
                    os.rename(path + name, path + filename)
                    shutil.copy(path + filename, toFileDir)
        dirList = set(pathList) - set(jpgList)
        if dirList:
            for dir in dirList:
                getFile(path + dir, toFileDir, number)


if __name__ == "__main__":
    fileDir = r'D:\桌面\python\wallpaper_change\wallpaper'
    toFileDir = r'D:\桌面\python\wallpaper_change\壁纸生成库'
    number = '8'
    getFile(fileDir, toFileDir, int(number))

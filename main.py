import os
import shutil

def createFolder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

createFolder("images")
createFolder("docs")
createFolder("others")
createFolder("videos")
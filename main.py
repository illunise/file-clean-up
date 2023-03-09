import os
import shutil

def createFolder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

createFolder("images")
createFolder("docs")
createFolder("others")
createFolder("videos")

dir_list = os.listdir()

image_ext = [".png", '.jpg', '.jpeg']
docs_ext = [".docs", '.bat', '.bin', '.csv', 'doc', '.docx', '.html', '.htm', '.iso', '.pdf', '.ppt', '.psd', '.xls', '.xlsx']
videos_ext = [".avi", '.gif', '.m4a', '.mov', '.mp4', '.mpeg']
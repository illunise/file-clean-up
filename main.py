import os

def createFolder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


createFolder("images")
createFolder("docs")
createFolder("others")
createFolder("videos")
createFolder("audios")

dir_list = os.listdir()

image_ext = [".png", '.jpg', '.jpeg']
docs_ext = [".docs", '.bat', '.bin', '.csv', '.doc', '.docx', '.html', '.htm', '.iso', '.pdf', '.ppt', '.psd', '.xls', '.xlsx']
videos_ext = [".avi", '.gif', '.mov', '.mp4', '.mpeg', '.mkv']
audio_ext = [".mp3", '.wav', '.aa', '.aac', '.m4a', '.m4p']

dir_list.remove("main.py")

for file in dir_list:
    if os.path.splitext(file)[-1] in image_ext:
        os.replace(file, f"images/{file}")
    elif os.path.splitext(file)[-1] in docs_ext:
        os.replace(file, f"docs/{file}")
    elif os.path.splitext(file)[-1] in videos_ext:
        os.replace(file, f"videos/{file}")
    elif os.path.splitext(file)[-1] in audio_ext:
        os.replace(file, f"audios/{file}")
    elif os.path.splitext(file)[-1] not in image_ext and os.path.splitext(file)[-1] not in docs_ext and os.path.splitext(file)[-1] not in videos_ext and os.path.splitext(file)[-1] not in audio_ext and os.path.isfile(file):
        os.replace(file, f"others/{file}")
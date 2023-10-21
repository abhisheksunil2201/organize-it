import time
import os
import shutil

def organize():
    downloads_folder_path = os.path.join(os.path.expanduser("~"), "Downloads")
    #create extensions dictionary with their filenames mapped to their extensions
    extensions = {
        "mp3": "Audios",
        "mp4": "Videos",
        "jpg": "Images",
        "jpeg": "Images",
        "png": "Images",
        "gif": "Images",
        "docx": "Documents",
        "doc": "Documents",
        "txt": "Documents",
        "pdf": "Documents",
        "exe": "Programs",
        "msi": "Programs",
        "zip": "Compressed",
        "rar": "Compressed",
        "": "Other"
    }
    
    for filename in os.listdir(downloads_folder_path):
        # ignore directories
        if os.path.isdir(os.path.join(downloads_folder_path, filename)):
            continue
        # get the file extension
        extension = os.path.splitext(filename)[1][1:].lower()
        #only move files that have an extension mp3 or mp4
        if extension not in ["mp3", "mp4"]:
            continue
        extension = extensions.get(extension, 'Other')
        if not os.path.exists(os.path.join(downloads_folder_path, extension)):
            os.mkdir(os.path.join(downloads_folder_path, extension))
        # move the file to the appropriate folder
        shutil.move(os.path.join(downloads_folder_path, filename), os.path.join(downloads_folder_path, extension, filename))

def main():
    while True:
        organize()
        #timeout for 5
        print("Organizing...")
        time.sleep(5)

if __name__ == "__main__":
    main()
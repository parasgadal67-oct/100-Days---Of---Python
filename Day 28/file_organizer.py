# FILE ORGANIZER SCRIPT
#CONCEPT USED : O.S module, Try/Except, For loop.
import os
try:
    folder = r"C:/Users/paras/OneDrive/Desktop/test folder"
    folders_map = {
        "jpg" : "images",
        "png" : "images",
        "pdf" : "documents",
        "txt" : "documents",
        "mp3" : "music",
        "mp4" : "video"
    }
    for  filename in os.listdir(folder):
        extension =  os.path.splitext(filename)[1]
        extension = extension.replace(".","")
        
        if  extension in folders_map:
            destination = folders_map[extension]
            
            new_folder = os.path.join(folder, destination)
            os.makedirs(new_folder, exist_ok = True)
            
            old_path = os.path.join(folder, filename)
            new_path = os.path.join(new_folder, filename)
            
            os.rename(old_path,new_path)
            print(f"Moved {filename} to {destination}")
            
except FileNotFoundError:
    print("Sorry that file not to be found")        
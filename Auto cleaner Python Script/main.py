import os
import shutil

#-- Configuration --
source_folder = "/Users/sahilchauhan/Downloads"
organized_folder = "/Users/sahilchauhan/Downloads/Organized"
#File Type Categories
file_type ={
    "Image":[".jpg", ".jpeg", ".png", ".bmp", ".gif"],
    "Videos":[".mp4", ".mkv", ".mov", ".avi"],
    "Music":[".mp3", ".wav", ".flac"],
    "Documents":[".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Archives":[".zip", ".rar", ".tar", ".dmg", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java"],
    "Others": []

}

#-- MAIN FUNCTION --
def organize_folder():
    if not os.path.exists(organized_folder):
        os.makedirs(organized_folder)

    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False

            for folder_name, extensions in file_type.items():
                if file_ext in extensions:
                    dest_folder = os.path.join(organized_folder, folder_name)
                    os.makedirs(dest_folder, exist_ok = True) 
                    shutil.move(file_path, os.path.join(dest_folder, filename))
                    print(f"Moved: {filename} -> {folder_name}")
                    moved = True
                    break
            
            if not moved:
                other_folder =os.path.join (organized_folder,"Others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder,filename))
                print(f"Moved: {filename} -> Other")

    print("\n Folder Organized Successfully!")

if __name__== "__main__":
    organize_folder()
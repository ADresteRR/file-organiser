import os
import shutil

cwd = os.getcwd()

file_types = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".mp4": "Videos",
    ".pdf": "PDFs",
    ".ppt": "Presentations",
    ".pptx": "Presentations",
    ".exe": "Softwares",
    ".zip": "Archieves",
    ".docx": "Documents",
    ".xlsx": "Excels",
}

for file_name in os.listdir(cwd):
    source = os.path.join(cwd, file_name)
    if os.path.isfile(source):
        extension = os.path.splitext(source)[1].lower()
        if extension in file_types:
            # Get the destination folder name
            destination_folder = os.path.join(cwd, file_types[extension])

            # Create the destination folder if it doesn't exist
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            # Move the file to the destination folder
            destination = os.path.join(destination_folder, file_name)
            shutil.move(source, destination)
            print(f"Moved {file_name} to {destination_folder}")

print("Download folder organization completed!")

from pathlib import Path
import shutil

#Add folders if you want more variety.
necessary_folders = ["Images", "Documents", "Videos", "Executables", "Archives", "Audios"]

#Expand if necessary, if some file extensions are not included.
documents_extension = [".txt", ".pdf", ".docx", ".html", ".xlsx", ".csv",".sql",".doc", ".pptx", ".java", ".py", ".md",".ovpn"]
images_extension = [".png", ".jpg", ".jpeg", ".webp", ".gif", ".avif"]
executables_extensions = [".exe", ".deb", ".iso", ".msi", ".apk"]
videos_extensions = [".mp4", ".mov", ".avi", ".wmv", ".mkv"]
archives_extensions = [".zip", ".rar", ".lzip", ".7z", ".tar", ".gz", ".unitypackage", ".vrm", ".fbx",".lock"]
audio_extensions = [".mp3", ".wav", ".aiff", ".pcm",".aac", ".ogg", ".wma"]

#Don't forget to change your "your_name"
your_name = "Users"
downloads = Path(f"C:\\Users\\{your_name}\\Downloads")

for folder in necessary_folders:
    (downloads / folder).mkdir(exist_ok=True)

file_types = {
    "Documents": documents_extension,
    "Images": images_extension,
    "Executables": executables_extensions,
    "Videos": videos_extensions,
    "Archives": archives_extensions,
    "Audios": audio_extensions
}

for file in downloads.iterdir():
    if file.is_file():
        for folder, extensions in file_types.items():
            if file.suffix.lower() in extensions:
                shutil.move(file, downloads / folder / file.name)
                break
    else:
        print(f"{file.name} is a folder though?")

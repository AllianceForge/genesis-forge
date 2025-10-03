import os

def list_files(directory, extension=None):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    if extension:
        files = [f for f in files if f.lower().endswith(extension)]
    return files

def is_image(filename):
    return filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp"))

def is_json(filename):
    return filename.lower().endswith(".json")

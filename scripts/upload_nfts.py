import os
import requests

API_KEY = "TU_API_KEY_DE_PINATA"
IMG_DIR = "./output/images"
META_DIR = "./output/metadata"

def upload_file_to_pinata(filepath):
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    headers = {"pinata_api_key": API_KEY}
    with open(filepath, "rb") as f:
        response = requests.post(url, files={"file": f}, headers=headers)
    if response.ok:
        return response.json()["IpfsHash"]
    else:
        print("Error:", response.text)
        return None

def main():
    for folder in [IMG_DIR, META_DIR]:
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            ipfs_hash = upload_file_to_pinata(file_path)
            print(f"{filename}: {ipfs_hash}")

if __name__ == "__main__":
    main()

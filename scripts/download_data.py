import kagglehub
import shutil
import os

DATA_DIR = "data"

def download_data():
    # Only download if data folder is empty or missing
    if not os.path.exists(DATA_DIR) or not os.listdir(DATA_DIR):
        print("Downloading dataset...")

        path = kagglehub.dataset_download("meirnizri/covid19-dataset")

        os.makedirs(DATA_DIR, exist_ok=True)

        for file in os.listdir(path):
            shutil.copy(os.path.join(path, file), DATA_DIR)

        print("Dataset downloaded into /data")
    else:
        print("Data already exists. Skipping download.")

if __name__ == "__main__":
    download_data()

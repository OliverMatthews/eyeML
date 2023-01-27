import os
import zipfile
import requests
import tqdm

URL = "https://cecas.clemson.edu/~ahoover/stare/images/all-images.zip"


def download_images():
    # If the data/STARE/images folder does not exist, create it
    if not os.path.exists("data/STARE/images"):
        os.makedirs("data/STARE/images")

    # Create a progress bar
    r = requests.get(URL, stream=True)
    total_size = int(r.headers.get("content-length", 0))
    block_size = 1024
    t = tqdm.tqdm(total=total_size, unit="iB", unit_scale=True)

    print("Downloading STARE images from " + URL)
    # Download the data
    with open("data/STARE/all-images.zip", "wb") as f:
        for data in r.iter_content(block_size):
            t.update(len(data))
            f.write(data)
    t.close()

    # Create a progress bar
    total_size = os.path.getsize("data/STARE/all-images.zip")
    t = tqdm.tqdm(total=total_size, unit="iB", unit_scale=True)

    # Unzip the data
    print("Unzipping STARE images")
    with zipfile.ZipFile("data/STARE/all-images.zip", "r") as zip_ref:
        for file in zip_ref.namelist():
            zip_ref.extract(file, "data/STARE/images")
            t.update(os.path.getsize("data/STARE/images/" + file))
    t.close()

    # Delete the zip file
    os.remove("data/STARE/all-images.zip")

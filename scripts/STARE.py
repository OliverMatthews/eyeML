import os
import zipfile
import requests
import tqdm

images_url = "https://cecas.clemson.edu/~ahoover/stare/images/all-images.zip"
diagnoses_url = "https://gist.github.com/OliverMatthews/b3ce29edccdd835ac3719995f2b322ec/archive" \
                "/20258b7c08eee8a81d1320d216bc7b13bb00199a.zip"


def download_images():
    # If the data/STARE/images folder does not exist, create it
    if not os.path.exists("data/STARE/images"):
        os.makedirs("data/STARE/images")

    print("Downloading STARE images from " + images_url)

    # Create a progress bar
    r = requests.get(images_url, stream=True)
    total_size = int(r.headers.get("content-length", 0))
    block_size = 1024
    t = tqdm.tqdm(total=total_size, unit="iB", unit_scale=True)

    # Download the data
    with open("data/STARE/all-images.zip", "wb") as f:
        for data in r.iter_content(block_size):
            t.update(len(data))
            f.write(data)
    t.close()

    print("Unzipping STARE images.")

    # Create a progress bar
    total_size = os.path.getsize("data/STARE/all-images.zip")
    t = tqdm.tqdm(total=total_size, unit="iB", unit_scale=True)

    # Unzip the data
    with zipfile.ZipFile("data/STARE/all-images.zip", "r") as zip_ref:
        for file in zip_ref.namelist():
            zip_ref.extract(file, "data/STARE/images")
            t.update(os.path.getsize("data/STARE/images/" + file))
    t.close()

    # Delete the zip file
    os.remove("data/STARE/all-images.zip")


def download_diagnoses():
    # If the data/STARE/diagnoses folder does not exist, create it
    if not os.path.exists("data/STARE/"):
        os.makedirs("data/STARE/")

    print("Downloading STARE diagnoses data from " + diagnoses_url)

    # Create a progress bar
    r = requests.get(diagnoses_url, stream=True)
    total_size = int(r.headers.get("content-length", 0))
    block_size = 1024
    t = tqdm.tqdm(total=total_size, unit="iB", unit_scale=True)

    # Download the data
    with open("data/STARE/diagnoses.zip", "wb") as f:
        for data in r.iter_content(block_size):
            t.update(len(data))
            f.write(data)
    t.close()

    print("Unzipping STARE diagnoses data.")

    # Create a progress bar
    total_size = os.path.getsize("data/STARE/diagnoses.zip")
    t = tqdm.tqdm(total=total_size, unit="iB", unit_scale=True)

    # Unzip the data from the zip file
    with zipfile.ZipFile("data/STARE/diagnoses.zip", "r") as zip_ref:
        for file in zip_ref.namelist():
            zip_ref.extract(file, "data/STARE/")
            t.update(os.path.getsize("data/STARE/" + file))
    t.close()

    # Delete the zip file
    os.remove("data/STARE/diagnoses.zip")

    # Rename the file
    os.rename("data/STARE/b3ce29edccdd835ac3719995f2b322ec-20258b7c08eee8a81d1320d216bc7b13bb00199a",
              "data/STARE/diagnoses")

    # Move the file to the data/STARE folder
    os.replace("data/STARE/diagnoses/STARE_data.csv", "data/STARE/diagnoses.csv")

    # Delete the folder
    os.rmdir("data/STARE/diagnoses")


def download_complete():
    download_images()
    download_diagnoses()
